full: assembler pc
assembler:
	flex -o assembler/lex.yy.c assembler/assembler.l
	gcc assembler/lex.yy.c -o assembler/assembler
	./assembler/assembler ./assembler/input.txt
pc:
	go build -C ./pc -o pc  .
	./pc/pc ./pcIN.txt

.PHONY: assembler pc full

