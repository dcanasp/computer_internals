%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MAX_LINE_LENGTH 100

FILE *output_file;

// Function to convert an integer to a binary string
void int_to_binary(int num, int bits, char *output) {
    for (int i = bits - 1; i >= 0; i--) {
        output[bits - 1 - i] = (num & (1 << i)) ? '1' : '0';
    }
    output[bits] = '\0';
}

%}

%option noyywrap

NUMBER      [0-9]+
WHITESPACE  [ \t]+
INSTRUCCION [A-Za-z]+
SIGN_NUMBER [-+]?{NUMBER}
LABEL       [A-Za-z_][A-Za-z0-9_]*

%%

^(BEGIN|END|FIN) {
    const char *output;
    if (strcmp(yytext, "BEGIN") == 0) {
        output = "00000000000000000000000000000000\n";
    } else if (strcmp(yytext, "END") == 0) {
        output = "11111000000000000000000000000000\n";
    } else if (strcmp(yytext, "FIN") == 0) {
        output = "11110000000000000000000000000000\n";
    }
    fprintf(output_file, "%s", output);
}

^(LOAD|CMP|CMPG|CMPL|CMPGE|CMPLE){WHITESPACE}{NUMBER}{WHITESPACE}{SIGN_NUMBER} {
    char instruction[20];
    int reg, value, sign, opcode;
    char reg_bin[14], value_bin[14], sign_bin[2];
    
    sscanf(yytext, "%s %d %d", instruction, &reg, &value);
    sign = (value < 0) ? 1 : 0;
    value = abs(value);

    int_to_binary(reg, 13, reg_bin);
    int_to_binary(value, 13, value_bin);
    int_to_binary(sign, 1, sign_bin);

    char output[34];
    if (strcmp(instruction, "LOAD") == 0) opcode = 1;
    else if (strcmp(instruction, "CMP") == 0) opcode = 16;
    else if (strcmp(instruction, "CMPG") == 0) opcode = 21;
    else if (strcmp(instruction, "CMPL") == 0) opcode = 22;
    else if (strcmp(instruction, "CMPGE") == 0) opcode = 23;
    else if (strcmp(instruction, "CMPLE") == 0) opcode = 24;

    char opcode_bin[6];

    int_to_binary(opcode, 5, opcode_bin);
    sprintf(output, "%s%s%s%s\n", opcode_bin, reg_bin, sign_bin, value_bin);

    fprintf(output_file, "%s", output);
}

^{INSTRUCCION}{WHITESPACE}{NUMBER}{WHITESPACE}{NUMBER} {
    char instruction[20];
    int reg1, reg2, opcode;
    char reg1_bin[14], reg2_bin[14];

    sscanf(yytext, "%s %d %d", instruction, &reg1, &reg2);
    
    // Opcode mapping
    if (strcmp(instruction, "STORE") == 0) opcode = 2;
    else if (strcmp(instruction, "MOVE") == 0) opcode = 3;
    else if (strcmp(instruction, "LOADDISK") == 0) opcode = 4;
    else if (strcmp(instruction, "ADD") == 0) opcode = 5;
    else if (strcmp(instruction, "SUB") == 0) opcode = 6;
    else if (strcmp(instruction, "MULT") == 0) opcode = 7;
    else if (strcmp(instruction, "DIV") == 0) opcode = 8;
    else if (strcmp(instruction, "MOD") == 0) opcode = 9;
    else if (strcmp(instruction, "AND") == 0) opcode = 10;
    else if (strcmp(instruction, "OR") == 0) opcode = 11;
    else if (strcmp(instruction, "XOR") == 0) opcode = 12;
    else if (strcmp(instruction, "STOREREG") == 0) opcode = 13;
    else if (strcmp(instruction, "LEFSHIFT") == 0) opcode = 14;
    else if (strcmp(instruction, "RIGHTSHIF") == 0) opcode = 15;
    else if (strcmp(instruction, "CMPREG") == 0) opcode = 17;
    else if (strcmp(instruction, "CMPGREG") == 0) opcode = 25;
    else if (strcmp(instruction, "CMPLREG") == 0) opcode = 26;
    else if (strcmp(instruction, "CMPGEREG") == 0) opcode = 27;
    else if (strcmp(instruction, "CMPLEREG") == 0) opcode = 28;
    else if (strcmp(instruction, "LOADDISKREG") == 0) opcode = 29;

    int_to_binary(reg1, 13, reg1_bin);
    int_to_binary(reg2, 13, reg2_bin);

    char opcode_bin[6];
    int_to_binary(opcode, 5, opcode_bin);

    char output[34];
    sprintf(output, "%s%s0%s\n", opcode_bin, reg1_bin, reg2_bin);
    fprintf(output_file, "%s", output);
}


^(JUMP|JEQ|JNE){WHITESPACE}{LABEL} {
    char instruction[6];
    int opcode;
    char label[80];
    sscanf(yytext, "%5s %79s", instruction, label);
    
    if (strcmp(instruction, "JUMP") == 0) opcode = 18;
    else if (strcmp(instruction, "JEQ") == 0) opcode = 19;    
    else if (strcmp(instruction, "JNE") == 0) opcode = 20;

    char opcode_bin[6];
    int_to_binary(opcode, 5, opcode_bin);
    char output[150];
    snprintf(output, sizeof(output), "%s8%s800000000000000\n", opcode_bin, label);
    fprintf(output_file, "%s", output);
}
^{LABEL}: {
    char instruction[80];  // Reduced from 100 since original warning suggested it was too large
    char output[100];
    sscanf(yytext, "%79s", instruction);  // Added length limit
    snprintf(output, sizeof(output), "%s\n", instruction);
    fprintf(output_file, "%s", output);
}

^[\t ]+ ;    // Ignore leading whitespace
\n      ;    // Ignore newlines
.       {
    fprintf(stderr, "Unrecognized input: %s\n", yytext);
}

%%

int main(int argc, char **argv) {
    if (argc != 3) {
        fprintf(stderr, "Usage: %s <input_file> <output_file>\n", argv[0]);
        return 1;
    }

    FILE *input_file = fopen(argv[1], "r");
    if (!input_file) {
        perror("Error opening input file");
        return 1;
    }

    output_file = fopen(argv[2], "w");
    if (!output_file) {
        perror("Error creating output file");
        fclose(input_file);
        return 1;
    }

    yyin = input_file;
    yylex();

    fclose(input_file);
    fclose(output_file);
    return 0;
}