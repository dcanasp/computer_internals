from gui.main_window import Ui_MainWindow  # Importamos la clase generada
from PySide6.QtGui import QTextCursor  # Importa QTextCursor
from PySide6.QtWidgets import QApplication, QMainWindow
import sys
import os
import subprocess
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

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

    def connect_buttons(self):
        """Conectar señales de los botones a sus funciones"""
        # Botones de procesamiento
        self.button_preprocessor.clicked.connect(self.preprocesar_clicked)
        self.button_compiler.clicked.connect(self.compilar_clicked)
        self.button_assembler.clicked.connect(self.ensamblar_clicked)
        self.button_linker.clicked.connect(self.enlazar_clicked)

        # Botones de control de ejecución
        self.button_siguiente_instruccion.clicked.connect(
            self.siguiente_instruccion_clicked)
        self.button_ultima_instruccion.clicked.connect(
            self.ultima_instruccion_clicked)
        self.button_reiniciar.clicked.connect(self.reiniciar_clicked)

        # Botones de carga de ejemplos
        self.button_cargar_ex1.clicked.connect(lambda: self.cargar_ejemplo(1))
        self.button_cargar_ex2.clicked.connect(lambda: self.cargar_ejemplo(2))
        self.button_cargar_ex3.clicked.connect(lambda: self.cargar_ejemplo(3))

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
        libraries_output_path = os.path.join(temp_folder, "temp_libraries_output.txt")
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
            self.textEditCodigoFuenteModificado.setPlainText(preprocessed_code)  # Código modificado
            self.textEditCodigoLib.setPlainText(libraries_code)  # Código de librerías

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
        print("¡Ensamblando código!")
        # Obtener texto del campo de código assembler
        codigo = self.textEditCodigoASM.toPlainText()
        print(f"Código a ensamblar:\n{codigo}")

        # Activar el botón de enlazar después de ensamblar
        self.button_linker.setEnabled(True)

    def enlazar_clicked(self):
        """Manejador del botón Enlazar/Cargar"""
        posicion = self.spinBox_pos_enlazar.value()  # Obtener valor del spinBox
        print(f"Enlazando en posición: {posicion}")
        # Obtener texto del campo de código relocalizable
        codigo = self.textEditCodigoReloc.toPlainText()
        print(f"Código a enlazar:\n{codigo}")
        self.button_siguiente_instruccion.setEnabled(True)
        self.button_ultima_instruccion.setEnabled(True) 

    def siguiente_instruccion_clicked(self):
        """Manejador del botón Siguiente Instrucción"""
        print("Ejecutando siguiente instrucción...")

    def ultima_instruccion_clicked(self):
        """Manejador del botón Saltar al Final"""
        print("Saltando a la última instrucción...")

    def reiniciar_clicked(self):
        """Manejador del botón Reiniciar"""
        print("Reiniciando sistema...")
        # Limpiar campos de texto
        self.textEditCodigoFuente.clear()
        self.textEditCodigoFuenteModificado.clear()
        self.textEditCodigoASM.clear()
        self.textEditCodigoReloc.clear()
        self.textEditCodigoLib.clear()
        self.textEditPCOutput.clear()

        # Desactivar botones de procesamiento
        self.disable_buttons()

    def cargar_ejemplo(self, ejemplo_num):
        """Cargar un ejemplo desde la carpeta examples"""

        self.reiniciar_clicked()
        base = get_project_root()
        ejemplo_path = os.path.join(base, "examples", f"example{ejemplo_num}.txt")
        
        if not os.path.exists(ejemplo_path):
            print(f"❌ Error: No se encontró el archivo de ejemplo {ejemplo_num}.")
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