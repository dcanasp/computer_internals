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

func preLoadedInstructions(wg *sync.WaitGroup, filePath string) {
	defer wg.Done()

	// Open the file
	file, err := os.Open(filePath)
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer file.Close()

	// Read instructions from the file
	var instructionMemory []int
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		instruction, err := strconv.ParseInt(line, 2, 64) // Assuming instructions are in binary
		if err != nil {
			fmt.Println("Error parsing instruction:", err)
			continue
		}
		instructionMemory = append(instructionMemory, int(instruction))
	}
	fmt.Println("Instructions:", instructionMemory)

	if err := scanner.Err(); err != nil {
		fmt.Println("Error reading file:", err)
		return
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
		// fmt.Println("Registers:", registers, "PC:", programCounter)
		// fmt.Println("Memory:", dataMemory[:20])

	}

	fmt.Println("Preloaded Registers:", registers)
	fmt.Println("Preloaded Memory:", dataMemory[:20])
	time.Sleep(1 * time.Second) // Para que alcance a pintar a la pantalla

}

func printEachCycle() {
	for {
		<-cpuDone
		fmt.Println("Registers:", registers, "PC:", programCounter)
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
		binaryInstruction, err := strconv.ParseInt(input, 2, 64)
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
