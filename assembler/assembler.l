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
INSTRUCTION [A-Za-z]+
SIGN_NUMBER [-+]?{NUMBER}
LABEL       [A-Za-z_][A-Za-z0-9_]*
TERM_LABEL  TERM_{LABEL}

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

^(LOAD|CMP){WHITESPACE}{NUMBER}{WHITESPACE}{SIGN_NUMBER} {
    char instruction[20];
    int reg, value, sign;
    char reg_bin[14], value_bin[14], sign_bin[2];
    
    sscanf(yytext, "%s %d %d", instruction, &reg, &value);
    sign = (value < 0) ? 1 : 0;
    value = abs(value);

    int_to_binary(reg, 13, reg_bin);
    int_to_binary(value, 13, value_bin);
    int_to_binary(sign, 1, sign_bin);

    char output[34];
    if (strcmp(instruction, "LOAD") == 0) {
        sprintf(output, "00001%s%s%s\n", reg_bin, sign_bin, value_bin);
    } else if (strcmp(instruction, "CMP") == 0) {
        sprintf(output, "10000%s%s%s\n", reg_bin, sign_bin, value_bin);
    }

    fprintf(output_file, "%s", output);
}

^(STORE|MOVE|LOADDISK|ADD|SUB|MULT|DIV|MOD|AND|OR|XOR|CMPREG|LEFSHIFT|RIGHTSHIF){WHITESPACE}{NUMBER}{WHITESPACE}{NUMBER} {
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
    else if (strcmp(instruction, "LEFSHIFT") == 0) opcode = 14;
    else if (strcmp(instruction, "RIGHTSHIF") == 0) opcode = 15;
    else if (strcmp(instruction, "CMPREG") == 0) opcode = 17;

    int_to_binary(reg1, 13, reg1_bin);
    int_to_binary(reg2, 13, reg2_bin);

    char opcode_bin[6];
    int_to_binary(opcode, 5, opcode_bin);

    char output[34];
    sprintf(output, "%s%s0%s\n", opcode_bin, reg1_bin, reg2_bin);
    fprintf(output_file, "%s", output);
}

^NOT{WHITESPACE}{NUMBER} {
    char instruction[20];
    int reg, opcode;
    char reg_bin[14];

    sscanf(yytext, "%s %d", instruction, &reg);
    
    if (strcmp(instruction, "NOT") == 0) opcode = 13;

    int_to_binary(reg, 13, reg_bin);
    
    char opcode_bin[6];
    int_to_binary(opcode, 5, opcode_bin);
    
    char output[35];
    sprintf(output, "%s%s00000000000000\n", opcode_bin, reg_bin);
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
    snprintf(output, sizeof(output), "%s8%s900000000000000\n", opcode_bin, label);
    fprintf(output_file, "%s", output);
}
^{LABEL}: {
    char instruction[80];  // Reduced from 100 since original warning suggested it was too large
    char output[100];
    sscanf(yytext, "%79s", instruction);  // Added length limit
    snprintf(output, sizeof(output), "%s\n", instruction);
    fprintf(output_file, "%s", output);

}
^{TERM_LABEL} {
    char instruction[80];  // Reduced from 100
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
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <input_file>\n", argv[0]);
        return 1;
    }

    FILE *input_file = fopen(argv[1], "r");
    if (!input_file) {
        perror("Error opening input file");
        return 1;
    }

    output_file = fopen("linkerIN.txt", "w");
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