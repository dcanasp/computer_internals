package main

import (
	"bufio"
	"context"
	"fmt"
	"os"
	"strconv"
	"strings"
	"sync"
	"time"
)

func preLoadedInstructions(ctx context.Context, wg *sync.WaitGroup, filePath string, useless int) {
	defer wg.Done()

	// Open the file only once, before starting the loop
	file, err := os.Open(filePath)
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer file.Close()

	// Read instructions from the file into memory
	var instructionMemory []int
	//
	for i := 0; i < useless; i++ {
		instructionMemory = append(instructionMemory, 0b00001000000000010000000000000000)
	}

	//
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
	if err := scanner.Err(); err != nil {
		fmt.Println("Error reading file:", err)
		return
	}

	// Process the instructions
	fmt.Println("Instructions:", instructionMemory)
	ticker := time.NewTicker(100 * time.Millisecond) // Check for context cancellation every 100ms
	defer ticker.Stop()
	for _, instr := range instructionMemory {
		select {
		case <-ctx.Done():
			// Stop the goroutine if context is canceled
			fmt.Println("Stopping Preloaded Instructions goroutine due to context cancellation")
			return
		case <-ticker.C:
			// Send instruction to memory and process
			addressBus <- programCounter
			writeDataBus <- instr
			// Wait for memory unit to finish writing
			select {
			case <-memoryDone:
			case <-ctx.Done():
				fmt.Println("Stopping Preloaded Instructions goroutine due to context cancellation (waiting for memory)")
				return
			}
			// Send signal to CPU to start processing
			controlBus <- 0
			// Wait for CPU to finish processing, allowing ctx to interrupt
			select {
			case <-cpuDone:
			case <-ctx.Done():
				fmt.Println("Stopping Preloaded Instructions goroutine due to context cancellation (waiting for CPU)")
				return
			}
			fmt.Println("Debug registers: ", registers[:9], "PC:", programCounter)

		}
	}

	// Print the preloaded registers and memory state
	fmt.Println("Preloaded Registers:", registers)
	fmt.Println("Preloaded Memory:", dataMemory[:20])
}

func printEachCycle(ctx context.Context) {
	for {
		select {
		case <-cpuDone:
			// Print the cycle information
			fmt.Println("Registers:", registers, "PC:", programCounter)
			fmt.Println("Memory:", dataMemory[:20])
			fmt.Print("> ")

		case <-ctx.Done():
			// Context was canceled, so stop the goroutine
			fmt.Println("Stopping Print Each Cycle goroutine")
			return
		}
	}
}

func showErrors(text string) {
	//usa ansi escape code para mostrar colores en la terminal
	const redColor = "\033[31m"
	const resetColor = "\033[0m"
	fmt.Printf("%sError: %s%s\n", redColor, text, resetColor)
}

func getInput(ctx context.Context, reader *bufio.Reader) (int, bool) {
	ticker := time.NewTicker(100 * time.Millisecond) // Check for context cancellation every 100ms
	defer ticker.Stop()

	for {
		select {
		case <-ctx.Done():
			// If the context is canceled, stop reading input
			fmt.Println("Input canceled due to context cancellation")
			return 0, true
		case <-ticker.C:
			// Every 100ms, check if the context is canceled, and also try reading input
			input, _ := reader.ReadString('\n')
			input = strings.TrimSpace(input)

			// Check for exit commands
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
}

func io(ctx context.Context, cancel context.CancelFunc, wg *sync.WaitGroup) {
	defer wg.Done()

	reader := bufio.NewReader(os.Stdin)
	fmt.Print("Enter 32-bit binary instructions or type EXIT:\n> ")
	for {
		binaryInstruction, exit := getInput(ctx, reader)
		if exit {
			cancel()
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
