package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"
	"strconv"
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
	Command  int `json:"instruction"`
	Src1     int `json:"input1"`
	Src2     int `json:"input2"`
	SignSrc2 int `json:"sign"`
}
type iterationData struct {
	controlSignal
	PC        int   `json:"PC"`
	Registros []int `json:"registros"`
	Memoria   []int `json:"memoria"`
}

var iterations []iterationData

// var inputFile string = `C:\David\nacional\lenguajes\16\pcIN.txt`

func main() {
	ctx, cancel := context.WithCancel(context.Background())
	defer cancel() // Ensure cancellation when done
	fmt.Println("Starting PC")
	if len(os.Args) < 2 {
		fmt.Println("No hay archivo de entrada: ./pc <input_file>")
		return
	}

	useless := 0
	if len(os.Args) > 2 {
		var err error
		useless, err = strconv.Atoi(os.Args[2])
		if err != nil {
			useless = 0
		}
	}

	go cpu(ctx, cancel)
	go memoryUnit(ctx)
	go operativeSystem(ctx)

	inputFile := os.Args[1]
	var wg2 sync.WaitGroup
	wg2.Add(1)
	go preLoadedInstructions(ctx, &wg2, inputFile, useless)
	wg2.Wait()
	go printEachCycle(ctx)

	var wg sync.WaitGroup
	wg.Add(1)
	go io(ctx, cancel, &wg)
	wg.Wait()

	//open file
	jsonFile, err := os.OpenFile("./iterPc.json", os.O_CREATE|os.O_RDWR|os.O_TRUNC, 0644)

	if err != nil {
		panic(err)
	}
	defer jsonFile.Close()
	decoder := json.NewDecoder(jsonFile)
	_ = decoder.Decode(&iterations)

	jsonWritter(jsonFile, iterations)
	// Output final state
	fmt.Println("Final Registers:", registers)
	fmt.Println("Final Memory:", dataMemory[:100])
}
