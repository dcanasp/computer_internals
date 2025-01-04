package main

import (
	"fmt"
	"os"
)

type executionFunc func(signal controlSignal)

var instructions map[int]executionFunc

func decodeInstruction(instruction int) controlSignal {
	opcode := (instruction >> 27) & 0b11111       // Extract bits 28-32
	src1 := (instruction >> 14) & 0b1111111111111 // Extract bits 15-27
	signSrc2 := (instruction >> 13) & 0b1         // Extract bit 14 el signo de src2
	src2 := (instruction) & 0b1111111111111       // Extract bits 0-13
	signSrc2 = 1 - 2*signSrc2                     // deja el signo en -1 o 1
	return controlSignal{
		Command:  opcode,
		Src1:     src1,
		Src2:     src2,
		SignSrc2: signSrc2,
	}
}

func execute(signal controlSignal) {
	operation, ok := instructions[signal.Command]
	if ok {
		operation(signal)
	} else {
		fmt.Printf("Unknown Operation: %05b\n", signal.Command)
	}
}

func alu(op, regA, regB int) (int, error) {
	switch op {
	case 0b00101:
		return regA + regB, nil
	case 0b00110:
		return regA - regB, nil
	case 0b00111:
		return regA * regB, nil
	case 0b01000:
		if regB == 0 {
			return 0, fmt.Errorf("division by zero")
		}
		return regA / regB, nil
	case 0b01001:
		if regB == 0 {
			return 0, fmt.Errorf("division by zero")
		}
		return regA % regB, nil
	default:
		fmt.Println("Unknown Operation: ", op)
		return 0, fmt.Errorf("unknown operation: %d", op)
	}
}

func aluMapper(signal controlSignal) {
	result, _ := alu(signal.Command, registers[signal.Src1], registers[signal.Src2])
	registers[signal.Src1] = result
}

func startInstructions() {
	instructions = map[int]executionFunc{
		0b00000: func(signal controlSignal) { // BEGIN
			if registers[0] == 0 {
				registers[0] = 1
				registers[1] = programCounter
			}
		},
		0b11111: func(signal controlSignal) { // END
			if registers[0] == 1 {
				registers[0] = 0
				registers[2] = programCounter
				programCounter = registers[1]
			}
		},
		0b11110: func(signal controlSignal) { // FIN
			os.Exit(0)
		},
		0b00001: func(signal controlSignal) { // LOAD
			if validateRegisterAccess(signal.Src1) {
				registers[signal.Src1] = signal.SignSrc2 * signal.Src2
			}
		},
		0b00010: func(signal controlSignal) { // STORE
			addressBus <- signal.Src1
			writeDataBus <- registers[signal.Src2]
			<-memoryDone
		},
		0b00011: func(signal controlSignal) { // MOVE
			if validateRegisterAccess(signal.Src1) {
				registers[signal.Src1] = registers[signal.Src2]
			}
		},
		0b00100: func(signal controlSignal) { //LOADDISK
			if validateRegisterAccess(signal.Src1) {
				addressBus <- signal.Src2
				data := <-readDataBus
				registers[signal.Src1] = data
			}
		},
		0b00101: func(signal controlSignal) { // ADD,
			if validateRegisterAccess(signal.Src1) {
				aluMapper(signal)
			}
		},
		0b00110: func(signal controlSignal) { // SUB,
			if validateRegisterAccess(signal.Src1) {
				aluMapper(signal)
			}
		},
		0b00111: func(signal controlSignal) { // MULT,
			if validateRegisterAccess(signal.Src1) {
				aluMapper(signal)
			}
		},
		0b01000: func(signal controlSignal) { // DIV,
			if validateRegisterAccess(signal.Src1) {
				aluMapper(signal)
			}
		},
		0b01001: func(signal controlSignal) { // MOD,
			if validateRegisterAccess(signal.Src1) {
				aluMapper(signal)
			}
		},
		0b01010: func(signal controlSignal) { // AND,
			registers[signal.Src1] = registers[signal.Src1] & registers[signal.Src2]
		},
		0b01011: func(signal controlSignal) { // OR,
			registers[signal.Src1] = registers[signal.Src1] | registers[signal.Src2]
		},
		0b01100: func(signal controlSignal) { // XOR,
			registers[signal.Src1] = registers[signal.Src1] ^ registers[signal.Src2]
		},
		0b01101: func(signal controlSignal) { // NOT,
			registers[signal.Src1] = registers[signal.Src1] ^ 0b1111111111111
		},
		0b01110: func(signal controlSignal) { // LEFTSHIFT,
			registers[signal.Src1] = registers[signal.Src1] << registers[signal.Src2]
		},
		0b01111: func(signal controlSignal) { // RightSHIFT,
			registers[signal.Src1] = registers[signal.Src1] >> registers[signal.Src2]
		},
		0b10000: func(signal controlSignal) { // CMP,
			if registers[signal.Src1] == signal.SignSrc2*signal.Src2 {
				registers[3] = 1
			} else {
				registers[3] = 0
			}
		},
		0b10001: func(signal controlSignal) { // CMPREG,
			if registers[signal.Src1] == registers[signal.Src2] {
				registers[3] = 1
			} else {
				registers[3] = 0
			}
		},
		0b10010: func(signal controlSignal) { // JUMP,
			programCounter = signal.Src1
		},
		0b10011: func(signal controlSignal) { // JEQ,
			if registers[3] == 1 {
				programCounter = signal.Src1
			}
		},
		0b10100: func(signal controlSignal) { // JNE,
			if registers[3] == 0 {
				programCounter = signal.Src1
			}
		},
	}
}

func cpuLogic() {

	addressBus <- programCounter
	signal := <-readDataBus

	instruction := decodeInstruction(signal)
	if instruction.Command == 0b10011 {
		fmt.Println("JUMP")
	}
	if instruction.Command == 0b11111 {
		execute(instruction)
	}
	if registers[0] == 0 {
		execute(instruction)
	}
	programCounter++
}

func cpu() {
	startInstructions()
	first := true
	for {
		if !first {
			cpuDone <- true
		}
		<-controlBus
		first = false
		cpuLogic()
		flag := false
		//ejecutar rutinas
		for programCounter < registers[2] {
			cpuLogic()
			flag = true
		}
		if flag {
			registers[1] = 0
			registers[2] = 0
		}

	}
}
