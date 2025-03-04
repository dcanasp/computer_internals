%{
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

char libs_path[1024];   // Ruta a la carpeta de librerías
char temp_libraries_path[1024];  

FILE *preprocessor_output;
FILE *libraries_output;

char *strtrim(char *str) {
    // Eliminar espacios al final
    char *end = str + strlen(str) - 1;
    while (end >= str && isspace((unsigned char)*end)) {
        end--;
    }
    *(end + 1) = '\0';

    // Eliminar espacios al principio
    char *start = str;
    while (*start && isspace((unsigned char)*start)) {
        start++;
    }
    memmove(str, start, strlen(start) + 1);

    return str;
}

void include_file(const char* filename);
%}

%option noyywrap

%%

^[[:space:]]*\/\/.* {
    fprintf(preprocessor_output, "%s\n", yytext);
}

^[[:space:]]*IMPORTA[[:space:]]*\"([^\"]+)\"[[:space:]]* {
    char file_name[256];
    char *p1 = strchr(yytext, '\"');  // Busca la primera comilla
    if(p1) {
        p1++;  // Salta la comilla
        char *p2 = strchr(p1, '\"'); // Busca la segunda comilla
        if(p2) {
            int len = p2 - p1;
            if(len >= 255)
                len = 255;
            strncpy(file_name, p1, len);
            file_name[len] = '\0';

            strtrim(file_name);  // Quita espacios extra
          
            char full_path[512];
            snprintf(full_path, sizeof(full_path), "%s%s", libs_path, file_name);
          
            include_file(full_path);  // Carga el archivo
            fprintf(preprocessor_output, "%s\n", yytext);
        }
    }
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

    strcpy(libs_path, argv[2]);

    preprocessor_output = fopen(argv[3], "w");
    if (!preprocessor_output) {
        fprintf(stderr, "Error: No se pudo crear %s\n", argv[3]);
        return 1;
    }

    libraries_output = fopen(argv[4], "w");
    if (!libraries_output) {
        fprintf(stderr, "Error: No se pudo crear %s\n", argv[4]);
        fclose(preprocessor_output);
        return 1;
    }

    FILE* input_file = fopen(argv[1], "r");
    if (!input_file) {
        fprintf(stderr, "Error: No se pudo abrir el archivo %s\n", argv[1]);
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
