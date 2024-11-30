package main

import "fmt"

type executionFunc func(signal controlSignal)

var instructions map[int]executionFunc

func decodeInstruction(instruction int) controlSignal {
	opcode := (instruction >> 22) & 0b11111     // Extract bits 27-22
	src1 := (instruction >> 11) & 0b11111111111 // Extract bits 21-11
	src2 := (instruction) & 0b11111111111       // Extract bits 10-0
	return controlSignal{
		Command: opcode,
		Src1:    src1,
		Src2:    src2,
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
		0b00001: func(signal controlSignal) { // LOAD
			if validateRegisterAccess(signal.Src1) {
				registers[signal.Src1] = signal.Src2
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
	}
}

func cpuLogic() {

	addressBus <- programCounter
	signal := <-readDataBus

	instruction := decodeInstruction(signal)
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
