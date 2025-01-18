%{
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char input_path[256]; // Ruta completa del archivo de entrada
char libs_path[256];  // Ruta a la carpeta de librerías
int processing_libraries = 1; // Indicador para saber si estamos en la sección de librerías

void include_file(const char* filename);
%}

%option noyywrap

%%
^[[:space:]]*INCLUDERE[[:space:]]<\"([^\"]+)\">[[:space:]]* {
    if (!processing_libraries) {
        fprintf(stderr, "Error: 'INCLUDERE' encontrado fuera de la seccion de librerías.\n");
        exit(1);
    }

    // Extraer el nombre del archivo dentro de las comillas
    char file_name[256];
    sscanf(yytext, "INCLUDERE <\"%[^\"]\">", file_name);

    // Construir la ruta completa al archivo dentro de la carpeta 'libs/'
    char full_path[512];
    snprintf(full_path, sizeof(full_path), "%s%s", libs_path, file_name);

    // Cargar el archivo de la ruta completa
    include_file(full_path);
}

.* {
    if (processing_libraries) {
        // Cuando aparece cualquier línea que no sea una directiva válida de librería
        processing_libraries = 0;
        printf("****FIN LIBRERIAS****\n"); // Separador de sección
    }
    printf("%s", yytext); // Imprimir la línea tal cual
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
        printf("%s", line); // Imprimir el contenido del archivo
    }

    fclose(file);
}

int main(int argc, char** argv) {
    if (argc < 3) {
        fprintf(stderr, "Uso: %s <archivo_entrada.txt> <ruta_librerias>\n", argv[0]);
        return 1;
    }

    // Guardar las rutas del archivo de entrada y las librerías
    strcpy(input_path, argv[1]);
    strcpy(libs_path, argv[2]);

    // Abrir el archivo de entrada como stdin para Flex
    FILE* input_file = fopen(input_path, "r");
    if (!input_file) {
        fprintf(stderr, "Error: No se pudo abrir el archivo %s\n", input_path);
        return 1;
    }
    yyin = input_file;

    yylex(); // Procesar el archivo

    fclose(input_file);
    return 0;
}
