full: assembler linker pc
faster: assembler linker 
	./pc/pc ./pcIN.txt
assembler:
	flex -o assembler/lex.yy.c assembler/assembler.l
	gcc assembler/lex.yy.c -o assembler/assembler
	./assembler/assembler ./assemblerIN.asm
linker:
	flex -o linkerLoader/lex.yy.c linkerLoader/linkerLoader.l
	gcc linkerLoader/lex.yy.c -o linkerLoader/linkerLoader
	./linkerLoader/linkerLoader ./linkerIN.txt 
pc:
	go build -C ./pc -o pc  .
	./pc/pc ./pcIN.txt
goBuild:
	go build -C ./pc -o pc  .

.PHONY: assembler pc full linker faster

