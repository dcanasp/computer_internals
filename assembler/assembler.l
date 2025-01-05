%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Global file pointer for output
FILE *output_file;

// Function to convert an integer to a binary string
void int_to_binary(int num, int bits, char *output) {
    for (int i = bits - 1; i >= 0; i--) {
        output[bits - 1 - i] = (num & (1 << i)) ? '1' : '0';
    }
    output[bits] = '\0'; // Null-terminate the string
}
%}

%option noyywrap

REGISTER    [0-9]+
REGISTERS   [ \t]+{REGISTER}[ \t]+{REGISTER}
SIGNED      -?[0-9]+
REG_SIGNED [ \t]+{REGISTER}[ \t]+{SIGNED}
SINGLE      [ \t]+{REGISTER}
%%

[ \t]+              ; // Ignore spaces and tabs
\n                  ; // Ignore newlines

(BEGIN|END|FIN) {
    const char *output;
    if (strcmp(yytext, "BEGIN") == 0) {
        output = "00000000000000000000000000000000\n";
    } else if (strcmp(yytext, "END") == 0) {
        output = "11111000000000000000000000000000\n";
    } else if (strcmp(yytext, "FIN") == 0) {
        output = "11110000000000000000000000000000\n";
    }

    printf("%s", output);
    fprintf(output_file, "%s", output);
}
(LOAD|CMP){REG_SIGNED} {
    int reg, value, sign;
    char reg_bin[14], value_bin[14], sign_bin[2];
    char opcode[6];

    sscanf(yytext, "%s %d %d", opcode, &reg, &value);
    sign = (value < 0) ? 1 : 0;
    value = abs(value);

    int_to_binary(reg, 13, reg_bin);
    int_to_binary(value, 13, value_bin);
    int_to_binary(sign, 1, sign_bin);

    char output[34];
    if (strcmp(opcode, "LOAD") == 0) {
        sprintf(output, "00001%s%s%s\n", reg_bin, sign_bin, value_bin);
    } else if (strcmp(opcode, "CMP") == 0) {
        sprintf(output, "10000%s%s%s\n", reg_bin, sign_bin, value_bin);
    }

    printf("%s", output);
    fprintf(output_file, "%s", output);
}

(STORE|MOVE|LOADDISK|ADD|SUB|MULT|DIV|MOD|AND|OR|XOR|CMPREG|LEFSHIFT|RIGHTSHIF){REGISTERS} {
    char op[10];
    int reg1, reg2, opcode;
    char reg1_bin[14], reg2_bin[14];

    sscanf(yytext, "%s %d %d", op, &reg1, &reg2);
    if (strcmp(op, "STORE") == 0) opcode = 2;
    else if (strcmp(op, "MOVE") == 0) opcode = 3;
    else if (strcmp(op, "LOADDISK") == 0) opcode = 4;
    else if (strcmp(op, "ADD") == 0) opcode = 5;
    else if (strcmp(op, "SUB") == 0) opcode = 6;
    else if (strcmp(op, "MULT") == 0) opcode = 7;
    else if (strcmp(op, "DIV") == 0) opcode = 8;
    else if (strcmp(op, "MOD") == 0) opcode = 9;
    else if (strcmp(op, "AND") == 0) opcode = 10;
    else if (strcmp(op, "OR") == 0) opcode = 11;
    else if (strcmp(op, "XOR") == 0) opcode = 12;
    else if (strcmp(op, "LEFSHIFT") == 0) opcode = 14;
    else if (strcmp(op, "RIGHTSHIF") == 0) opcode = 15;
    else if (strcmp(op, "CMPREG") == 0) opcode = 17;

    int_to_binary(reg1, 13, reg1_bin);
    int_to_binary(reg2, 13, reg2_bin);

    char opcode_bin[6];
    int_to_binary(opcode, 5, opcode_bin);

    char output[34];
    sprintf(output, "%s%s0%s\n", opcode_bin, reg1_bin, reg2_bin);
    printf("%s", output);
    fprintf(output_file, "%s", output);
}

(JUMP|JEQ|JNE|NOT){SINGLE} {
    char op[10];
    int reg,opcode;
    char reg_bin[14];

    sscanf(yytext, "%s %d", op,&reg);
    int_to_binary(reg, 13, reg_bin);

    if (strcmp(op, "NOT") == 0) opcode = 13;
    else if (strcmp(op, "JUMP") == 0) opcode = 18;
    else if (strcmp(op, "JEQ") == 0) opcode = 19;
    else if (strcmp(op, "JNE") == 0) opcode = 20;

    char opcode_bin[6];
    int_to_binary(opcode, 5, opcode_bin);

    char output[34];
    sprintf(output, "%s%s00000000000000\n", opcode_bin,reg_bin);
    printf("%s", output);
    fprintf(output_file, "%s", output);
}


.|\n { fprintf(stderr, "Unrecognized input: %s\n", yytext); }

%%

int main(int argc, char **argv) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <input_file>\n", argv[0]);
        return 1;
    }

    FILE *file = fopen(argv[1], "r");
    if (!file) {
        perror("Error opening file");
        return 1;
    }

    output_file = fopen("pcIN.txt", "w");
    if (!output_file) {
        perror("Error creating output file");
        fclose(file);
        return 1;
    }

    yyin = file;
    yylex();

    fclose(file);
    fclose(output_file);

    return 0;
}
