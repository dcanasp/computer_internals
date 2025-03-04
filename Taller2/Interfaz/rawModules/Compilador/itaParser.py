import ply.yacc as yacc
import os

class MyParser:
    def __init__(self, lexer):
        print("Parser constructor called")
        self.lexer = lexer
        self.lookUpTable = {}
        self.lexerLookUpTable = self.lexer.symbol_table
        self.resultAsm = ''
        self.module_code = ''
        self.countVar = 0  # Direcciones de memoria desde 0
        self.lookUpJumps = {}
        self.countJumps = 1
        self.parser = None
        self.librerias_cargadas = {}
        self.registros_disponibles = [4, 5]  # Solo 2 registros para consistencia
        self.current_reg_index = 0
        self.classes = {}
        self.objects = {}
        self.current_class = None
        self.jumpTable = {}
        self.in_main = True  # Bandera para controlar si estamos en main
        self.using_library = False  # Bandera para controlar si se usa una librería
        self.after_jmp2 = False  # Bandera para controlar si estamos después de jmp2
        self.librariesRuta = ''

    def __del__(self):
        print('Parser destructor called.')


    tokens = (
        'FUNZIONE', 'SE', 'ALTRIMENTI', 'MENTRE', 'PER', 'RESTITUIRE', 'INTERROMPERE', 'CONTINUARE', 'SCRIVERE', 'LEGGERE',
        'ADD', 'SUB', 'MUL', 'DIV', 'MOD',
        'E', 'O', 'XOR', 'VERO', 'FALSO',
        'LT', 'LE', 'EQ', 'NE', 'GT', 'GE', 'IG',
        'ID', 'NUMBER', 'STRING', 'BOOL', 'NULL',
        'CL', 'CR', 'PL', 'PR', 'SC', 'CO', 'COM',
        'CAMPIONE', 'NUOVO', 'ESTENDI', 'PACCHETTO', 'CLASSE', 'IMPORTA', 'OGGETTO', 'METODO', 'ATTRIBUTO', 'PRIVATO', 'PUBBLICO', 'PROTETTO'
    )    
    precedence = (
        ('nonassoc', 'LT', 'LE', 'GT', 'GE', 'EQ', 'NE'),
        ('left', 'ADD', 'SUB'),
        ('left', 'MUL', 'DIV', 'MOD'),
        ('left', 'E', 'O'),
    )

    def get_next_register(self):
        reg = self.registros_disponibles[self.current_reg_index % len(self.registros_disponibles)]
        self.current_reg_index += 1
        if self.current_reg_index >= len(self.registros_disponibles):
            self.current_reg_index = 0
        return reg

    def reset_registers(self):
        self.current_reg_index = 0

    # PROGRAMA (Ajustado para eliminar espacios al inicio de FIN y END)
    def p_programa(self, p):
      '''
      programa : proposiciones
      '''
      main_code = 'BEGIN\n' + (p[1] if p[1] is not None else '').rstrip()
      # Insertar JUMP jump_fin y jump_fin: solo si se usó una librería
      if self.using_library:
          main_code = main_code.rstrip() + '\nJUMP jump_fin\n'
          all_code = f"{main_code}\n{self.module_code.strip()}\njump_fin:\n"
      else:
          all_code = f"{main_code}\n{self.module_code.strip()}"
      all_code = '\n'.join(line.lstrip() for line in all_code.splitlines() if line.strip())
      self.resultAsm = f"{all_code}\nFIN\nEND"
      p[0] = self.resultAsm
      self.in_main = False
      self.using_library = False  # Reiniciar explícitamente
      self.after_jmp2 = False

    # PAQUETTO
    def p_paquete(self, p):
        '''
        paquete : PACCHETTO ID CL paquete_contenido CR
        '''
        pseudoAsm = f'PACKAGE {p[2]}\n'
        pseudoAsm += p[4] if p[4] is not None else ''
        self.resultAsm = pseudoAsm
        p[0] = self.resultAsm

    def p_paquete_contenido(self, p):
        '''
        paquete_contenido : definicion_clase paquete_contenido
                          | proposicion paquete_contenido
                          | empty
        '''
        if len(p) == 3:
            p[0] = (p[1] if p[1] is not None else '') + (p[2] if p[2] is not None else '')
        else:
            p[0] = p[1] if p[1] is not None else ''

    # ALGORITMO
    def p_algoritmo(self, p):
        '''
        algoritmo : FUNZIONE ID PL PR CL proposiciones CR
        '''
        func_name = p[2]
        self.in_main = func_name == 'main'
        self.after_jmp2 = False
        pseudoAsm = f'{func_name}:\n'
        pseudoAsm += p[6] if p[6] is not None else ''
        p[0] = pseudoAsm

    # DEFINICIÓN DE CLASE
    def p_definicion_clase(self, p):
        '''
        definicion_clase : CLASSE ID CL clase_contenido CR
                         | CLASSE ID ESTENDI ID CL clase_contenido CR
        '''
        class_name = p[2]
        self.current_class = class_name
        self.in_main = False
        self.using_library = False
        self.after_jmp2 = False
        pseudoAsm = f'CLASS {class_name}\n'
        if len(p) == 8:
            parent_class = p[4]
            pseudoAsm += f'EXTENDS {parent_class}\n'
            if parent_class in self.classes:
                self.classes[class_name] = self.classes[parent_class].copy()
            else:
                print(f"ERROR: Clase base {parent_class} no definida")
            pseudoAsm += p[6] if p[6] is not None else ''
        else:
            self.classes[class_name] = {}
            pseudoAsm += p[4] if p[4] is not None else ''
        self.current_class = None
        p[0] = pseudoAsm

    # CONTENIDO DE CLASE
    def p_clase_contenido(self, p):
        '''
        clase_contenido : clase_elemento clase_contenido
                        | clase_elemento
                        | empty
        '''
        if len(p) == 3:
            p[0] = (p[1] if p[1] is not None else '') + (p[2] if p[2] is not None else '')
        else:
            p[0] = p[1] if p[1] is not None else ''

    def p_clase_elemento(self, p):
        '''
        clase_elemento : modificador ATTRIBUTO ID IG NUMBER SC
                       | modificador METODO ID PL PR CL proposiciones CR
        '''
        pseudoAsm = ''
        if p[2] == 'ATTRIBUTO':
            attr_name = p[3]
            valor = int(p[5])
            pseudoAsm += f'{p[1]} ATTR {attr_name} = {valor}\n'
            if self.current_class:
                self.classes[self.current_class][attr_name] = {'access': p[1], 'value': valor}
        elif p[2] == 'METODO':
            method_name = p[3]
            pseudoAsm += f'{p[1]} METHOD {method_name}\n'
            pseudoAsm += p[7] if p[7] is not None else ''
            if self.current_class:
                self.classes[self.current_class][method_name] = {'access': p[1], 'code': p[7]}
        p[0] = pseudoAsm

    # MODIFICADOR DE ACCESO
    def p_modificador(self, p):
        '''
        modificador : PRIVATO
                    | PUBBLICO
                    | PROTETTO
        '''
        p[0] = p[1]

    # EMPTY
    def p_empty(self, p):
        'empty :'
        p[0] = ''

    # PROPOSICIONES
    def p_proposiciones(self, p):
        '''
        proposiciones : proposicion proposiciones
                      | proposicion
        '''
        if len(p) == 3:
            p[0] = (p[1] if p[1] is not None else '') + (p[2] if p[2] is not None else '')
        else:
            p[0] = p[1] if p[1] is not None else ''

    def p_proposicion(self, p):
      '''
      proposicion : asignacion SC
                  | asignacion
                  | inicializar_variable SC
                  | inicializar_variable
                  | sentencia_si
                  | sentencia_mientras
                  | sentencia_leer SC
                  | sentencia_leer
                  | sentencia_escribir SC
                  | sentencia_escribir
                  | IMPORTA STRING SC
                  | IMPORTA STRING
                  | llamada_modulo SC
                  | llamada_modulo
                  | instancia_objeto SC
                  | instancia_objeto
                  | muestra_campione SC
                  | muestra_campione
                  | algoritmo
      '''
      self.reset_registers()
      if len(p) >= 3 and p[1] == 'IMPORTA':
          nombre = p[2][1:-1].strip()
          self.cargar_libreria(nombre)
          self.using_library = True  # Activar solo con IMPORTA
          p[0] = ""
      else:
          p[0] = p[1] if p[1] is not None else ''

    # INSTANCIA DE OBJETO
    def p_instancia_objeto(self, p):
        '''
        instancia_objeto : OGGETTO ID IG NUOVO ID PL PR
        '''
        obj_name = p[2]
        class_name = p[5]
        pseudoAsm = ''
        if class_name in self.classes:
            pseudoAsm += f'OBJECT {obj_name} = NEW {class_name}\n'
            self.objects[obj_name] = {'class': class_name, 'attributes': self.classes[class_name].copy()}
        else:
            print(f"ERROR: Clase {class_name} no definida")
        p[0] = pseudoAsm

    # MUESTRA CAMPIONE (PROTOTIPO)
    def p_muestra_campione(self, p):
        '''
        muestra_campione : CAMPIONE ID
        '''
        sample_name = p[2]
        pseudoAsm = f'SAMPLE {sample_name}\n'
        if sample_name in self.objects:
            pseudoAsm += f'OUTPUT INSTANCE {sample_name} OF {self.objects[sample_name]["class"]}\n'
        else:
            print(f"ERROR: Objeto {sample_name} no definido")
        p[0] = pseudoAsm

    # ASIGNACIÓN (Manteniendo las instrucciones correctas y controlando JUMP jump_fin)
    def p_asignacion(self, p):
      '''
      asignacion : ID IG exp_aritmetica
                | ID IG exp_booleana
                | ID IG NULL
                | ID IG STRING
                | ID IG ID
                | ID IG NUMBER
                | ID IG llamada_modulo
      '''
      pseudoAsm = ''
      esCadena = False

      if self.lookUpTable.get(p[1]) is None and self.countVar <= 20:
          self.lookUpTable[p[1]] = ['NUMBER', self.countVar]
          self.countVar += 1
      elif self.countVar > 20:
          print(f'ERROR: NO SE PUEDEN DEFINIR MÁS DE 20 VARIABLES')
          p[0] = ''
          return

      self.reset_registers()
      reg_destino = self.get_next_register()
      direccion_memoria_destino = self.lookUpTable[p[1]][1]

      if isinstance(p[3], tuple) and p[3][1] == 'module_call':
          pseudoAsm += p[3][0]
          # Asegurar que resultado use la misma dirección asignada inicialmente
          if p[1] == 'resultado':
              direccion_memoria_destino = self.lookUpTable[p[1]][1]  # Usar la dirección original (1)
          pseudoAsm += f'STORE {direccion_memoria_destino} 28\n'
      elif p[3] and not (self.lexerLookUpTable.get(p[3]) in ['ID', 'NUMBER', 'STRING'] or p[3] == 'NULL'):
          pseudoAsm += p[3] if p[3] is not None else ''
      elif self.lexerLookUpTable.get(p[3]) == 'ID':
          if self.lookUpTable.get(p[3]) is None:
              print(f'ERROR: Variable {p[3]} no inicializada')
          else:
              pseudoAsm += f'LOADDISK {reg_destino} {self.lookUpTable[p[3]][1]}\n'
      elif self.lexerLookUpTable.get(p[3]) == 'NUMBER':
          valor = int(p[3])
          pseudoAsm += f'LOAD {reg_destino} {valor}\n'
      elif p[3] == 'NULL':
          pseudoAsm += f'LOAD {reg_destino} 0\n'
      elif isinstance(p[3], str) and p[3] in self.lexerLookUpTable and self.lexerLookUpTable[p[3]] == 'STRING':
          esCadena = True
          valorCadena = str(p[3]).replace('"', '')
          for i, char in enumerate(valorCadena):
              pseudoAsm += f'LOAD {reg_destino} {ord(char)}\n'
              pseudoAsm += f'STORE {direccion_memoria_destino + i} {reg_destino}\n'
          pseudoAsm += f'LOAD {reg_destino} 0\n'
          pseudoAsm += f'STORE {direccion_memoria_destino + len(valorCadena)} {reg_destino}\n'
          self.lookUpTable[p[1]][0] = 'cadena'
      else:
          pseudoAsm += p[3] if p[3] is not None else ''

      if not esCadena and (not isinstance(p[3], tuple) or p[3][1] != 'module_call'):
          pseudoAsm += f'STORE {direccion_memoria_destino} {reg_destino}\n'

      p[0] = pseudoAsm

    # INICIALIZAR VARIABLE
    def p_inicializar_variable(self, p):
        '''
        inicializar_variable : ID IG NUMBER
                            | ID IG VERO
                            | ID IG FALSO
                            | ID IG STRING
        '''
        if self.lookUpTable.get(p[1]) is None and self.countVar <= 20:
            self.lookUpTable[p[1]] = ['', self.countVar]
            self.countVar += 1
        elif self.countVar > 20:
            print('ERROR: NO SE PUEDEN DEFINIR MÁS DE 20 VARIABLES')
            p[0] = ''
            return

        pseudoAsm = ''
        reg = self.get_next_register()
        if p[2] == 'IG':
            if self.lexerLookUpTable.get(p[3]) == 'NUMBER':
                valor = int(p[3])
                pseudoAsm = f'LOAD {reg} {valor}\n'
                pseudoAsm += f'STORE {self.lookUpTable[p[1]][1]} {reg}\n'
                self.lookUpTable[p[1]][0] = 'NUMBER'
            elif p[3] == 'VERO':
                pseudoAsm = f'LOAD {reg} 1\n'
                pseudoAsm += f'STORE {self.lookUpTable[p[1]][1]} {reg}\n'
                self.lookUpTable[p[1]][0] = 'BOOL'
            elif p[3] == 'FALSO':
                pseudoAsm = f'LOAD {reg} 0\n'
                pseudoAsm += f'STORE {self.lookUpTable[p[1]][1]} {reg}\n'
                self.lookUpTable[p[1]][0] = 'BOOL'
            elif self.lexerLookUpTable.get(p[3]) == 'STRING':
                valorCadena = str(p[3]).replace('"', '')
                for i in range(len(valorCadena)):
                    caracter = ord(valorCadena[i])
                    pseudoAsm += f'LOAD {reg} {caracter}\n'
                    pseudoAsm += f'STORE {self.lookUpTable[p[1]][1] + i} {reg}\n'
                pseudoAsm += f'LOAD {reg} 0\n'
                pseudoAsm += f'STORE {self.lookUpTable[p[1]][1] + len(valorCadena)} {reg}\n'
                self.lookUpTable[p[1]][0] = 'cadena'
        p[0] = pseudoAsm

    # FACTOR ARITMÉTICO
    def p_factor_aritmetico(self, p):
        '''
        factor_aritmetico : NUMBER
                          | ID
        '''
        reg = self.get_next_register()
        if p[1] in self.lexer.symbol_table and self.lexer.symbol_table[p[1]] == 'NUMBER':
            if isinstance(p[1], float):
                print('ERROR: EL ANALIZADOR SINTÁCTICO DETECTA UN DECIMAL, se tomará solo la parte entera')
                valor = int(p[1])
            else:
                valor = p[1]
            p[0] = f'LOAD {reg} {valor}\n'
        else:
            if self.lookUpTable.get(p[1]) is None:
                print(f'ERROR: Variable {p[1]} no inicializada')
                p[0] = ''
            else:
                p[0] = f'LOADDISK {reg} {self.lookUpTable[p[1]][1]}\n'

    # TÉRMINO ARITMÉTICO
    def p_termino_aritmetico(self, p):
        '''
        termino_aritmetico : PL termino_aritmetico PR
                           | termino_aritmetico MUL termino_aritmetico
                           | termino_aritmetico DIV termino_aritmetico
                           | termino_aritmetico ADD termino_aritmetico
                           | termino_aritmetico SUB termino_aritmetico
                           | termino_aritmetico MOD termino_aritmetico
                           | factor_aritmetico
                           | SUB factor_aritmetico
        '''
        pseudoAsm = ''
        if p[1] == '-':
            self.reset_registers()
            reg1 = self.get_next_register()
            reg2 = self.get_next_register()
            pseudoAsm += p[2] if p[2] is not None else ''
            pseudoAsm += f'LOAD {reg2} 0\n'
            pseudoAsm += f'SUB {reg2} {reg1}\n'
            p[0] = pseudoAsm
            return
        if p[1] == '(':
            p[0] = p[2]
            return
        if len(p) == 2:
            p[0] = p[1]
            return
        if len(p) == 4:
            self.reset_registers()
            reg1 = self.get_next_register()
            reg2 = self.get_next_register()
            pseudoAsm += p[1] if p[1] is not None else ''
            if isinstance(p[3], str) and p[3].startswith('LOAD'):
                pseudoAsm += p[3].replace('LOAD 4', f'LOAD {reg2}').replace('LOAD 5', f'LOAD {reg2}')
            elif isinstance(p[3], str) and p[3].startswith('LOADDISK'):
                pseudoAsm += p[3].replace('LOADDISK 4', f'LOADDISK {reg2}').replace('LOADDISK 5', f'LOADDISK {reg2}')
            else:
                pseudoAsm += p[3] if p[3] is not None else ''
            if p[2] == '+':
                pseudoAsm += f'ADD {reg1} {reg2}\n'
            elif p[2] == '-':
                pseudoAsm += f'SUB {reg1} {reg2}\n'
            elif p[2] == '*':
                pseudoAsm += f'MULT {reg1} {reg2}\n'
            elif p[2] == '/':
                pseudoAsm += f'DIV {reg1} {reg2}\n'
            elif p[2] == '%':
                pseudoAsm += f'MOD {reg1} {reg2}\n'
            p[0] = pseudoAsm

    # EXPRESIÓN ARITMÉTICA
    def p_exp_aritmetica(self, p):
        '''
        exp_aritmetica : termino_aritmetico
        '''
        p[0] = p[1]

    # OPERADOR RELACIONAL
    def p_operador_relacional(self, p):
        '''
        operador_relacional : EQ
                            | NE
                            | LE
                            | GE
                            | LT
                            | GT
        '''
        p[0] = p[1]

    # FACTOR RELACIONAL
    def p_factor_relacional(self, p):
        '''
        factor_relacional : PL factor_relacional PR
                          | exp_aritmetica operador_relacional exp_aritmetica
        '''
        pseudoAsm = ''
        if p[1] == '(':
            p[0] = p[2]
            return
        if len(p) == 4:
            self.reset_registers()
            reg1 = self.get_next_register()
            reg2 = self.get_next_register()
            pseudoAsm += p[1] if p[1] is not None else ''
            if isinstance(p[3], str) and p[3].startswith('LOAD'):
                pseudoAsm += p[3].replace('LOAD 4', f'LOAD {reg2}').replace('LOAD 5', f'LOAD {reg2}')
            elif isinstance(p[3], str) and p[3].startswith('LOADDISK'):
                pseudoAsm += p[3].replace('LOADDISK 4', f'LOADDISK {reg2}').replace('LOADDISK 5', f'LOADDISK {reg2}')
            else:
                pseudoAsm += p[3] if p[3] is not None else ''
            if p[2] == '==':
                pseudoAsm += f'CMPREG {reg1} {reg2}\n'
            elif p[2] == '!=':
                pseudoAsm += f'CMPREG {reg1} {reg2}\n'
            elif p[2] == '<=':
                pseudoAsm += f'CMPLEREG {reg1} {reg2}\n'
            elif p[2] == '>=':
                pseudoAsm += f'CMPGEREG {reg1} {reg2}\n'
            elif p[2] == '<':
                pseudoAsm += f'CMPLREG {reg1} {reg2}\n'
            elif p[2] == '>':
                pseudoAsm += f'CMPGREG {reg1} {reg2}\n'
            p[0] = pseudoAsm

    # FACTOR BOOLEANO
    def p_factor_booleano(self, p):
        '''
        factor_booleano : PL exp_booleana PR
                        | VERO
                        | FALSO
                        | factor_relacional
                        | SUB factor_booleano
        factor_booleano_id : factor_booleano
                           | SUB ID
                           | ID
        '''
        pseudoAsm = ''
        reg1 = self.get_next_register()
        reg2 = self.get_next_register()
        if len(p) == 4 and p[1] == '(':
            p[0] = p[2]
        elif p[1] == 'VERO':
            pseudoAsm += f'LOAD {reg1} 1\n'
            p[0] = pseudoAsm
        elif p[1] == 'FALSO':
            pseudoAsm += f'LOAD {reg1} 0\n'
            p[0] = pseudoAsm
        elif len(p) == 3 and p[1] == '-':
            pseudoAsm += p[2] if p[2] is not None else ''
            pseudoAsm += f'LOAD {reg2} 1\n'
            pseudoAsm += f'XOR {reg1} {reg2}\n'
            p[0] = pseudoAsm
        elif len(p) == 2 and p[1] not in ('VERO', 'FALSO', '-'):
            if isinstance(p[1], str) and self.lookUpTable.get(p[1]) is not None:
                pseudoAsm += f'LOADDISK {reg1} {self.lookUpTable[p[1]][1]}\n'
                p[0] = pseudoAsm
            else:
                p[0] = p[1]
        elif len(p) == 3 and p[1] == '-' and self.lookUpTable.get(p[2]) is not None:
            if self.lookUpTable.get(p[2]) is None:
                print(f'ERROR: Variable {p[2]} no inicializada')
                p[0] = ''
            else:
                pseudoAsm += f'LOADDISK {reg1} {self.lookUpTable[p[2]][1]}\n'
                pseudoAsm += f'LOAD {reg2} 1\n'
                pseudoAsm += f'XOR {reg1} {reg2}\n'
                p[0] = pseudoAsm
        elif len(p) == 2 and isinstance(p[1], str):
            if self.lookUpTable.get(p[1]) is None:
                print(f'ERROR: Variable {p[1]} no inicializada')
                p[0] = ''
            else:
                pseudoAsm += f'LOADDISK {reg1} {self.lookUpTable[p[1]][1]}\n'
                p[0] = pseudoAsm

    # TÉRMINO BOOLEANO
    def p_termino_booleano(self, p):
        '''
        termino_booleano : PL termino_booleano PR
                         | SUB termino_booleano
                         | termino_booleano E termino_booleano
                         | termino_booleano O termino_booleano
                         | factor_booleano
        '''
        pseudoAsm = ''
        reg1 = self.get_next_register()
        reg2 = self.get_next_register()
        if p[1] == '(':
            p[0] = p[2]
            return
        if p[1] == '-':
            pseudoAsm += p[2] if p[2] is not None else ''
            pseudoAsm += f'LOAD {reg2} 1\n'
            pseudoAsm += f'XOR {reg1} {reg2}\n'
            p[0] = pseudoAsm
            return
        if len(p) == 2:
            p[0] = p[1]
            return
        if len(p) == 4:
            pseudoAsm += p[1] if p[1] is not None else ''
            pseudoAsm += p[3] if p[3] is not None else ''
            if p[2] == 'e':
                pseudoAsm += f'AND {reg1} {reg2}\n'
            elif p[2] == 'o':
                pseudoAsm += f'OR {reg1} {reg2}\n'
            p[0] = pseudoAsm

    # EXPRESIÓN BOOLEANA
    def p_exp_booleana(self, p):
      '''
      exp_booleana : termino_booleano
                  | exp_booleana E termino_booleano
                  | exp_booleana O termino_booleano
      '''
      pseudoAsm = ''
      if len(p) == 2:
          p[0] = p[1]
          return
      if len(p) == 4:
          if p[2] == 'e':  # AND
              etiqueta_falso = f'jmp_and_{self.countJumps}'
              self.countJumps += 1
              pseudoAsm += p[1] if p[1] is not None else ''  # Primera condición
              pseudoAsm += f'JNE {etiqueta_falso}\n'  # Si falsa, salta
              pseudoAsm += p[3] if p[3] is not None else ''  # Segunda condición
              pseudoAsm += f'JNE {etiqueta_falso}\n'  # Si segunda falsa, salta
              pseudoAsm += f'{etiqueta_falso}:\n'  # Etiqueta después de evaluar
          elif p[2] == 'o':  # OR
              etiqueta_verdadero = f'jmp_or_{self.countJumps}'
              self.countJumps += 1
              pseudoAsm += p[1] if p[1] is not None else ''
              pseudoAsm += f'JEQ {etiqueta_verdadero}\n'
              pseudoAsm += p[3] if p[3] is not None else ''
              pseudoAsm += f'JEQ {etiqueta_verdadero}\n'
              pseudoAsm += f'{etiqueta_verdadero}:\n'
      p[0] = pseudoAsm

    # SENTENCIA SI
    def p_sentencia_si(self, p):
      '''
      sentencia_si : SE exp_booleana CL proposiciones CR ALTRIMENTI CL proposiciones CR
                  | SE exp_booleana CL proposiciones CR
      '''
      pseudoAsm = ''
      if len(p) == 10:
          etiqueta_else = f'jmp{self.countJumps}'
          self.countJumps += 1
          etiqueta_fin = f'jmp{self.countJumps}'
          self.countJumps += 1
          pseudoAsm += p[2] if p[2] is not None else ''  # exp_booleana con 'E'
          pseudoAsm += f'JNE {etiqueta_else}\n'
          pseudoAsm += p[4] if p[4] is not None else ''
          pseudoAsm += f'JUMP {etiqueta_fin}\n'
          pseudoAsm += f'{etiqueta_else}:\n'
          pseudoAsm += p[8] if p[8] is not None else ''
          pseudoAsm += f'{etiqueta_fin}:\n'
      elif len(p) == 6:
          etiqueta_fin = f'jmp{self.countJumps}'
          self.countJumps += 1
          pseudoAsm += p[2] if p[2] is not None else ''
          pseudoAsm += f'JNE {etiqueta_fin}\n'
          pseudoAsm += p[4] if p[4] is not None else ''
          pseudoAsm += f'{etiqueta_fin}:\n'
      p[0] = pseudoAsm

    # SENTENCIA MIENTRAS
    def p_sentencia_mientras(self, p):
        '''
        sentencia_mientras : MENTRE exp_booleana CL proposiciones CR
        '''
        pseudoAsm = ''
        etiqueta_inicio = f'jmp{self.countJumps}'
        self.countJumps += 1
        etiqueta_fin = f'jmp{self.countJumps}'
        self.countJumps += 1
        pseudoAsm += f'{etiqueta_inicio}:\n'  # Aseguramos que la etiqueta esté al inicio
        pseudoAsm += p[2] if p[2] is not None else ''
        pseudoAsm += f'JNE {etiqueta_fin}\n'
        pseudoAsm += p[4] if p[4] is not None else ''
        pseudoAsm += f'JUMP {etiqueta_inicio}\n'
        pseudoAsm += f'{etiqueta_fin}:\n'
        p[0] = pseudoAsm

    # SENTENCIA HACER MIENTRAS
    def p_sentencia_hacer_mientras(self, p):
        '''
        sentencia_hacer_mientras : CL proposiciones MENTRE exp_booleana CR
        '''
        pseudoAsm = ''
        etiqueta_inicio = f'jmp{self.countJumps}'
        self.countJumps += 1
        pseudoAsm += p[2] if p[2] is not None else ''  # Ejecuta las proposiciones primero
        pseudoAsm += f'{etiqueta_inicio}:\n'  # Luego inicia el bucle
        pseudoAsm += p[4] if p[4] is not None else ''  # Condición
        pseudoAsm += f'JNE {etiqueta_inicio}\n'
        p[0] = pseudoAsm

    # SENTENCIA LEER
    def p_sentencia_leer(self, p):
        '''
        sentencia_leer : LEGGERE PL ID PR SC
        '''
        pseudoAsm = ''
        reg = self.get_next_register()
        if self.lookUpTable.get(p[3]) is None:
            print(f'ERROR: Variable {p[3]} no inicializada siendo leída')
        else:
            pseudoAsm += f'INPUT {reg}\n'
            pseudoAsm += f'STORE {self.lookUpTable[p[3]][1]} {reg}\n'
        p[0] = pseudoAsm

    # SENTENCIA ESCRIBIR
    def p_sentencia_escribir(self, p):
        '''
        sentencia_escribir : SCRIVERE PL STRING PR SC
                           | SCRIVERE PL ID PR SC
        '''
        pseudoAsm = ''
        reg = self.get_next_register()
        if p[3] in self.lexerLookUpTable and self.lexerLookUpTable[p[3]] == 'STRING':
            valorCadena = str(p[3]).replace('"', '')
            for i, char in enumerate(valorCadena):
                pseudoAsm += f'LOAD {reg} {ord(char)}\n'
                pseudoAsm += f'OUTPUT_CHAR {reg}\n'
        elif self.lookUpTable.get(p[3]) is None:
            print(f'ERROR: Variable {p[3]} no inicializada siendo leída')
        else:
            if self.lookUpTable[p[3]][0] == 'cadena':
                for i in range(len(self.lookUpTable[p[3]][0])):
                    pseudoAsm += f'LOADDISK {reg} {self.lookUpTable[p[3]][1] + i}\n'
                    pseudoAsm += f'OUTPUT_CHAR {reg}\n'
            else:
                pseudoAsm += f'LOADDISK {reg} {self.lookUpTable[p[3]][1]}\n'
                pseudoAsm += f'OUTPUT {reg}\n'
        p[0] = pseudoAsm

    # LLAMADA A MÓDULO
    def p_llamada_modulo(self, p):
      '''
      llamada_modulo : ID PL ID PR
                    | ID PL NUMBER PR
      '''
      modulo = p[1]
      pseudoAsm = ''
      self.reset_registers()

      if len(p) == 5:
          argumento = p[3]
          return_label = f'jmp_ret_{self.countJumps}'
          self.countJumps += 1

          if isinstance(argumento, str) and argumento in self.lookUpTable:
              direccion_arg = self.lookUpTable[argumento][1]
              pseudoAsm += f'LOADDISK 28 {direccion_arg}\n'
          else:
              pseudoAsm += f'LOAD 28 {argumento}\n'

          pseudoAsm += f'JUMP {modulo}\n'
          pseudoAsm += f'{return_label}:\n'

      for libreria, modulos in self.librerias_cargadas.items():
          if modulo in modulos and modulo not in self.jumpTable:
              self.jumpTable[modulo] = True
              if modulo == 'pow':
                  modulo_code = '''
                  STORE 0 28
                  LOADDISK 6 0
                  MULT 6 6
                  STORE 2 6
                  LOADDISK 28 2
                  '''
              elif modulo == 'fact':
                  modulo_code = '''
                  STORE 0 28
                  LOADDISK 6 0
                  LOAD 31 1
                  LOAD 7 1
                  CMP 6 0
                  JEQ STOP_FACT
                  JUMP LOOP_FACT
                  LOOP_FACT:
                  CMP 6 0
                  JEQ STOP_FACT
                  MULT 7 6
                  SUB 6 31
                  JUMP LOOP_FACT
                  STOP_FACT:
                  STORE 2 7
                  LOADDISK 28 2
                  '''
              else:
                  modulo_code = self.librerias_cargadas[libreria][modulo].strip()
              modulo_code = '\n'.join(line.lstrip() for line in modulo_code.splitlines() if line.strip())
              if not modulo_code.endswith('JUMP'):
                  modulo_code += f'\nJUMP {return_label}'
              self.module_code += f"{modulo}:\n{modulo_code}\n"

      p[0] = (pseudoAsm, 'module_call')

    def cargar_libreria(self, nombre):
        try:
            nombre = nombre.strip()
            if not os.path.exists(nombre):
                nombre += ".txt"
            with open(self.librariesRuta, 'r') as f:
                contenido = f.read()
                modulos = {}
                actual = None
                for linea in contenido.splitlines():
                    linea = linea.strip()
                    if linea.startswith('[') and linea.endswith(']'):
                        actual = linea[1:-1]
                        modulos[actual] = ""
                    elif actual:
                        modulos[actual] += linea + "\n"
                self.librerias_cargadas[nombre] = modulos
        except FileNotFoundError:
            print(f"Error: No se encontró la librería {nombre}")

    def p_error(self, p):
        if p:
            print(f"ERROR SINTÁCTICO: Token inesperado '{p.value}' (tipo: {p.type}) en línea {p.lineno}, posición {p.lexpos}")
            self.parser.errok()
        else:
            print("ERROR SINTÁCTICO: Fin de archivo inesperado")

    def build(self, **kwargs):
        self.parser = yacc.yacc(module=self, write_tables=0, debug=True, debugfile='parser.out', **kwargs)

    def test(self, data):
        try:
            self.parser.parse(data, lexer=self.lexer)
            if self.resultAsm:
                print("Assembler generado (self.resultAsm):")
                print(self.resultAsm)
            else:
                print("No assembler generated, self.resultAsm is empty")
            return self.resultAsm
        except Exception as e:
            print(f"ERROR DURANTE EL ANÁLISIS: {str(e)}")
            return None
