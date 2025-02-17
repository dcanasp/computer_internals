from PySide6.QtWidgets import QTableWidgetItem, QMessageBox
from gui.main_window import Ui_MainWindow  # Importamos la clase generada
from PySide6.QtGui import QTextCursor  # Importa QTextCursor
from PySide6.QtWidgets import QApplication, QMainWindow
import sys
import os
import subprocess
import json

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Mapa de instrucciones
instruction_map = {
    0: "BEGIN",
    31: "END",
    30: "FIN",
    1: "LOAD",
    2: "STORE",
    3: "MOVE",
    4: "LOADDISK",
    5: "ADD",
    6: "SUB",
    7: "MULT",
    8: "DIV",
    9: "MOD",
    10: "AND",
    11: "OR",
    12: "XOR",
    13: "STOREREG",
    14: "LEFSHIFT",
    15: "RIGHTSHIF",
    16: "CMP",
    17: "CMPREG",
    18: "JUMP",
    19: "JEQ",
    20: "JNE",
    21: "CMPG",
    22: "CMPL",
    23: "CMPGE",
    24: "CMPLE",
    25: "CMPGREG",
    26: "CMPLREG",
    27: "CMPGEREG",
    28: "CMPLEREG",
    29: "LOADDISKREG"
}

def get_project_root():
    # Si se compiló (por ejemplo, con PyInstaller), sys.frozen es True.
    if getattr(sys, 'frozen', False):
        # Si está compilado, la ruta del ejecutable está en dist
        return os.path.abspath(os.path.join(os.path.dirname(sys.executable), ".."))
    else:
        # Si no está compilado, la ruta base sería el directorio de main.py
        return os.path.abspath(os.path.dirname(__file__))


class MainApp(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Configura la interfaz
        self.connect_buttons()  # Conecta los botones
        self.setup_console()  # Configura la consola de salida
        self.setup_styles()  # Configura los estilos
        self.disable_buttons()  # Desactiva los botones al inicio

        # Inicializar memoria y registros
        self.inicializar_memoria_y_registros()

        # Inicializar índice de instrucción
        self.instruction_index = 0
        self.iter_pc_data = []

    def connect_buttons(self):
        """Conectar señales de los botones a sus funciones"""
        # Botones de procesamiento
        self.button_preprocessor.clicked.connect(self.preprocesar_clicked)
        self.button_compiler.clicked.connect(self.compilar_clicked)
        self.button_assembler.clicked.connect(self.ensamblar_clicked)
        self.button_linker.clicked.connect(self.enlazar_clicked)

        # Botones de control de ejecución
        self.button_siguiente_instruccion.clicked.connect(self.siguiente_instruccion_clicked)
        self.button_ultima_instruccion.clicked.connect(self.ultima_instruccion_clicked)
        self.button_reiniciar.clicked.connect(self.reiniciar_clicked)

        # Botones de carga de ejemplos
        self.button_cargar_ex1.clicked.connect(lambda: self.cargar_ejemplo(1))
        self.button_cargar_ex2.clicked.connect(lambda: self.cargar_ejemplo(2))
        self.button_cargar_ex3.clicked.connect(lambda: self.cargar_ejemplo(3))

        # Botones de conversión de RAM
        self.button_sel_ram2bin.clicked.connect(self.convert_ram_to_bin)
        self.button_sel_ram2dec.clicked.connect(self.convert_ram_to_dec)
        self.button_sel_ram2ascii.clicked.connect(self.convert_ram_to_ascii)

        # Botones de conversión de registros
        self.button_sel_reg2bin.clicked.connect(self.convert_reg_to_bin)
        self.button_sel_reg2dec.clicked.connect(self.convert_reg_to_dec)
        self.button_sel_reg2ascii.clicked.connect(self.convert_reg_to_ascii)

    def setup_console(self):
        """Redirige los prints a la consola de salida (textEditPCOutput)"""
        import sys
        from io import StringIO

        class ConsoleOutput(StringIO):
            def __init__(self, text_edit):
                super().__init__()
                self.text_edit = text_edit

            def write(self, text):
                # Mueve el cursor al final
                self.text_edit.moveCursor(QTextCursor.MoveOperation.End)
                self.text_edit.insertPlainText(text)  # Inserta el texto

        # Redirige sys.stdout a la consola de salida
        sys.stdout = ConsoleOutput(self.textEditPCOutput)

    def setup_styles(self):
        """Configura los estilos de los botones"""
        self.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border-radius: 5px;
                padding: 8px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:disabled {
                background-color: #cccccc;
                color: #666666;
            }
        """)

    def disable_buttons(self):
        """Desactiva los botones de procesamiento al inicio"""
        return
        self.button_preprocessor.setEnabled(True)
        self.button_verTablaSimbolos.setEnabled(False)
        self.button_compiler.setEnabled(False)
        self.button_assembler.setEnabled(False)
        self.button_linker.setEnabled(False)
        self.button_siguiente_instruccion.setEnabled(False)
        self.button_ultima_instruccion.setEnabled(False)

    def preprocesar_clicked(self):
        """Manejador del botón Preprocesar"""
        codigo = self.textEditCodigoFuente.toPlainText().strip()
        if not codigo:
            print("❌ Error: El campo de código fuente está vacío.")
            return

        base = get_project_root()
        print(base)

        temp_folder = os.path.join(base, "_temp")
        input_path = os.path.join(temp_folder, "temp_preprocessor_input.txt")
        output_path = os.path.join(temp_folder, "temp_preprocessor_output.txt")
        libraries_output_path = os.path.join(
            temp_folder, "temp_libraries_output.txt")
        exec_path = os.path.join(base, "execs", "preprocessor")
        libs_path = os.path.join(base, "libs")

        if not libs_path.endswith(os.sep):
            libs_path += os.sep

        os.makedirs(temp_folder, exist_ok=True)
        with open(input_path, "w", encoding="utf-8") as f:
            f.write(codigo)

        try:
            subprocess.run(
                [exec_path, input_path, libs_path, output_path, libraries_output_path], check=True, text=True
            )

            # Leer el archivo de salida del preprocesador
            preprocessed_code = ""
            if os.path.exists(output_path):
                with open(output_path, "r", encoding="utf-8") as f:
                    preprocessed_code = f.read()

            # Leer el archivo de salida de las librerías
            libraries_code = ""
            if os.path.exists(libraries_output_path):
                with open(libraries_output_path, "r", encoding="utf-8") as f:
                    libraries_code = f.read()

            # Actualizar la interfaz con los resultados
            self.textEditCodigoFuenteModificado.setPlainText(
                preprocessed_code)  # Código modificado
            self.textEditCodigoLib.setPlainText(
                libraries_code)  # Código de librerías

            # Activar el botón de compilar después de preprocesar
            self.button_compiler.setEnabled(True)
            print("✅ Preprocesamiento completado.")

        except subprocess.CalledProcessError as e:
            print(f"❌ Error al ejecutar el preprocesador: {e}")

    def compilar_clicked(self):
        """Manejador del botón Compilar"""
        print("¡Compilando código!")
        # Obtener texto del campo de código
        codigo = self.textEditCodigoFuenteModificado.toPlainText()
        print(f"Código a compilar:\n{codigo}")

        # Activar el botón de ensamblar después de compilar
        self.button_assembler.setEnabled(True)
        self.button_verTablaSimbolos.setEnabled(True)

    def ensamblar_clicked(self):
        """Manejador del botón Ensamblar"""
        codigo = self.textEditCodigoASM.toPlainText().strip()
        if not codigo:
            print("❌ Error: El código assembler está vacío.")
            return

        base = get_project_root()
        temp_folder = os.path.join(base, "_temp")
        input_path = os.path.join(temp_folder, "temp_assembler_input.txt")
        output_path = os.path.join(temp_folder, "temp_assembler_output.txt")
        exec_path = os.path.join(base, "execs", "assembler")

        os.makedirs(temp_folder, exist_ok=True)

        # Guardar el código assembler en un archivo temporal
        with open(input_path, "w", encoding="utf-8") as f:
            f.write(codigo)

        try:
            subprocess.run(
                [exec_path, input_path, output_path],
                check=True,
                text=True
            )

            # Leer el archivo de salida del ensamblador
            assembled_code = ""
            if os.path.exists(output_path):
                with open(output_path, "r", encoding="utf-8") as f:
                    assembled_code = f.read()

            # Actualizar la interfaz con los resultados
            self.textEditCodigoReloc.setPlainText(
                assembled_code)  # Código relocalizable

            # Activar el botón de enlazar después de ensamblar
            self.button_linker.setEnabled(True)
            print("✅ Ensamblado completado.")

        except subprocess.CalledProcessError as e:
            print(f"❌ Error al ejecutar el ensamblador: {e}")

    def inicializar_memoria_y_registros(self):
        """Inicializa la RAM, registros de la ALU y unidad de control en cero"""
        self.tamano_ram = 8192  # Definir tamaño de la RAM
        self.ram = ["0"*32] * self.tamano_ram  # Memoria RAM vacía

        # Reflejar en la interfaz
        self.actualizar_tabla_ram()

    def actualizar_tabla_ram(self):
        """Actualiza la tabla de RAM en la interfaz gráfica"""
        self.table_ram.clearContents()
        for i, valor in enumerate(self.ram):
            item = QTableWidgetItem(valor)
            self.table_ram.setItem(i, 0, item)

    def enlazar_clicked(self):
        """Manejador del botón Enlazar/Cargar"""
        try:
            # Obtener parámetros clave
            base = get_project_root()
            offset = self.spinBox_pos_enlazar.value()

            # 1. Combinar código relocalizable principal y de librerías
            codigo_reloc = self.textEditCodigoReloc.toPlainText()
            codigo_lib = self.textEditCodigoLib.toPlainText()
            combined_code = codigo_reloc + "\n" + codigo_lib

            if not combined_code.strip():
                print("❌ Error: No hay código relocalizable para enlazar")
                return

            # 2. Guardar en archivo temporal combinado
            temp_folder = os.path.join(base, "_temp")
            input_path = os.path.join(temp_folder, "temp_linker_input.txt")
            output_path = os.path.join(temp_folder, "temp_linker_output.txt")
            exec_path = os.path.join(base, "execs", "linkerLoader")

            os.makedirs(temp_folder, exist_ok=True)

            with open(input_path, "w", encoding="utf-8") as f:
                f.write(combined_code)

            # 3. Ejecutar el linker-loader con offset
            try:
                result = subprocess.run(
                    [exec_path, input_path, output_path, str(offset)],
                    check=True,
                    text=True,
                    stderr=subprocess.PIPE  # Capturar stderr
                )
            except subprocess.CalledProcessError as e:
                # Obtener el código de error del linker
                error_code = int(e.stderr.strip()) if e.stderr else -1

                # Mostrar mensaje descriptivo basado en el código de error
                if error_code == 1:
                    print("❌ Error: Overflow de la RAM (límite: 8192)")
                elif error_code == 2:
                    print("❌ Error: Overflow en el número de etiquetas (límite: 100)")
                elif error_code == 3:
                    print("❌ Error: No se pudo abrir el archivo de entrada")
                elif error_code == 4:
                    print("❌ Error: No se pudo crear el archivo de salida")
                else:
                    print(f"❌ Error en el linker: {e.stderr.strip()}")
                return

            # 4. Leer el binario generado
            if not os.path.exists(output_path):
                print("❌ Error: No se generó archivo de salida")
                return

            with open(output_path, "r", encoding="utf-8") as f:
                binario = [line.strip() for line in f if line.strip()]

            if not binario:
                print("❌ Error: La salida del linker está vacía")
                return

            # 6. Verificar colisiones en la RAM
            for i in range(len(binario)):
                if self.ram[offset + i] != ("0" * 32):
                    print(
                        f"❌ Error: Colisión en la RAM en la dirección {offset + i}")
                    return

            # 8. Habilitar botones de ejecución
            self.button_siguiente_instruccion.setEnabled(True)
            self.button_ultima_instruccion.setEnabled(True)

            print(
                f"✅ Enlazado completado.")

            # 9. Ejecutar el computador
            computer_exec_path = os.path.join(base, "execs", "computer.exe")
            try:
                subprocess.run(
                    [computer_exec_path, output_path, str(offset)],
                    check=True,
                    text=True,
                    stderr=subprocess.PIPE  # Capturar stderr
                )
                print("✅ Computador ejecutado correctamente.")
            except subprocess.CalledProcessError as e:
                print(f"❌ Error al ejecutar el computador: {e.stderr.strip()}")
                return

            # 10. Leer el archivo iterPc.json generado por el computador
            iter_pc_path = os.path.join(base, "execs",  "iterPc.json")
            if not os.path.exists(iter_pc_path):
                print("❌ Error: No se generó el archivo iterPc.json")
                return

            with open(iter_pc_path, "r", encoding="utf-8") as f:
                self.iter_pc_data = json.load(f)

            # Inicializar el índice de instrucción
            self.instruction_index = 0

        except Exception as e:
            print(f"❌ Error inesperado: {str(e)}")
    def siguiente_instruccion_clicked(self):
        """Manejador del botón Siguiente Instrucción"""
        if not self.iter_pc_data:
            print("❌ Error: No hay datos de iteración cargados.")
            return

        if self.instruction_index >= len(self.iter_pc_data):
            print("❌ Error: No hay más instrucciones para ejecutar.")
            return

        # Obtener la instrucción actual
        current_instruction = self.iter_pc_data[self.instruction_index]

        # Actualizar los campos de texto
        self.textEditCurrentInstruction.setPlainText(instruction_map.get(current_instruction["instruction"], "UNKNOWN"))
        self.textEditArg1.setPlainText(str(current_instruction["input1"]))
        self.textEditArg2.setPlainText(str(current_instruction["input2"] * current_instruction["sign"]))
        self.textEdit_ProgramCounter.setPlainText(str(current_instruction["PC"]))

        # Actualizar los registros
        for i in range(4):
            self.table_registros.setItem(i, 0, QTableWidgetItem(str(current_instruction["registros"][i])))
        for i in range(4, 32):
            self.table_alu.setItem(i - 4, 0, QTableWidgetItem(str(current_instruction["registros"][i])))

        # Actualizar la RAM
        for i, valor in enumerate(current_instruction["memoria"]):
            # Convertir el valor de decimal a binario de 32 bits
            binario = format(valor, '032b')
            self.ram[i] = binario
            item = QTableWidgetItem(binario)
            self.table_ram.setItem(i, 0, item)

        # Seleccionar la instrucción actual en la RAM
        pc_value = current_instruction["PC"]
        self.table_ram.selectRow(pc_value)

        # Incrementar el índice de instrucción
        self.instruction_index += 1

    def ultima_instruccion_clicked(self):
        """Manejador del botón Saltar al Final"""
        if not self.iter_pc_data:
            print("❌ Error: No hay datos de iteración cargados.")
            return

        # Ejecutar todas las instrucciones restantes
        while self.instruction_index < len(self.iter_pc_data)-1:
            self.siguiente_instruccion_clicked()

    def convert_ram_to_bin(self):
        """Reinicia la RAM cargando nuevamente la memoria del JSON de la instrucción actual"""
        if not self.iter_pc_data or self.instruction_index >= len(self.iter_pc_data):
            print("❌ Error: No hay datos de iteración cargados o el índice de instrucción es inválido.")
            return

        # Obtener la instrucción actual
        current_instruction = self.iter_pc_data[self.instruction_index]

        # Actualizar la RAM
        for i, valor in enumerate(current_instruction["memoria"]):
            # Convertir el valor de decimal a binario de 32 bits
            binario = format(valor, '032b')
            self.ram[i] = binario
            item = QTableWidgetItem(binario)
            self.table_ram.setItem(i, 0, item)

        print("✅ RAM reiniciada correctamente.")

    def convert_ram_to_dec(self):
        """Convierte el contenido de las celdas seleccionadas de la RAM a decimal"""
        selected_items = self.table_ram.selectedItems()
        for item in selected_items:
            value = item.text()
            if len(value) == 32 and all(c in '01' for c in value):  # Check if the value is a 32-bit binary string
                dec_value = str(int(value, 2))
                item.setText(dec_value)
            else:
                QMessageBox.critical(self, "Error", "La celda no contiene un valor binario de 32 bits.")

    def convert_ram_to_ascii(self):
        """Convierte el contenido de las celdas seleccionadas de la RAM a ASCII"""
        selected_items = self.table_ram.selectedItems()
        for item in selected_items:
            value = item.text()
            if len(value) == 32 and all(c in '01' for c in value):  # Check if the value is a 32-bit binary string
                ascii_value = ''.join(chr(int(value[i:i+8], 2)) for i in range(0, len(value), 8))
                item.setText(ascii_value)
            else:
                QMessageBox.critical(self, "Error", "La celda no contiene un valor binario de 32 bits.")

    def convert_reg_to_bin(self):
        """Convierte el contenido de los registros seleccionados a binario"""
        selected_items = self.table_registros.selectedItems() + self.table_alu.selectedItems()
        for item in selected_items:
            value = item.text()
            if value.isdigit():
                bin_value = format(int(value), '032b')
                item.setText(bin_value)
            else:
                QMessageBox.critical(self, "Error", "El valor del registro no es un número decimal.")

    def convert_reg_to_dec(self):
        """Reinicia los registros cargando nuevamente los valores del JSON de la instrucción actual"""
        if not self.iter_pc_data or self.instruction_index >= len(self.iter_pc_data):
            print("❌ Error: No hay datos de iteración cargados o el índice de instrucción es inválido.")
            return

        # Obtener la instrucción actual
        current_instruction = self.iter_pc_data[self.instruction_index]

        # Actualizar los registros
        for i in range(4):
            self.table_registros.setItem(i, 0, QTableWidgetItem(str(current_instruction["registros"][i])))
        for i in range(4, 32):
            self.table_alu.setItem(i - 4, 0, QTableWidgetItem(str(current_instruction["registros"][i])))

        print("✅ Registros reiniciados correctamente.")

    def convert_reg_to_ascii(self):
        """Convierte el contenido de los registros seleccionados a ASCII"""
        selected_items = self.table_registros.selectedItems() + self.table_alu.selectedItems()
        for item in selected_items:
            value = item.text()
            if all(c in '01' for c in value):  # Check if the value is binary
                ascii_value = ''.join(chr(int(value[i:i+8], 2)) for i in range(0, len(value), 8))
                item.setText(ascii_value)
            else:
                QMessageBox.critical(self, "Error", "El valor del registro no es un número binario.")

    def reiniciar_clicked(self):
        """Reinicia el sistema, limpiando memoria y registros"""

        # Limpiar campos de texto
        self.textEditCodigoFuente.clear()
        self.textEditCodigoFuenteModificado.clear()
        self.textEditCodigoASM.clear()
        self.textEditCodigoReloc.clear()
        self.textEditCodigoLib.clear()
        self.textEditPCOutput.clear()

        # Reestablecer memoria y registros
        self.inicializar_memoria_y_registros()

        # Inicializar índice de instrucción
        self.instruction_index = 0
        self.iter_pc_data = []

        # Desactivar botones de procesamiento
        self.disable_buttons()
        print("✅ Sistema reiniciado correctamente.")

    def cargar_ejemplo(self, ejemplo_num):
        """Cargar un ejemplo desde la carpeta examples"""

        self.reiniciar_clicked()
        base = get_project_root()
        ejemplo_path = os.path.join(
            base, "examples", f"example{ejemplo_num}.txt")

        if not os.path.exists(ejemplo_path):
            print(
                f"❌ Error: No se encontró el archivo de ejemplo {ejemplo_num}.")
            return

        try:
            with open(ejemplo_path, "r", encoding="utf-8") as f:
                codigo = f.read()
                self.textEditCodigoFuente.setPlainText(codigo)
                print(f"✅ Ejemplo {ejemplo_num} cargado correctamente.")

                # Activar el botón de preprocesar después de cargar el ejemplo
                self.button_preprocessor.setEnabled(True)

        except Exception as e:
            print(f"❌ Error al cargar el ejemplo {ejemplo_num}: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())
