package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
	"sync"
	"time"
)

func preLoadedInstructions(wg *sync.WaitGroup) {
	defer wg.Done()
	instructionMemory := []int{
		0b000000000000000000000000000, // BEGIN
		0b000010000000010000000001010, // LOAD R4, 10
		0b000010000000010100000001011, // LOAD R5, 11
		0b001010000000010000000000101, // ADD R4 + R5
		0b000100000000001000000000001, // STORE R1 -> Mem[2]
		0b001000000000011000000000010, // LOADDISK R6, Mem[2]
		0b000110000000011100000000100, // MOVE R7, R4
		0b001110000000010000000001011, // MULT R4, R5
		0b111110000000000000000000000, // END
	}

	for pos := range instructionMemory {
		instr := instructionMemory[pos]
		addressBus <- programCounter
		writeDataBus <- instr
		//waits for memory unit to finish writing it
		<-memoryDone
		// Send signal to CPU to start processing
		controlBus <- 0
		<-cpuDone

	}

	fmt.Println("Preloaded Registers:", registers)
	fmt.Println("Preloaded Memory:", dataMemory[:20])
	time.Sleep(1 * time.Second) // Para que alcance a pintar a la pantalla

}

func printEachCycle() {
	for {
		<-cpuDone
		fmt.Println("Registers:", registers)
		fmt.Println("Memory:", dataMemory[:20])
		fmt.Print("> ")
	}
}

func showErrors(text string) {
	//usa ansi escape code para mostrar colores en la terminal
	const redColor = "\033[31m"
	const resetColor = "\033[0m"
	fmt.Printf("%sError: %s%s\n", redColor, text, resetColor)
}

func getInput(reader *bufio.Reader) (int, bool) {
	for {
		input, _ := reader.ReadString('\n')
		input = strings.TrimSpace(input)
		if strings.ToLower(input) == "exit" || strings.ToLower(input) == "quit" {
			return 0, true
		}

		// Validate binary input
		if len(input) != 32 || strings.Trim(input, "01") != "" {
			fmt.Print("Invalid input. Please enter a 32-bit binary instruction.\n> ")
			continue
		}

		// Convert binary string to integer (for easier manipulation)
		binaryInstruction, err := strconv.ParseInt(input, 2, 32)
		if err != nil {
			fmt.Print("Error parsing binary input:\n> ", err)
			continue
		}

		return int(binaryInstruction), false
	}

}

func io(wg *sync.WaitGroup) {
	defer wg.Done()

	reader := bufio.NewReader(os.Stdin)
	fmt.Print("Enter 32-bit binary instructions or type EXIT:\n> ")
	for {
		binaryInstruction, exit := getInput(reader)
		if exit {
			break
		}

		// Send instruction to memory unit
		addressBus <- programCounter
		writeDataBus <- binaryInstruction
		//waits for memory unit to finish writing it
		<-memoryDone
		// fmt.Println("Waiting for memory unit to finish writing instruction")
		// Send signal to CPU to start processing
		controlBus <- 0
	}
}
