import sys
import os
from ply import lex

# Asignar un valor ficticio a __file__ para evitar el error en Google Colab
if not hasattr(sys.modules['__main__'], '__file__'):
    sys.modules['__main__'].__file__ = '__main__.py'

class Lexer:
    # CONSTRUCTOR
    def __init__(self):
        print('Lexer constructor called.')
        self.symbol_table = {}
        self.errors = []

    # DESTRUCTOR
    def __del__(self):
        print('Lexer destructor called.')

    # Tokens
    tokens = (
        'FUNZIONE', 'SE', 'ALTRIMENTI', 'MENTRE', 'PER', 'RESTITUIRE', 'INTERROMPERE', 'CONTINUARE', 'SCRIVERE', 'LEGGERE',
        'ADD', 'SUB', 'MUL', 'DIV', 'MOD',
        'E', 'O', 'XOR', 'VERO', 'FALSO',
        'LT', 'LE', 'EQ', 'NE', 'GT', 'GE', 'IG',
        'ID', 'NUMBER', 'STRING', 'BOOL', 'NULL',
        'CL', 'CR', 'PL', 'PR', 'SC', 'CO', 'COM',
        'CAMPIONE', 'NUOVO', 'ESTENDI', 'PACCHETTO', 'CLASSE', 'IMPORTA', 'OGGETTO', 'METODO', 'ATTRIBUTO', 'PRIVATO', 'PUBBLICO', 'PROTETTO'
    )

    # Palabras reservadas
    reserved = {
        'funzione': 'FUNZIONE',
        'se': 'SE',
        'altrimenti': 'ALTRIMENTI',
        'mentre': 'MENTRE',
        'per': 'PER',
        'restituire': 'RESTITUIRE',
        'interrompere': 'INTERROMPERE',
        'continuare': 'CONTINUARE',
        'scrivere': 'SCRIVERE',
        'leggere': 'LEGGERE',
        'e': 'E',
        'o': 'O',
        'xor': 'XOR',
        'vero': 'VERO',
        'falso': 'FALSO',
        'campione': 'CAMPIONE',
        'nuovo': 'NUOVO',
        'estendi': 'ESTENDI',
        'pacchetto': 'PACCHETTO',
        'classe': 'CLASSE',
        'importa': 'IMPORTA',
        'oggetto': 'OGGETTO',
        'metodo': 'METODO',
        'attribuito': 'ATTRIBUTO',
        'privato': 'PRIVATO',
        'pubblico': 'PUBBLICO',
        'protetto': 'PROTETTO'
    }

    # Reglas de expresiones regulares para tokens simples
    t_ADD = r'\+'
    t_SUB = r'-'
    t_MUL = r'\*'
    t_DIV = r'/'
    t_MOD = r'%'
    t_LT = r'<'
    t_LE = r'<='
    t_EQ = r'=='
    t_NE = r'!='
    t_GT = r'>'
    t_GE = r'>='
    t_IG = r'='
    t_CL = r'\{'
    t_CR = r'\}'
    t_PL = r'\('
    t_PR = r'\)'
    t_SC = r';'
    t_CO = r':'
    t_COM = r','

    # Caracteres ignorados
    t_ignore = ' \t'

    # Reglas de expresiones regulares con código de acción
    def t_RESERVED(self, t):
        r'[A-Za-z_][A-Za-z0-9_]*'
        t.type = self.reserved.get(t.value.lower(), 'ID')
        if t.type != 'ID':
            return t
        else:
            return self.t_ID(t)

    def t_ID(self, t):
        r'[A-Za-z_][A-Za-z0-9_]*'
        self.symbol_table[t.value] = 'ID'
        return t

    def t_NUMBER(self, t):
        r'\d+(\.\d+)?'
        t.value = float(t.value) if '.' in t.value else int(t.value)
        self.symbol_table[t.value] = 'NUMBER'
        return t

    def t_STRING(self, t):
        r'\"([^"\\]|\\.|\\\\)*\"'
        t.value = t.value[1:-1]  # Quitar las comillas
        self.symbol_table[t.value] = 'STRING'
        return t

    def t_COMMENT(self, t):
        r'//.*'
        pass  # Ignorar comentarios

    # Regla para rastrear números de línea
    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    # Regla para manejar errores
    def t_error(self, t):
        error_message = f"Illegal character '{t.value[0]}' at line {t.lineno}, column {self.find_column(t)}"
        self.errors.append(error_message)
        t.lexer.skip(1)

    # Encontrar la columna
    def find_column(self, token):
        last_cr = self.lexer.lexdata.rfind('\n', 0, token.lexpos)
        if last_cr < 0:
            last_cr = 0
        column = (token.lexpos - last_cr) + 1
        return column

    # Método para construir el lexer
    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, lextab='lexer_table', outputdir='.', **kwargs)

    # Método para alimentar el lexer con código
    def input(self, data):
        self.lexer.input(data)

    # Método para obtener el siguiente token
    def token(self):
        return self.lexer.token()

    # Método de prueba
    def test(self, data):
        self.input(data)
        while True:
            tok = self.token()
            if not tok:
                break
            print(tok)
        print("Symbol Table:", self.symbol_table)

    # Escribir errores en un archivo
    def write_errors_to_file(self, filename):
        with open(filename, 'w') as f:
            for error in self.errors:
                f.write(error + '\n')

# Prueba
if __name__ == "__main__":
    lexer = Lexer()
    lexer.build()  # Construir el lexer antes de usarlo
    lexer.test('FUNZIONE calcular  SE x > 10 ALTRIMENTI x = x + 1')