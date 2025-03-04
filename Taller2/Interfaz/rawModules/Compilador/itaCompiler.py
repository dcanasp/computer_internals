import os
import argparse
from pathlib import Path
from lexerAnalyzer import Lexer
from itaParser import MyParser

class Compiler:
    def __init__(self):
        self.myLex = Lexer()
        self.myPars = MyParser(self.myLex)

    def compile(self, code=""):
        if not code:
            file_path = "lexPrueba3.txt"
            print(f"Reading file: {file_path}")
            if not os.path.exists(file_path):
                print(f"Error: File {file_path} not found")
                return ""
            with open(file_path, 'r') as file:
                code = file.read()

        # Construir el lexer y el parser
        self.myLex.build()
        self.myPars.build()

        # Analizar el código y obtener el assembler
        asm_result = self.myPars.test(code)

        # Imprimir el resultado directamente aquí si existe
        if asm_result:
            print("Assembler generado por el compilador:")
            print(asm_result)

        # Retornar el assembler generado
        return asm_result if asm_result else self.myPars.resultAsm

    def write_symbol_table_to_file(self, filepath):
            with open(filepath, 'w') as f:
                f.write("Tabla de Símbolos:\n")
                for symbol, attributes in self.myLex.symbol_table.items():
                    f.write(f"{symbol}: {attributes}\n")

def main():
    parser = argparse.ArgumentParser(description="Compiler script")
    parser.add_argument('input_file', type=str, help='Input file to compile')
    parser.add_argument('output_file', type=str, help='Output file for the assembler code')
    parser.add_argument('libs_input_file', type=str, help='Input file with the libraries')
    parser.add_argument('parser_error_file', type=str, help='Output file for the parser errors')
    parser.add_argument('symbol_table_file', type=str, help='Output file for the symbol table')
    args = parser.parse_args()

    # Validar que todos los parámetros se hayan proporcionado
    if not args.input_file:
        print("Error: 'input_file' parameter is missing")
        return
    if not args.output_file:
        print("Error: 'output_file' parameter is missing")
        return
    if not args.libs_input_file:
        print("Error: 'libs_input_file' parameter is missing")
        return
    if not args.parser_error_file:
        print("Error: 'parser_error_file' parameter is missing")
        return
    if not args.symbol_table_file:
        print("Error: 'symbol_table_file' parameter is missing")
        return

    compiler = Compiler()
    compiler.myPars.librariesRuta = args.libs_input_file
    with open(args.input_file, 'r') as file:
        code = file.read()

    asm_output = compiler.compile(code)

    with open(args.output_file, 'w') as file:
        file.write(asm_output)

    compiler.write_symbol_table_to_file(args.symbol_table_file)
    compiler.myLex.write_errors_to_file(args.parser_error_file)

if __name__ == "__main__":
    main()