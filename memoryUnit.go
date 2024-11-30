package main

func memoryUnit() {
	for {
		address := <-safeAddressBus
		select {
		case data := <-writeDataBus:
			dataMemory[address] = data
			memoryDone <- true

		case readDataBus <- dataMemory[address]:
		}
	}
}
