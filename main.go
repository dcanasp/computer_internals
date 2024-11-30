package main

import (
	"fmt"
	"sync"
)

var dataMemory = make([]int, 2048)
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
	Command int
	Src1    int
	Src2    int
}

func main() {
	var wg sync.WaitGroup

	// Start CPU and MemoryUnit in separate goroutines
	go cpu()
	go memoryUnit()
	go operativeSystem()

	var wg2 sync.WaitGroup
	wg2.Add(1)
	go preLoadedInstructions(&wg2)
	wg2.Wait()
	go printEachCycle()
	// Start IO in a separate goroutine
	wg.Add(1)
	go io(&wg)
	// Wait for IO to finish
	wg.Wait()

	// Output final state
	fmt.Println("Final Registers:", registers)
	fmt.Println("Final Memory:", dataMemory[:20])
}
