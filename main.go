package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
	"sync"
)

// var instructions = []string{"ADD", "SUB", "MULT"} //no hace nada
var dataMemory = make([]int, 1024)
var registers = make([]int, 32)

var controlBus = make(chan ControlSignal)
var addressBus = make(chan int)
var readDataBus = make(chan int)
var writeDataBus = make(chan int)

var done = make(chan bool)

type ControlSignal struct {
	Command string // e.g., "ADD", "LOAD", "STORE"
	Src1    int    // Source register 1
	Src2    int    // Source register 2 or immediate value
}

func CPU() {
	for {
		// Wait for control signal
		signal := <-controlBus

		switch signal.Command {
		case "LOAD":
			registers[signal.Src1] = signal.Src2 // Store data in the destination register
		case "LOADDISK":
			addressBus <- signal.Src2     // Send address to address bus
			data := <-readDataBus         // Read data from data bus
			registers[signal.Src1] = data // Store data in the destination register
		case "STORE":
			addressBus <- signal.Src1              // Send address to address bus
			writeDataBus <- registers[signal.Src2] // Send data to data bus
		case "MOVE":
			registers[signal.Src1] = registers[signal.Src2] // Copy data from source to destination register
		case "ADD", "SUB", "MULT":
			result, err := ALU(signal.Command, registers[signal.Src1], registers[signal.Src2])
			if err != nil {
				fmt.Println("ALU result:", result)
			} else {
				registers[signal.Src1] = result // Write ALU result to destination register
			}
		default:
			fmt.Println("Unknown command:", signal.Command)
		}
		done <- true
	}
}

func ALU(op string, regA, regB int) (int, error) {
	switch op {
	case "ADD":
		return regA + regB, nil
	case "SUB":
		return regA - regB, nil
	case "MULT":
		return regA * regB, nil
	default:
		fmt.Println("Unknown Operation: ", op)
		return 0, fmt.Errorf("unknown operation: %s", op)
	}
}

func MemoryUnit() {
	for {
		address := <-addressBus
		select {
		case data := <-writeDataBus:
			// Write operation
			// fmt.Println("MemoryUnit: Writing data to address", address)
			dataMemory[address] = data
		case readDataBus <- dataMemory[address]:
			// Read operation
			// fmt.Println("MemoryUnit: Reading data from address", address)
		}
	}
}

func preLoadedInstructions() {
	instructionMemory := []ControlSignal{
		{"LOAD", 1, 10},    // LOAD R1, 10
		{"LOAD", 2, 11},    // LOAD R2, 11
		{"ADD", 1, 2},      // ADD R0 + R1
		{"STORE", 4, 1},    // STORE R1 -> Mem[4]
		{"LOADDISK", 3, 4}, // LOADDISK R3, Mem[4]
		{"MOVE", 4, 2},     // MOVE R4, R2
		{"MULT", 1, 2},     // MULT R1, R2
	}

	for pos := range instructionMemory {
		instr := instructionMemory[pos]
		controlBus <- instr
		<-done
	}

	fmt.Println("Preloaded Registers:", registers)
	fmt.Println("Preloaded Memory:", dataMemory[:20])
}
func IO(wg *sync.WaitGroup) {
	defer wg.Done()

	reader := bufio.NewReader(os.Stdin)
	fmt.Println("Enter instructions (e.g., LOAD 1 10, ADD 1 2, etc.)")
	for {
		fmt.Print("> ")
		input, _ := reader.ReadString('\n')
		input = strings.TrimSpace(input)
		if input == "EXIT" {
			break
		}

		parts := strings.Fields(input)
		if len(parts) < 3 {
			fmt.Println("Invalid instruction format. Expected: COMMAND SRC1 SRC2")
			continue
		}

		command := parts[0]
		src1, err1 := strconv.Atoi(parts[1])
		src2, err2 := strconv.Atoi(parts[2])
		if err1 != nil || err2 != nil {
			fmt.Println("Invalid arguments. SRC1 and SRC2 must be integers.")
			continue
		}

		instruction := ControlSignal{
			Command: command,
			Src1:    src1,
			Src2:    src2,
		}

		controlBus <- instruction
		<-done
		fmt.Println("Current Registers:", registers)
		fmt.Println("Current Memory:", dataMemory[:20])
	}
}

func main() {
	var wg sync.WaitGroup

	// Start CPU and MemoryUnit in separate goroutines
	go CPU()
	go MemoryUnit()

	// Start IO in a separate goroutine
	preLoadedInstructions()
	wg.Add(1)
	go IO(&wg)

	// Wait for IO to finish
	wg.Wait()

	// Output final state
	fmt.Println("Final Registers:", registers)
	fmt.Println("Final Memory:", dataMemory[:20])
}
