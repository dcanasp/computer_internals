package main

import (
	"context"
	"fmt"
)

func operativeSystem(ctx context.Context) {
	for {
		select {
		case address := <-addressBus:
			// Perform memory operations as usual
			select {
			case data := <-writeDataBus:
				if (address > registers[1]) && (address < registers[2]) {
					showErrors("Error: Dirección de memoria inválida. No puedes modificar memoria que es parte de una rutina.")
					memoryDone <- false
				} else {
					safeAddressBus <- address
					writeDataBus <- data
				}
			default:
				safeAddressBus <- address
			}

		case <-ctx.Done():
			// Context was canceled, so stop the goroutine
			fmt.Println("Stopping Operative System goroutine")
			return
		}
	}

}

func validateRegisterAccess(registerIndex int) bool {
	if registerIndex >= 0 && registerIndex <= 3 {
		showErrors(fmt.Sprintf("Error: El registro R%d está reservado y no puede ser modificado por esta instrucción.", registerIndex))
		return false
	}
	return true
}
