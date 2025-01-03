# Computer Internals simulator in Go

This project simulates the internals of a compiler and a von Neumann architecture computer, complete with a **CPU**, **memory**, **ASSEMBLER**, **LEXICAL PARSER** among others. The system is written in **Go** and **flex**

The goal of this project is to better understand the fundamentals of computer systems

# Features

- Custom binary language instruction set
- CPU that understands those instructions
- Memory and register management
- Custom assembler for it
- Lexical parser


# Usage
Assuming you have both flex, go, and an initial input on a .txt file. Just run the makefile
```sh
make
```

To avoid some unwanted warning. The input.txt file must end on **LR** instead of *CRLF*


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
