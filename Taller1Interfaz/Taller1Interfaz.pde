import g4p_controls.*;
import javax.swing.JFileChooser;
import java.io.*;
import java.awt.Toolkit;
import java.awt.datatransfer.StringSelection;

// Campos de texto para entrada/salida de módulos
GTextArea preprocessorInput, preprocessorOutput, lexicalOutput;
GTextArea assemblerInput, assemblerOutput, linkerOutput;

GButton copyPreprocessorInputButton, copyAssemblerInputButton, copyPreprocessorOutputButton, 
        copyLexicalOutputButton, copyAssemblerOutputButton, copyLinkerOutputButton;

GButton runPreprocessorButton, runLexicalAnalyzerButton, runAssemblerButton, runLinkerButton;

// Botones auxiliares
GButton clearAllButton, loadExample1Button, loadExample2Button, loadExample3Button;
GButton uploadPreprocessorButton, uploadAssemblerButton;

GButton toggleInfoButton;
boolean showInfo = false;

// Estado del sistema
String status = "Todo listo!";

String basePath;
String examplesPath;
String tempPath;
String libsPath;

void setup() {
  size(1600, 900); // Tamaño para mayor espacio vertical
  textSize(16);
  
  // Directorio base
  basePath = sketchPath("data");
  examplesPath = basePath + "/Examples/";
  tempPath = basePath + "/temp/";
  libsPath = basePath + "/Libs/";

  // *** Sección Superior: Preprocessor y Lexical Analyzer ***
  preprocessorInput = createTextArea(50, 100, 450, 200, "Preprocessor Input", true);
  preprocessorOutput = createTextArea(550, 100, 450, 200, "Preprocessor Output", false);
  lexicalOutput = createTextArea(1050, 100, 450, 200, "Lexical Output", false);

  runPreprocessorButton = createButton("Run Preprocessor", 50, 310, "runPreprocessor");
  runLexicalAnalyzerButton = createButton("Run Lexical Analyzer", 550, 310, "runLexicalAnalyzer");

  // *** Sección Inferior: Assembler y Linker ***
  assemblerInput = createTextArea(50, 500, 450, 200, "Assembler Input", true);
  assemblerOutput = createTextArea(550, 500, 450, 200, "Assembler Output", false);
  linkerOutput = createTextArea(1050, 500, 450, 200, "Linker Output", false);

  runAssemblerButton = createButton("Run Assembler", 50, 710, "runAssembler");
  runLinkerButton = createButton("Run Linker", 550, 710, "runLinker");

  // *** Botones inferiores ***
  loadExample1Button = createSquareButton("Ex1", 1000, 820, "loadExample1");
  loadExample2Button = createSquareButton("Ex2", 1100, 820, "loadExample2");
  loadExample3Button = createSquareButton("Ex3", 1200, 820, "loadExample3");
  clearAllButton = createSquareButton("Clear", 1300, 820, "clearAll");
  toggleInfoButton = createSquareButton("Info", 1400, 820, "toggleInfo");

}

GTextArea createTextArea(int x, int y, int width, int height, String label, boolean hasUploadButton) {
  GTextArea textArea = new GTextArea(this, x, y, width, height);
  textArea.setOpaque(true);
  textArea.setLocalColorScheme(GCScheme.BLUE_SCHEME);
  textArea.setText(""); // Inicialmente vacío

  // Crear botón de carga dentro del cuadro si aplica
  if (hasUploadButton) {
    GButton uploadButton = new GButton(this, x + width - 40, y + 10, 30, 30);
    uploadButton.setText(""); // Deja vacío el texto del botón
    uploadButton.setIcon("./Icons/folder.png", 1, GAlign.CENTER, GAlign.CENTER); // Ícono centrado
    uploadButton.setLocalColorScheme(GCScheme.ORANGE_SCHEME);
    uploadButton.addEventHandler(this, "uploadFileToField");

    // Asociar el botón a la entrada correspondiente
    if (label.equals("Preprocessor Input")) {
      uploadPreprocessorButton = uploadButton;
    } else if (label.equals("Assembler Input")) {
      uploadAssemblerButton = uploadButton;
    }
  }

  // Crear botón de copiar
  GButton copyButton = new GButton(this, x + width - 40, y + height - 40, 30, 30);
  copyButton.setText(""); // Deja vacío el texto del botón
  copyButton.setIcon("./Icons/copy.png", 1, GAlign.CENTER, GAlign.CENTER); // Ícono de copiar
  copyButton.setLocalColorScheme(GCScheme.GREEN_SCHEME);

  // Asociar el botón de copiar con el área correspondiente
  if (label.equals("Preprocessor Input")) {
    copyPreprocessorInputButton = copyButton;
    copyButton.addEventHandler(this, "copyToClipboardPreprocessor");
  } else if (label.equals("Assembler Input")) {
    copyAssemblerInputButton = copyButton;
    copyButton.addEventHandler(this, "copyToClipboardAssembler");
  } else if (label.equals("Preprocessor Output")) {
    copyPreprocessorOutputButton = copyButton;
    copyButton.addEventHandler(this, "copyToClipboardPreprocessorOutput");
  } else if (label.equals("Lexical Output")) {
    copyLexicalOutputButton = copyButton;
    copyButton.addEventHandler(this, "copyToClipboardLexicalOutput");
  } else if (label.equals("Assembler Output")) {
    copyAssemblerOutputButton = copyButton;
    copyButton.addEventHandler(this, "copyToClipboardAssemblerOutput");
  } else if (label.equals("Linker Output")) {
    copyLinkerOutputButton = copyButton;
    copyButton.addEventHandler(this, "copyToClipboardLinkerOutput");
  }

  // Etiqueta para el cuadro
  fill(50);
  textAlign(LEFT);
  textSize(14);
  text(label, x, y - 10);

  return textArea;
}

// Evento para copiar texto al portapapeles del preprocesador
void copyToClipboardPreprocessor(GButton button, GEvent event) {
  String text = preprocessorInput.getText();
  if (text.isEmpty()) {
    status = "No hay texto para copiar en la entrada del preprocesador.";
    return;
  }
  Toolkit.getDefaultToolkit().getSystemClipboard().setContents(new StringSelection(text), null);
  status = "Texto copiado al portapapeles desde la entrada del preprocesador!";
}

// Evento para copiar texto al portapapeles del ensamblador
void copyToClipboardAssembler(GButton button, GEvent event) {
  String text = assemblerInput.getText();
  if (text.isEmpty()) {
    status = "No hay texto para copiar en la entrada del ensamblador.";
    return;
  }
  Toolkit.getDefaultToolkit().getSystemClipboard().setContents(new StringSelection(text), null);
  status = "Texto copiado al portapapeles desde la entrada del ensamblador!";
}

// Evento para copiar texto del preprocesador a su salida
void copyToClipboardPreprocessorOutput(GButton button, GEvent event) {
  String text = preprocessorOutput.getText();
  if (text.isEmpty()) {
    status = "No hay texto para copiar en la salida del preprocesador.";
    return;
  }
  Toolkit.getDefaultToolkit().getSystemClipboard().setContents(new StringSelection(text), null);
  status = "Texto copiado al portapapeles desde la salida del preprocesador!";
}

// Evento para copiar texto del analizador léxico a su salida
void copyToClipboardLexicalOutput(GButton button, GEvent event) {
  String text = lexicalOutput.getText();
  if (text.isEmpty()) {
    status = "No hay texto para copiar en la salida del analizador léxico.";
    return;
  }
  Toolkit.getDefaultToolkit().getSystemClipboard().setContents(new StringSelection(text), null);
  status = "Texto copiado al portapapeles desde la salida del analizador léxico!";
}

// Evento para copiar texto del ensamblador a su salida
void copyToClipboardAssemblerOutput(GButton button, GEvent event) {
  String text = assemblerOutput.getText();
  if (text.isEmpty()) {
    status = "No hay texto para copiar en la salida del ensamblador.";
    return;
  }
  Toolkit.getDefaultToolkit().getSystemClipboard().setContents(new StringSelection(text), null);
  status = "Texto copiado al portapapeles desde la salida del ensamblador!";
}

// Evento para copiar texto del Linker a su salida
void copyToClipboardLinkerOutput(GButton button, GEvent event) {
  String text = linkerOutput.getText();
  if (text.isEmpty()) {
    status = "No hay texto para copiar en la salida del Linker.";
    return;
  }
  Toolkit.getDefaultToolkit().getSystemClipboard().setContents(new StringSelection(text), null);
  status = "Texto copiado al portapapeles desde la salida del Linker!";
}


GButton createButton(String label, int x, int y, String action) {
  GButton button = new GButton(this, x, y, 450, 40);
  button.setText(label);
  button.addEventHandler(this, action);
  return button;
}

GButton createSquareButton(String label, int x, int y, String action) {
  GButton button = new GButton(this, x, y, 80, 40); // Tamaño cuadrado pequeño
  button.setText(label);
  button.addEventHandler(this, action);
  return button;
}

void draw() {
  background(220);

  // Título del sistema
  textAlign(CENTER);
  textSize(18);
  fill(50);
  text("TALLER 1 - SISTEMA DE PROCESAMIENTO DE LENGUAJE", width / 2, 40);

  // Mostrar información si el toggle está activo
  if (showInfo) {
    displayInformation();
  } else {
    // Renderizar componentes solo si el toggle está desactivado
    drawComponents();
  }
}


// *** Función para dibujar componentes normales ***
void drawComponents() {
  textSize(16);
  textAlign(LEFT);

  // Sección superior
  text("Entrada del Preprocesador", 50, 90);
  text("Salida del Preprocesador (Entrada del Analizador Léxico)", 550, 90);
  text("Salida del Analizador Léxico", 1050, 90);

  // Sección inferior
  text("Entrada del Ensamblador", 50, 490);
  text("Salida del Ensamblador (Entrada del Linker)", 550, 490);
  text("Salida del Linker", 1050, 490);

  // Estado del sistema
  textAlign(LEFT);
  textSize(18);
  text(status, 50, height - 50);
}

// *** Función para mostrar la información del equipo ***
void displayInformation() {
  textAlign(CENTER);
  textSize(16);
  fill(50);

  // Información de texto
  String info = 
    "Integrantes: \n\n" +
    "David Alfonso Cañas Palomino\n" +
    "Esteban Lopez Barreto\n" +
    "Santiago Reyes Ochoa\n" +
    "Juan Esteban Peña Burgos\n" +
    "Gabriela Guzman Rivera\n" +
    "Gabriela Gallegos Rubio\n\n" +
    "Universidad Nacional de Colombia\n" +
    "Facultad de Ingeniería\n" +
    "Departamento de Ingeniería de Sistemas e Industrial\n\n" +
    "Lenguajes de programación (2025966)\n\n" +
    "Profesor Jorge Eduardo Ortiz Triviño\n" +
    "Bogotá, D.C. Colombia\n" +
    "2024 - 2S";

  text(info, width / 2, height / 2 - 140);
}

void toggleInfo(GButton button, GEvent event) {
  showInfo = !showInfo; // Alternar estado
  toggleInfoButton.setText(showInfo ? "Hide Info" : "Info"); // Actualizar texto del botón
  
  // Mostrar/ocultar componentes
  setComponentsVisibility(!showInfo);
}

void setComponentsVisibility(boolean visible) {
  // Establecer la visibilidad de todos los componentes de G4P
  preprocessorInput.setVisible(visible);
  preprocessorOutput.setVisible(visible);
  lexicalOutput.setVisible(visible);
  assemblerInput.setVisible(visible);
  assemblerOutput.setVisible(visible);
  linkerOutput.setVisible(visible);

  // Establecer visibilidad de los botones de copiar
  copyPreprocessorInputButton.setVisible(visible);
  copyAssemblerInputButton.setVisible(visible);
  copyPreprocessorOutputButton.setVisible(visible);
  copyLexicalOutputButton.setVisible(visible);
  copyAssemblerOutputButton.setVisible(visible);
  copyLinkerOutputButton.setVisible(visible);

  // Botones principales
  runPreprocessorButton.setVisible(visible);
  runLexicalAnalyzerButton.setVisible(visible);
  runAssemblerButton.setVisible(visible);
  runLinkerButton.setVisible(visible);

  // Botones inferiores
  clearAllButton.setVisible(visible);
  loadExample1Button.setVisible(visible);
  loadExample2Button.setVisible(visible);
  loadExample3Button.setVisible(visible);
  uploadPreprocessorButton.setVisible(visible);
  uploadAssemblerButton.setVisible(visible);
}

void runPreprocessor(GButton button, GEvent event) {
  if (preprocessorInput.getText().trim().isEmpty()) {
    status = "Entrada del preprocesador vacía. Proporcione datos válidos.";
    return;
  }
  // Llamar a la función processFile para procesar el archivo de entrada con el módulo 'preprocessor'
  processFile(preprocessorInput, preprocessorOutput, "preprocessor");
  status = "Preprocesador ejecutado correctamente!";
}

void runLexicalAnalyzer(GButton button, GEvent event) {
  if (preprocessorOutput.getText().trim().isEmpty()) {
    status = "Salida del preprocesador vacía. Ejecute primero el preprocesador.";
    return;
  }
  // Llamar a la función processFile para procesar el archivo de salida del preprocesador con el módulo 'lexicalAnalyzer'
  processFile(preprocessorOutput, lexicalOutput, "lexicalAnalyzer");
  status = "Analizador léxico ejecutado correctamente!";
}

void runAssembler(GButton button, GEvent event) {
  if (assemblerInput.getText().trim().isEmpty()) {
    status = "Entrada del ensamblador vacía. Proporcione datos válidos.";
    return;
  }
  // Llamar a la función processFile para procesar el archivo de entrada con el módulo 'assembler'
  processFile(assemblerInput, assemblerOutput, "assembler");
  status = "Ensamblador ejecutado correctamente!";
}

void runLinker(GButton button, GEvent event) {
  if (assemblerOutput.getText().trim().isEmpty()) {
    status = "Salida del ensamblador vacía. Ejecute primero el ensamblador.";
    return;
  }
  // Llamar a la función processFile para procesar el archivo de salida del ensamblador con el módulo 'linker'
  processFile(assemblerOutput, linkerOutput, "linker");
  status = "Vinculador ejecutado correctamente!";
}

void processFile(GTextArea inputField, GTextArea outputField, String moduleName) {
  try {

    // Obtén el texto de entrada y guárdalo en un archivo temporal
    String inputText = inputField.getText().trim();

    // Crear archivo temporal para la entrada
    String tempInputFilePath = basePath + "/temp/" + "temp_" + moduleName + ".txt";
    FileWriter fileWriter = new FileWriter(tempInputFilePath);
    BufferedWriter bufferedWriter = new BufferedWriter(fileWriter);
    bufferedWriter.write(inputText);
    bufferedWriter.close();

    // Definir la ruta al ejecutable del módulo
    String execPath = basePath + "/Execs/" + moduleName;
    
    String[] commandArray;
    
    if (!moduleName.equals("preprocessor")) { 
      commandArray = new String[] { "\"" + execPath + "\"", "\"" + tempInputFilePath + "\"" };
    } else {
      commandArray = new String[] { "\"" + execPath + "\"", "\"" + tempInputFilePath + "\"", "\"" + libsPath + "\"" };
    }
    
    // Imprimir los detalles del comando para depuración
    System.out.println("Command: " + String.join(" ", commandArray));

    // Ejecutar el proceso
    ProcessBuilder processBuilder = new ProcessBuilder(commandArray);
    processBuilder.directory(new File(basePath));  // Establecer el directorio de trabajo
    processBuilder.redirectErrorStream(true);  // Redirigir la salida de error a la salida estándar
    Process process = processBuilder.start();

    // Capturar la salida y colocarla en el campo de texto de salida
    BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
    String line;
    StringBuilder outputText = new StringBuilder();
    while ((line = reader.readLine()) != null) {
      outputText.append(line).append("\n");
    }

    // Esperar a que el proceso termine
    int exitCode = process.waitFor();
    System.out.println("Exit Code: " + exitCode);  // Mostrar el código de salida del proceso

    // Colocar la salida en el campo de texto
    outputField.setText(outputText.toString());

    if (exitCode == 0) {
      status = "Archivo procesado correctamente!";
    } else {
      status = "Error al procesar el archivo!";
    }
  } catch (Exception e) {
    e.printStackTrace();  // Mostrar el error completo
    status = "Error al procesar el archivo!";
  }
}


// *** Métodos para cargar entradas ***
void uploadFileToField(GButton button, GEvent event) {
  if (button == uploadPreprocessorButton) {
    loadFileToField(preprocessorInput);
  } else if (button == uploadAssemblerButton) {
    loadFileToField(assemblerInput);
  }
}

// *** Métodos para cargar ejemplos ***
void loadExample1(GButton button, GEvent event) {
  loadExample("Example1");
}

void loadExample2(GButton button, GEvent event) {
  loadExample("Example2");
}

void loadExample3(GButton button, GEvent event) {
  loadExample("Example3");
}

void loadExample(String exampleFolder) {
  try {
    String examplePath = examplesPath + exampleFolder + "/";
    preprocessorInput.setText(readFile(examplePath + "preprocessorInput.txt"));
    assemblerInput.setText(readFile(examplePath + "assemblerInput.txt"));
    clearOutputs();
    status = "Se cargó el " + exampleFolder + " exitosamente!";
  } catch (IOException e) {
    status = "Error cargando el " + exampleFolder + "!";
  }
}

String readFile(String filePath) throws IOException {
  StringBuilder content = new StringBuilder();

  try {
    BufferedReader reader = new BufferedReader(new FileReader(filePath));
    String line;
    while ((line = reader.readLine()) != null) {
      content.append(line).append("\n");
    }
    reader.close();
  } catch (FileNotFoundException e) {
    System.err.println("File not found: " + filePath);
    throw new IOException("File not found: " + filePath, e);
  } catch (IOException e) {
    System.err.println("Error reading file: " + filePath);
    throw new IOException("Error reading file: " + filePath, e);
  }

  return content.toString();
}

void clearAll(GButton button, GEvent event) {
  preprocessorInput.setText("");
  preprocessorOutput.setText("");
  lexicalOutput.setText("");
  assemblerInput.setText("");
  assemblerOutput.setText("");
  linkerOutput.setText("");
  status = "Todos los campos han sido limpiados.";
}

void clearOutputs() {
  preprocessorOutput.setText("");
  lexicalOutput.setText("");
  assemblerOutput.setText("");
  linkerOutput.setText("");
}

void loadFileToField(GTextArea textArea) {
  String workingDir = sketchPath("");
  File defaultDir = new File(workingDir);

  JFileChooser fileChooser = new JFileChooser(defaultDir);
  int returnValue = fileChooser.showOpenDialog(null);

  if (returnValue == JFileChooser.APPROVE_OPTION) {
    File selectedFile = fileChooser.getSelectedFile();
    if (!selectedFile.getName().endsWith(".txt")) {
      status = "Selecciona un archivo.txt válido.";
      return;
    }

    try {
      BufferedReader reader = new BufferedReader(new FileReader(selectedFile));
      StringBuilder fileContent = new StringBuilder();
      String line;
      while ((line = reader.readLine()) != null) {
        fileContent.append(line).append("\n");
      }
      reader.close();
      textArea.setText(fileContent.toString());
      status = "Entrada cargada exitosamente!";
    } catch (IOException e) {
      e.printStackTrace();
      status = "Error cargando el archivo!";
    }
  }
}
