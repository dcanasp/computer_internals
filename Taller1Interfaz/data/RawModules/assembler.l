%{
#include <stdio.h>
#include <stdlib.h>

extern FILE *yyin; // Archivo de entrada para Flex
%}

%%

[a-zA-Z]+   { printf("Assembler Output: Processed %s\n", yytext); }

%%

int main(int argc, char **argv) {
    if (argc > 1) {
        yyin = fopen(argv[1], "r");
        if (!yyin) {
            perror("Error opening file");
            return 1;
        }
    }

    yylex();

    if (yyin != stdin) {
        fclose(yyin);
    }

    return 0;
}
