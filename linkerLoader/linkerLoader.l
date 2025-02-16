%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MAX_LABELS 100
#define MAX_INSTRUCTIONS 8192
#define MAX_LINE_LENGTH 100

// Códigos de error
#define ERROR_OVERFLOW_INSTRUCCIONES 1
#define ERROR_OVERFLOW_ETIQUETAS 2
#define ERROR_ARCHIVO_ENTRADA 3
#define ERROR_ARCHIVO_SALIDA 4

typedef struct {
    char name[50];
    int start_address;         
    int end_address;          
    int return_address;       
    int is_term_marker;        
} Label;
int InitialJumps = 0;

Label labels[MAX_LABELS];
int label_count = 0;
char instructions[MAX_INSTRUCTIONS][MAX_LINE_LENGTH];
int instruction_count = 0;

Label* find_label(const char* name) {
    for (int j = 0; j < label_count; j++) {
        if (strcmp(labels[j].name, name) == 0) {
            return &labels[j];
        }
    }
    return NULL;
}

char *strrchr_last(const char *str, int c) {
    char *last_occurrence = NULL;

    while (*str) {
        if (*str == (char)c) {
            last_occurrence = (char *)str;
        }
        str++;
    }

    return last_occurrence;
}

void resolve_labels() {
    printf("Initial instruction count: %d\n", instruction_count);
    printf("Initial instructions:\n");
    for (int i = 0; i < instruction_count; i++) {
        printf("[%d]: '%s'\n", i, instructions[i]);
    }
    for (int i = 0; i < instruction_count; i++) {
        if (strlen(instructions[i]) != 32) {
            // Check for any of the three jump types
            if (strncmp(instructions[i], "10010", 5) == 0 || // JUMP
                strncmp(instructions[i], "10011", 5) == 0 || // JEQ
                strncmp(instructions[i], "10100", 5) == 0) { // JNE
                
                char* start = strchr(instructions[i], '8');
                char* end = strrchr_last(instructions[i], '8');
                
                if (start && end && start < end) {
                    char label_name[50] = {0};
                    int label_len = end - (start + 1);
                    if (label_len < 50) {
                        strncpy(label_name, start + 1, label_len);
                        label_name[label_len] = '\0';

                        char jump_type[6] = {0};
                        strncpy(jump_type, instructions[i], 5);
                        jump_type[5] = '\0';

                        Label* label = find_label(label_name);
                        //aca va el numero de la label y ya
                        char binary_address[14] = {0};
                        // Fill with zeros first
                        memset(binary_address, '0', 13);
                        
                        // Convert address to binary (target address - 1)
                        int address = label->start_address - 1;
                        for (int j = 12; j >= 0 && address > 0; j--) {
                            binary_address[j] = '0' + (address & 1);
                            address >>= 1;
                        }

                        // Create the complete jump instruction
                        char new_instruction[33] = {0};
                        char relleno_1[15] = "00000000000000";
                        strcpy(new_instruction, jump_type);
                        strcat(new_instruction, binary_address);
                        strcat(new_instruction, relleno_1);
                        
                        strcpy(instructions[i], new_instruction);
                    }
                }
            }
        }
    }

    printf("Final instructions:\n");
    for (int i = 0; i < instruction_count; i++) {
        printf("[%d]: '%s'\n", i, instructions[i]);
    }
}
%}

%option noyywrap

BINARY      [01]{32}
JUMP_MARKER [01]{5}8[A-Za-z_][A-Za-z0-9_]*8[01]*
LABEL       [A-Za-z_][A-Za-z0-9_]*

%%

{BINARY} {
    if (instruction_count >= MAX_INSTRUCTIONS) {
        fprintf(stderr, "%d\n", ERROR_OVERFLOW_INSTRUCCIONES);  // Código de error
        exit(ERROR_OVERFLOW_INSTRUCCIONES);  // Terminar ejecución con código de error
    }
    strncpy(instructions[instruction_count], yytext, sizeof(instructions[instruction_count]) - 1);
    instructions[instruction_count][sizeof(instructions[instruction_count]) - 1] = '\0';
    instruction_count++;
}

{JUMP_MARKER} {
    if (instruction_count >= MAX_INSTRUCTIONS) {
        fprintf(stderr, "%d\n", ERROR_OVERFLOW_INSTRUCCIONES);  // Código de error
        exit(ERROR_OVERFLOW_INSTRUCCIONES);  // Terminar ejecución con código de error
    }
    strncpy(instructions[instruction_count], yytext, sizeof(instructions[instruction_count]) - 1);
    instructions[instruction_count][sizeof(instructions[instruction_count]) - 1] = '\0';
    instruction_count++;
}

^{LABEL}:   {
    if (label_count >= MAX_LABELS) {
        fprintf(stderr, "%d\n", ERROR_OVERFLOW_ETIQUETAS);  // Código de error
        exit(ERROR_OVERFLOW_ETIQUETAS);  // Terminar ejecución con código de error
    }
    char *label = strdup(yytext);
    label[strlen(label)-1] = '\0';  // Remove colon
    strncpy(labels[label_count].name, label, sizeof(labels[label_count].name) - 1);
    labels[label_count].name[sizeof(labels[label_count].name) - 1] = '\0';
    labels[label_count].start_address = instruction_count;
    labels[label_count].end_address = -1;
    labels[label_count].return_address = -1;
    labels[label_count].is_term_marker = 0;
    label_count++;
    free(label);
}

^[\t ]+ ;
\n      ;
.       ;

%%

int main(int argc, char **argv) {
    if (argc != 4) {  // Ahora espera 3 argumentos
        fprintf(stderr, "Uso: %s <entrada> <salida> <offset>\n", argv[0]);
        return 1;
    }
    
    FILE *file = fopen(argv[1], "r"); // Archivo entrada (absoluto)
    if (!file) {
        fprintf(stderr, "%d\n", ERROR_ARCHIVO_ENTRADA);  // Código de error
        return ERROR_ARCHIVO_ENTRADA;
    }

    if (argv[3] != NULL) {
        InitialJumps = atoi(argv[3]);
    }

    for (int i = 0; i < InitialJumps; i++) {
        if (instruction_count >= MAX_INSTRUCTIONS) {
            fprintf(stderr, "%d\n", ERROR_OVERFLOW_INSTRUCCIONES);  // Código de error
            fclose(file);
            return ERROR_OVERFLOW_INSTRUCCIONES;
        }
        instruction_count++;
    }

    yyin = file;
    yylex();
    fclose(file);
    resolve_labels();

    FILE *output_file = fopen(argv[2], "w"); // Archivo salida (absoluto)
    if (!output_file) {
        fprintf(stderr, "%d\n", ERROR_ARCHIVO_SALIDA);  // Código de error
        return ERROR_ARCHIVO_SALIDA;
    }

    for (int i = 0; i < instruction_count; i++) {
        if (instructions[i][0] == '\0') continue;
        fprintf(output_file, "%s\n", instructions[i]);
    }

    fclose(output_file);
    return 0;
}