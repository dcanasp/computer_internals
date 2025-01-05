%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MAX_LABELS 100
#define MAX_INSTRUCTIONS 1000
#define MAX_LINE_LENGTH 100

typedef struct {
    char name[50];
    int address;
    int first_jump_location;  // Ubicación del primer salto a esta etiqueta
} Label;

Label labels[MAX_LABELS];
int label_count = 0;
char instructions[MAX_INSTRUCTIONS][MAX_LINE_LENGTH];
int instruction_count = 0;

// Función mejorada para encontrar la dirección de una etiqueta
int get_label_address(const char *name) {
    char clean_name[50];
    strncpy(clean_name, name, sizeof(clean_name) - 1);
    clean_name[sizeof(clean_name) - 1] = '\0';
    
    char *colon = strchr(clean_name, ':');
    if (colon) *colon = '\0';

    for (int i = 0; i < label_count; i++) {
        if (strcmp(labels[i].name, clean_name) == 0) {
            return labels[i].address;
        }
    }
    return -1;
}

// Función para encontrar una etiqueta por nombre
Label* find_label(const char *name) {
    for (int i = 0; i < label_count; i++) {
        if (strcmp(labels[i].name, name) == 0) {
            return &labels[i];
        }
    }
    return NULL;
}

// Función mejorada para resolver las referencias a etiquetas
void resolve_labels() {
    for (int i = 0; i < instruction_count; i++) {
        char line[MAX_LINE_LENGTH];
        char opcode[20], arg1[20], arg2[20];
        strcpy(line, instructions[i]);
        
        int args = sscanf(line, "%s %s %s", opcode, arg1, arg2);
        
        if (args >= 2) {
            if (strcmp(opcode, "JNE") == 0) {
                Label* label = find_label(arg1);
                if (label != NULL) {
                    // Si es la primera vez que vemos este salto, guardamos su ubicación
                    if (label->first_jump_location == -1) {
                        label->first_jump_location = i;
                        sprintf(instructions[i], "JNE %d", label->address);
                    } else {
                        // Si es un salto desde dentro del bucle, agregamos un JUMP adicional
                        sprintf(instructions[i], "JNE %d", label->address);
                        
                        // Agregar un JUMP a la instrucción después del primer JNE
                        // Desplazamos todas las instrucciones una posición
                        for (int j = instruction_count; j > i + 1; j--) {
                            strcpy(instructions[j], instructions[j-1]);
                        }
                        // Insertamos el JUMP
                        sprintf(instructions[i + 1], "JUMP %d", label->first_jump_location);
                        instruction_count++;
                        i++; // Saltamos la instrucción que acabamos de insertar
                    }
                }
            } else if (strcmp(opcode, "JUMP") == 0 || strcmp(opcode, "JEQ") == 0) {
                int addr = get_label_address(arg1);
                if (addr != -1) {
                    sprintf(instructions[i], "%s %d", opcode, addr);
                }
            }
        }
    }
}

%}

%option noyywrap

LABEL       [A-Za-z_][A-Za-z0-9_]*
NUMBER      [0-9]+
WHITESPACE  [ \t]+

%%

^{LABEL}:   {
    char *label = strdup(yytext);
    label[strlen(label)-1] = '\0';
    strncpy(labels[label_count].name, label, sizeof(labels[label_count].name) - 1);
    labels[label_count].name[sizeof(labels[label_count].name) - 1] = '\0';
    labels[label_count].address = instruction_count -1;
    labels[label_count].first_jump_location = -1;  // Inicializamos en -1
    label_count++;
    free(label);
}

^(LOAD|ADD|SUB|MUL|DIV|CMP|MOVE){WHITESPACE}{NUMBER}{WHITESPACE}{NUMBER} {
    strncpy(instructions[instruction_count], yytext, sizeof(instructions[instruction_count]) - 1);
    instructions[instruction_count][sizeof(instructions[instruction_count]) - 1] = '\0';
    instruction_count++;
}

^(JUMP|JEQ|JNE){WHITESPACE}{LABEL} {
    strncpy(instructions[instruction_count], yytext, sizeof(instructions[instruction_count]) - 1);
    instructions[instruction_count][sizeof(instructions[instruction_count]) - 1] = '\0';
    instruction_count++;
}

^(BEGIN|END|FIN) {
    strncpy(instructions[instruction_count], yytext, sizeof(instructions[instruction_count]) - 1);
    instructions[instruction_count][sizeof(instructions[instruction_count]) - 1] = '\0';
    instruction_count++;
}

^[\t ]+ ;
\n      ;
.       ;

%%

int main(int argc, char **argv) {
    if (argc != 2) {
        fprintf(stderr, "Uso: %s <archivo_entrada>\n", argv[0]);
        return 1;
    }

    FILE *file = fopen(argv[1], "r");
    if (!file) {
        perror("Error al abrir el archivo");
        return 1;
    }

    yyin = file;
    yylex();
    fclose(file);

    resolve_labels();

    FILE *output_file = fopen("assemblerIN.asm", "w");
    if (!output_file) {
        perror("Error al crear el archivo de salida");
        return 1;
    }

    for (int i = 0; i < instruction_count; i++) {
        fprintf(output_file, "%s\n", instructions[i]);
    }

    fclose(output_file);
    return 0;
}