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
    int start_address;         
    int end_address;          
    int return_address;       
    int is_term_marker;        // Changed from is_end_marker to is_term_marker
} Label;

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

void process_term_label(const char* term_marker) {
    char label_name[50];
    strcpy(label_name, term_marker + 5);  // Skip "TERM_"
    
    Label* label = find_label(label_name);
    if (label != NULL) {
        label->end_address = instruction_count - 1;
        label->is_term_marker = 1;
    }
}

void insert_instruction(int position, const char* instruction) {
    for (int i = instruction_count; i > position; i--) {
        strcpy(instructions[i], instructions[i-1]);
    }
    strcpy(instructions[position], instruction);
    instruction_count++;
    
    // Update label addresses
    for (int i = 0; i < label_count; i++) {
        if (labels[i].start_address > position) {
            labels[i].start_address++;
        }
        if (labels[i].end_address >= position) {
            labels[i].end_address++;
        }
    }
}

void resolve_labels() {
    // First pass: Insert all return jumps to calculate final instruction count
    int total_jumps_to_insert = 0;
    for (int i = 0; i < instruction_count; i++) {
        char line[MAX_LINE_LENGTH];
        char opcode[20], arg1[20], arg2[20];
        strcpy(line, instructions[i]);
        
        int args = sscanf(line, "%s %s %s", opcode, arg1, arg2);
        
        if (args >= 2 && strcmp(opcode, "JUMP") == 0) {
            Label* label = find_label(arg1);
            if (label != NULL) {
                total_jumps_to_insert++;
            }
        }
    }
    
    // Pre-allocate space for all return jumps
    for (int i = 0; i < total_jumps_to_insert; i++) {
        strcpy(instructions[instruction_count + i], "JUMP 0");  // Temporary placeholder
    }
    instruction_count += total_jumps_to_insert;
    
    // Second pass: Process all jump instructions and update addresses
    int inserted_jumps = 0;
    for (int i = 0; i < instruction_count - total_jumps_to_insert; i++) {
        char line[MAX_LINE_LENGTH];
        char opcode[20], arg1[20], arg2[20];
        strcpy(line, instructions[i]);
        
        int args = sscanf(line, "%s %s %s", opcode, arg1, arg2);
        
        if (args >= 2) {
            Label* label = find_label(arg1);
            
            if (label != NULL) {
                if (strcmp(opcode, "JUMP") == 0) {
                    // Calculate target address (decremented by 1)
                    int target = label->start_address - 1;
                    
                    // Update jump instruction
                    sprintf(instructions[i], "JUMP %d", target);
                    
                    // Calculate return position
                    int return_pos = label->end_address + inserted_jumps;
                    
                    // Calculate return target (decremented by 1)
                    int return_target = i + 1;
                    
                    // Move instructions between label end and next label start
                    for (int j = instruction_count - 1; j > return_pos; j--) {
                        strcpy(instructions[j], instructions[j-1]);
                    }
                    
                    // Insert return jump
                    sprintf(instructions[return_pos], "JUMP %d", return_target - 1);
                    inserted_jumps++;
                }
                else if (strcmp(opcode, "JEQ") == 0 || strcmp(opcode, "JNE") == 0) {
                    // Update conditional jump target (decremented by 1)
                    int target = label->start_address - 1;
                    sprintf(instructions[i], "%s %d", opcode, target);
                }
            }
        }
    }
    
    // Remove TERM_ markers from final output
    int write_pos = 0;
    for (int read_pos = 0; read_pos < instruction_count; read_pos++) {
        if (strncmp(instructions[read_pos], "TERM_", 5) != 0) {
            if (write_pos != read_pos) {
                strcpy(instructions[write_pos], instructions[read_pos]);
            }
            write_pos++;
        }
    }
    instruction_count = write_pos;
}
%}

%option noyywrap

LABEL       [A-Za-z_][A-Za-z0-9_]*
NUMBER      [0-9]+
WHITESPACE  [ \t]+
INSTRUCTION [A-Za-z]+
SIGN_NUMBER [-+]?{NUMBER}
TERM_LABEL  TERM_{LABEL}

%%

^{LABEL}:   {
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

^{TERM_LABEL} {
    process_term_label(yytext);
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

^{INSTRUCTION}{WHITESPACE}{NUMBER} {
    strncpy(instructions[instruction_count], yytext, sizeof(instructions[instruction_count]) - 1);
    instructions[instruction_count][sizeof(instructions[instruction_count]) - 1] = '\0';
    instruction_count++;
}

^{INSTRUCTION}{WHITESPACE}{NUMBER}{WHITESPACE}{SIGN_NUMBER} {
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