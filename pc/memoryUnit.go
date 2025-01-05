package main

import (
	"context"
	"fmt"
)

func memoryUnit(ctx context.Context) {
	for {
		select {
		case address := <-safeAddressBus:
			select {
			case data := <-writeDataBus:
				dataMemory[address] = data
				memoryDone <- true

			case readDataBus <- dataMemory[address]:
			}

		case <-ctx.Done():
			// Context was canceled, so stop the goroutine
			fmt.Println("Stopping Memory Unit goroutine")
			return
		}
	}
}
