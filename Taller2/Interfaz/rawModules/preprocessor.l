%{
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char input_path[512];  // Ruta completa del archivo de entrada
char libs_path[512];   // Ruta a la carpeta de librerías
char temp_preprocessor_path[512];  
char temp_libraries_path[512];  

FILE *preprocessor_output;
FILE *libraries_output;

void include_file(const char* filename);
%}

%option noyywrap

%%

^[[:space:]]*INCLUDERE[[:space:]]<\"([^\"]+)\">[[:space:]]* {
    char file_name[256];
    sscanf(yytext, "INCLUDERE <\"%[^\"]\">", file_name);

    char full_path[512];
    snprintf(full_path, sizeof(full_path), "%s%s", libs_path, file_name);

    include_file(full_path);  // Carga el archivo y lo guarda en libraries_output

    fprintf(preprocessor_output, "\n"); // Mantiene la estructura original
}

.* {
    fprintf(preprocessor_output, "%s\n", yytext); // Mantiene los saltos de línea
}
%%

void include_file(const char* filename) {
    FILE* file = fopen(filename, "r");
    if (!file) {
        fprintf(stderr, "Error: No se pudo abrir el archivo %s\n", filename);
        exit(1);
    }

    char line[1024];
    while (fgets(line, sizeof(line), file)) {
        fprintf(libraries_output, "%s", line); // Guarda el contenido de la librería
    }

    fclose(file);
}

int main(int argc, char** argv) {
    if (argc < 5) {
        fprintf(stderr, "Uso: %s <archivo_entrada> <ruta_librerias> <salida_preprocesador> <salida_librerias>\n", argv[0]);
        return 1;
    }

    strcpy(input_path, argv[1]);
    strcpy(libs_path, argv[2]);
    strcpy(temp_preprocessor_path, argv[3]);
    strcpy(temp_libraries_path, argv[4]);

    preprocessor_output = fopen(temp_preprocessor_path, "w");
    if (!preprocessor_output) {
        fprintf(stderr, "Error: No se pudo crear %s\n", temp_preprocessor_path);
        return 1;
    }

    libraries_output = fopen(temp_libraries_path, "w");
    if (!libraries_output) {
        fprintf(stderr, "Error: No se pudo crear %s\n", temp_libraries_path);
        fclose(preprocessor_output);
        return 1;
    }

    FILE* input_file = fopen(input_path, "r");
    if (!input_file) {
        fprintf(stderr, "Error: No se pudo abrir el archivo %s\n", input_path);
        fclose(preprocessor_output);
        fclose(libraries_output);
        return 1;
    }
    yyin = input_file;

    yylex();  // Procesar archivo

    fclose(input_file);
    fclose(preprocessor_output);
    fclose(libraries_output);
    return 0;
}
