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
    int is_term_marker;        
} Label;
int InitialJumps=0;

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
        label->end_address = instruction_count;
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
        if (strlen(instructions[i]) != 32) {
            if (strncmp(instructions[i], "10010", 5) == 0 || 
                strncmp(instructions[i], "10011", 5) == 0 || 
                strncmp(instructions[i], "10100", 5) == 0) {

                char* start = strchr(instructions[i], '8');
                char* end = strchr(instructions[i], '9');
                
                if (start && end && start < end) {
                    char label_name[50] = {0};
                    int label_len = end - (start + 1);
                    if (label_len < 50) {
                        strncpy(label_name, start + 1, label_len);
                        label_name[label_len] = '\0';
                        
                        Label* label = find_label(label_name);
                        if (label != NULL) {
                            total_jumps_to_insert++;
                        }
                    }
                }
            }
        }
    }
    
    // Pre-allocate space for all return jumps
    for (int i = 0; i < total_jumps_to_insert; i++) {
        strcpy(instructions[instruction_count + i], "10010000000000000000000000000000");
    }
    instruction_count += total_jumps_to_insert;
    
    // Second pass: Process all jump instructions and update addresses
    int inserted_jumps = 0;
    for (int i = 0; i < instruction_count - total_jumps_to_insert; i++) {
        if (strlen(instructions[i]) != 32) {
            char jump_type[6] = {0};
            strncpy(jump_type, instructions[i], 5);
            jump_type[5] = '\0';
            
            if (strcmp(jump_type, "10010") == 0 || 
                strcmp(jump_type, "10011") == 0 || 
                strcmp(jump_type, "10100") == 0) {
                
                char* start = strchr(instructions[i], '8');
                char* end = strchr(instructions[i], '9');
                
                if (start && end && start < end) {
                    char label_name[50] = {0};
                    int label_len = end - (start + 1);
                    if (label_len < 50) {
                        strncpy(label_name, start + 1, label_len);
                        label_name[label_len] = '\0';
                        
                        Label* label = find_label(label_name);
                        if (label != NULL) {
                            char binary_address[14] = {0};
                            memset(binary_address, '0', 13);
                            
                            int address = label->start_address - 1;
                            for (int j = 12; j >= 0 && address > 0; j--) {
                                binary_address[j] = '0' + (address & 1);
                                address >>= 1;
                            }

                            char new_instruction[33] = {0};
                            char relleno_1[15] = "00000000000000";
                            strcpy(new_instruction, jump_type);
                            strcat(new_instruction, binary_address);
                            strcat(new_instruction, relleno_1);
                            
                            strcpy(instructions[i], new_instruction);
                            
                            int return_pos = label->end_address + inserted_jumps;
                            int return_target = i + 1;
                            
                            for (int j = instruction_count - 1; j > return_pos; j--) {
                                strcpy(instructions[j], instructions[j-1]);
                            }
                            
                            char return_binary[14] = {0};
                            memset(return_binary, '0', 13);

                            address = return_target - 1;
                            for (int j = 12; j >= 0 && address > 0; j--) {
                                return_binary[j] = '0' + (address & 1);
                                address >>= 1;
                            }
                            
                            char return_jump[33] = "10010";
                            char relleno_2[15] = "00000000000000";
                            strcat(return_jump, return_binary);
                            strcat(return_jump, relleno_2);
                            strcpy(instructions[return_pos], return_jump);
                            
                            inserted_jumps++;
                        }
                    }
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

BINARY      [01]{32}
JUMP_MARKER [01]{5}*8[A-Za-z_][A-Za-z0-9_]*9[01]*  
LABEL       [A-Za-z_][A-Za-z0-9_]*  
TERM_LABEL  TERM_{LABEL}

%%

{BINARY} {
    strncpy(instructions[instruction_count], yytext, sizeof(instructions[instruction_count]) - 1);
    instructions[instruction_count][sizeof(instructions[instruction_count]) - 1] = '\0';
    instruction_count++;
}

{JUMP_MARKER} {
    strncpy(instructions[instruction_count], yytext, sizeof(instructions[instruction_count]) - 1);
    instructions[instruction_count][sizeof(instructions[instruction_count]) - 1] = '\0';
    instruction_count++;
}

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

^[\t ]+ ;
\n      ;
.       ;

%%

int main(int argc, char **argv) {
    if (argc < 2) {
        fprintf(stderr, "Uso: %s <archivo_entrada>\n", argv[0]);
        return 1;
    }
    FILE *file = fopen(argv[1], "r");
    if (!file) {
        perror("Error al abrir el archivo");
        return 1;
    }

    if (argv[2] != NULL) {
        InitialJumps = atoi(argv[2]); 
    }

    for (int i = 0; i < InitialJumps; i++) {
        strcpy(instructions[instruction_count], "00001000000000010000000000000000");
        instruction_count++;
    }

    yyin = file;
    yylex();
    fclose(file);
    resolve_labels();

    // Mostrar solo las instrucciones finales
    for (int i = InitialJumps; i < instruction_count; i++) {
        printf("%s\n", instructions[i]);
    }

    return 0;
}
