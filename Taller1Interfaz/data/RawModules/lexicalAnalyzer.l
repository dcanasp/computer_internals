%{
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/* TOKENS */

#define KW              300
#define FUNZIONE        400   /*Function, para definir una funcion*/
#define SE              410   /*If*/
#define ALTRIMENTI      420   /*Else*/
#define MENTRE          430   /*While*/
#define PER             440   /*For*/
#define RESTITUIRE      450   /*Return, para definir final de una funcion (o no)*/
#define INTERROMPERE    460   /*Break, para romper un ciclo*/
#define CONTINUARE      470   /*Continue, para saltarse un ciclo*/
#define IMPORTA         490   /*Import*/

#define ARITOP    700     /* Operadores aritméticos */
#define ADD       710     /* + */
#define SUB       720     /* - */
#define MUL       730     /* * */
#define DIV       740     /* / */
#define MOD       750     /* % */

#define LOGOP     500     /* Operadores logicos */
#define E         510     /* And */
#define O         560     /* Or */ 
#define NON       570     /* Not */
#define VERO      580     /* True */
#define FALSO     590     /* False */

#define RELOP     600     /* Operadores relacionales */
#define LT        610     /* <  */
#define LE        620     /* <= */
#define EQ        630     /* == */
#define NE        640     /* != */
#define GT        650     /* >  */
#define GE        660     /* >= */

#define ID        800
#define NUMBER    900
#define STRING    1000
#define COMMENT   1100


#define MAX_TABLE_SIZE 100

typedef union {
    char* str;
    int intval;
    char lexeme[100];
} YYSTYPE;

YYSTYPE yylval;

typedef struct {
    char lexeme[100];
    char type[20];
    char value[100];
} SymbolTableEntry;

/* TABLAS DE SÍMBOLOS */
SymbolTableEntry idTable[MAX_TABLE_SIZE];
SymbolTableEntry numTable[MAX_TABLE_SIZE];
SymbolTableEntry strTable[MAX_TABLE_SIZE];
SymbolTableEntry commentTable[MAX_TABLE_SIZE];

int idCount = 0;
int numCount = 0;
int strCount = 0;
int commentCount = 0;

int installID();
int installNum();
int installStr();
int installComment();
void printSymbolTables();
char* processString();
void processComments(const char* text);
%}

/* Expresiones regulares */
delim      [ \t\n]+
letter     [A-Za-z_]
digit      [0-9]
id         {letter}({letter}|{digit})*
number     {digit}+(\.{digit}+)?(E[+-]?{digit}+)? 
string     \"([^"\\]|\\.|\\\\)*\"                
comment    "//".*                                

%%

{delim}      {/* Ignorar espacios */} 

"FUNZIONE"      { printf("PALABRA RESERVADA: 'funzione'\n"); return FUNZIONE; }
"SE"            { printf("PALABRA RESERVADA: 'se'\n"); return SE; }
"ALTRIMENTI"    { printf("PALABRA RESERVADA: 'altrimenti'\n"); return ALTRIMENTI; }
"MENTRE"        { printf("PALABRA RESERVADA: 'mentre'\n"); return MENTRE; }
"PER"           { printf("PALABRA RESERVADA: 'per'\n"); return PER; }
"RESTITUIRE"    { printf("PALABRA RESERVADA: 'restituire'\n"); return RESTITUIRE; }
"INTERROMPERE"  { printf("PALABRA RESERVADA: 'interrompere'\n"); return INTERROMPERE; }
"CONTINUARE"    { printf("PALABRA RESERVADA: 'continuare'\n"); return CONTINUARE; }
"IMPORTA"       { printf("PALABRA RESERVADA: 'importa'\n"); return IMPORTA; }

"+"             { printf("OPERADOR ARITMETICO: '+'\n"); return ADD; }
"-"             { printf("OPERADOR ARITMETICO: '-'\n"); return SUB; }
"*"             { printf("OPERADOR ARITMETICO: '*'\n"); return MUL; }
"/"             { printf("OPERADOR ARITMETICO: '/'\n"); return DIV; }
"%"             { printf("OPERADOR ARITMETICO: '%'\n"); return MOD; }

"E"             { printf("OPERADOR LOGICO: 'e'\n"); return E; }
"O"             { printf("OPERADOR LOGICO: 'o'\n"); return O; }
"NON"           { printf("OPERADOR LOGICO: 'non'\n"); return NON; }
"VERO"          { printf("BOOLEANO: 'VERDADERO'\n"); return VERO; }
"FALSO"         { printf("BOOLEANO: 'FALSO'\n"); return FALSO; }

"<"             { printf("OPERADOR RELACIONAL: '<'\n"); return LT; }
"<="            { printf("OPERADOR RELACIONAL: '<='\n"); return LE; }
"=="            { printf("OPERADOR RELACIONAL: '=='\n"); return EQ; }
"!="            { printf("OPERADOR RELACIONAL: '!='\n"); return NE; }
">"             { printf("OPERADOR RELACIONAL: '>'\n"); return GT; }
">="            { printf("OPERADOR RELACIONAL: '>='\n"); return GE; }


{id}       { strcpy(yylval.lexeme, yytext); installID(); return ID; }

{number}   { yylval.intval = atoi(yytext); installNum(); return NUMBER; } /* Solo ENTEROOOOOS odio los float */

{string}   { char* processed = processString(yytext); installStr(processed); free(processed); return STRING; }

{comment}  { processComments(yytext); return COMMENT; }

%%

/* FUNCIONES */
int installID() {
    for (int i = 0; i < idCount; i++) {
        if (strcmp(idTable[i].lexeme, yylval.lexeme) == 0) {
            return i;
        }
    }
    if (idCount < MAX_TABLE_SIZE) {
        strcpy(idTable[idCount].lexeme, yylval.lexeme);
        strcpy(idTable[idCount].type, "ID");
        sprintf(idTable[idCount].value, "N/A");
        return idCount++;
    } else {
        printf("Tabla de identificadores llena!\n");
        exit(1);
    }
}

int installNum() {
    for (int i = 0; i < numCount; i++) {
        if (strcmp(numTable[i].lexeme, yytext) == 0) {
            return i;
        }
    }
    if (numCount < MAX_TABLE_SIZE) {
        strcpy(numTable[numCount].lexeme, yytext);
        strcpy(numTable[numCount].type, "NUMBER");
        sprintf(numTable[numCount].value, "%d", yylval.intval);
        return numCount++;
    } else {
        printf("Tabla de numeros llena!\n");
        exit(1);
    }
}

int installStr(const char* processedString) {
    for (int i = 0; i < strCount; i++) {
        if (strcmp(strTable[i].lexeme, processedString) == 0) {
            return i;
        }
    }
    if (strCount < MAX_TABLE_SIZE) {
        strcpy(strTable[strCount].lexeme, processedString);
        strcpy(strTable[strCount].type, "STRING");
        sprintf(strTable[strCount].value, "\"%s\"", processedString);
        return strCount++;
    } else {
        printf("Tabla de cadenas llena!\n");
        exit(1);
    }
}

int installComment() {
    for (int i = 0; i < commentCount; i++) {
        if (strcmp(commentTable[i].lexeme, yytext) == 0) {
            return i;
        }
    }
    if (commentCount < MAX_TABLE_SIZE) {
        strcpy(commentTable[commentCount].lexeme, yytext);
        strcpy(commentTable[commentCount].type, "COMMENT");
        sprintf(commentTable[commentCount].value, "%s", yytext);
        return commentCount++;
    } else {
        printf("Tabla de comentarios llena!\n");
        exit(1);
    }
}

char* processString(const char* text) {
    char* result = malloc(strlen(text) - 1);
    char *dest = result;
    const char *src = text + 1; // Saltamos la primera comilla

    while (*src && *(src + 1)) { // Evitamos la última comilla
        if (*src == '\\') {
            src++;
            if (*src == '\"') *dest++ = '\"';
            else if (*src == '\\') *dest++ = '\\';
            else *dest++ = *src;
        } else {
            *dest++ = *src;
        }
        src++;
    }
    *dest = '\0'; // Terminamos el string
    return result;
}

void processComments(const char* text) {
    printf("COMENTARIO: '%s'\n", text);
    installComment();
}

void printSymbolTables() {
    printf("\n--- TABLA DE IDENTIFICADORES ---\n");
    for (int i = 0; i < idCount; i++) {
        printf("Posicion %d | Lexema: %s | Tipo: %s | Valor: %s\n", 
               i, idTable[i].lexeme, idTable[i].type, idTable[i].value);
    }

    printf("\n--- TABLA DE NUMEROS ---\n");
    for (int i = 0; i < numCount; i++) {
        printf("Posicion %d | Lexema: %s | Tipo: %s | Valor: %s\n", 
               i, numTable[i].lexeme, numTable[i].type, numTable[i].value);
    }

    printf("\n--- TABLA DE CADENAS ---\n");
    for (int i = 0; i < strCount; i++) {
        printf("Posicion %d | Lexema: %s | Tipo: %s | Valor: %s\n", 
               i, strTable[i].lexeme, strTable[i].type, strTable[i].value);
    }

    printf("\n--- TABLA DE COMENTARIOS ---\n");
    for (int i = 0; i < commentCount; i++) {
        printf("Posicion %d | Lexema: %s | Tipo: %s | Valor: %s\n", 
               i, commentTable[i].lexeme, commentTable[i].type, commentTable[i].value);
    }
}

int main(int argc, char **argv) {
    if (argc < 2) {
        printf("Uso: %s <archivo_de_entrada.txt>\n", argv[0]);
        return 1;
    }

    FILE *file = fopen(argv[1], "r");
    if (!file) {
        perror("Error al abrir el archivo");
        return 1;
    }

    yyin = file;
    printf("------ Iniciando Analisis Lexico ------\n");
    while (yylex() != 0);  // Analizar todo el archivo

    fclose(file);
    printSymbolTables();
    return 0;
}

int yywrap() {
    return 1;
}
