# Computer Internals simulator in Go

This project simulates a von Neumann architecture computer, complete with a **CPU**, **memory**, **registers**, simple OS and a basic instruction set. The system is written in **Go** and is designed to mimic key aspects of a von Neumann architecture.

The goal of this project is to better understand the fundamentals of computer systems

# Features

- Custom binary language instruction set
- CPU that understands those instructions
- Memory and register management
- Simple OS
# Instruction Set

Here’s the complete list of supported instructions:

| Code  | Instruction | Input 1                  | Input 2                 |
| ----- | ----------- | ------------------------ | ----------------------- |
| 00000 | BEGIN       | N/A                      | N/A                     |
| 11111 | END         | N/A                      | N/A                     |
| 00001 | LOAD        | Destiny Register         | Const                   |
| 00010 | STORE       | Destiny Memory Direction | Register                |
| 00011 | MOVE        | Destiny Register         | Origin Register         |
| 00100 | LOADDISK    | Destiny Register         | Origin Memory Direction |
| 00101 | ADD         | Register 1               | Register 2              |
| 00110 | SUB         | Register 1               | Register 2              |
| 00111 | MULT        | Register 1               | Register 2              |
| 01000 | DIV         | Register 1               | Register 2              |
| 01001 | MOD         | Register 1               | Register 2              |
| 01010 | AND         | Register 1               | Register 2              |
| 01011 | OR          | Register 1               | Register 2              |
| 01100 | XOR         | Register 1               | Register 2              |
| 01101 | NOT         | Register 1               | Register 2              |
| 01110 | LEFSHIFT    | Register 1               | Bit ammount             |
| 01111 | RIGHTSHIF   | Register 1               | Bit ammount             |

# Usage
this is a simple **go** project. Just build and run.
```sh
go build -o simulator
./simulator
```
after that this is an example input
```sh
000000000000000000000000000
000010000000010000000001010
000010000000010100000001011
001010000000010000000000101
000100000000001000000000001
001000000000011000000000010
000110000000011100000000100
001110000000010000000001011
111110000000000000000000000
```

that returns this state:
```sh
Error: Invalid memory direction. You can't modify memory from a rutine.
Preloaded Registers: [0 0 0 0 0 11 4204555 21 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
Preloaded Memory: [0 4202506 4204555 20979717 8392705 16789506 12597252 29368331 130023424 0 0 0 0 0 0 0 0 0 0 0]
```