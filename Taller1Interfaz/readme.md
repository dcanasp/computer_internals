# Interfaz Taller 1

Este proyecto requiere **Processing 4**. Por favor, asegúrate de instalar la última versión desde su [sitio oficial](https://processing.org/download).  

## Estructura de la carpeta `data`

La carpeta `data` contiene varias subcarpetas organizadas según su propósito en el proyecto. A continuación, se detalla la estructura y el contenido de cada una:  

### 1. **`Examples`**  
   - Contiene las entradas de ejemplo para el **preprocesador** y el **ensamblador**.  
   - Estos ejemplos corresponden a los tres casos planteados para el taller.  

### 2. **`Execs`**  
   - Aquí se encuentran los archivos compilados generados a partir del código en **flex** ubicado en la carpeta `RawModules`.  
   - Cada archivo corresponde a un módulo específico del proyecto.  

### 3. **`Icons`**  
   - Contiene las imágenes utilizadas en la interfaz del proyecto.  

### 4. **`Libs`**  
   - Este es el lugar donde deben guardarse las librerías en código **relocalizable** que se importarán en el preprocesador.  

### 5. **`temp`**  
   - En esta carpeta se almacenan los archivos temporales generados durante la ejecución.  
   - Los archivos temporales toman la entrada de los módulos y se pasan como parámetros para su procesamiento.  

## Exportación del Proyecto  

Para exportar el proyecto como una aplicación ejecutable para Windows:  
1. Abre el archivo `.pde` en **Processing 4**.  
2. Ve al menú `Archivo` y selecciona la opción `Exportar aplicación...`.  
3. Asegúrate de configurar la exportación para Windows en las opciones disponibles.  
4. Una vez exportado, la aplicación estará lista para ser ejecutada en cualquier equipo con Windows.  

## Recomendaciones  
- Antes de ejecutar el proyecto, verifica que todos los archivos necesarios se encuentren en sus respectivas carpetas.  
- Si necesitas agregar nuevas librerías o imágenes, asegúrate de colocarlas en la carpeta correspondiente (`Libs` o `Icons`).  
- Evita eliminar los archivos temporales manualmente; estos se gestionan automáticamente por el programa.  
