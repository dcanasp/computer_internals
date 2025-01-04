package main

import (
	"fmt"
	"os"
	"sync"
)

var dataMemory = make([]int, 8192)

// var dataMemory = make([]int, 2048)
var registers = make([]int, 32)

var programCounter = 0

var controlBus = make(chan int)
var addressBus = make(chan int)
var safeAddressBus = make(chan int)
var readDataBus = make(chan int)
var writeDataBus = make(chan int)

var cpuDone = make(chan bool)
var memoryDone = make(chan bool)

type controlSignal struct {
	Command  int
	Src1     int
	Src2     int
	SignSrc2 int
}

// var inputFile string = `C:\David\nacional\lenguajes\16\pcIN.txt`

func main() {
	fmt.Println("Starting PC")
	if len(os.Args) < 2 {
		fmt.Println("No hay archivo de entrada: ./pc <input_file>")
		return
	}

	go cpu()
	go memoryUnit()
	go operativeSystem()

	inputFile := os.Args[1]
	var wg2 sync.WaitGroup
	wg2.Add(1)
	go preLoadedInstructions(&wg2, inputFile)
	wg2.Wait()
	go printEachCycle()

	var wg sync.WaitGroup
	wg.Add(1)
	go io(&wg)
	wg.Wait()

	// Output final state
	fmt.Println("Final Registers:", registers)
	fmt.Println("Final Memory:", dataMemory[:100])
}
