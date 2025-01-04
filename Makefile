full: linker assembler pc
assembler:
	flex -o assembler/lex.yy.c assembler/assembler.l
	gcc assembler/lex.yy.c -o assembler/assembler
	./assembler/assembler ./assemblerIN.asm
pc:
	go build -C ./pc -o pc  .
	./pc/pc ./pcIN.txt
linker:
	flex -o linkerLoader/lex.yy.c linkerLoader/linkerLoader.l
	gcc linkerLoader/lex.yy.c -o linkerLoader/linkerLoader
	./linkerLoader/linkerLoader ./linkerLoader/linkerIN.txt
go:
	go run -C ./pc .

.PHONY: assembler pc full linker go

