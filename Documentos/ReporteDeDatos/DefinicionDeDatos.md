# Definición de los datos

## Origen de los datos

- **Fuente de los datos**: Los datos provienen de un conjunto de datos disponible en Kaggle titulado *"Extrovert vs Introvert Behavior Data"*, creado por el usuario **rakeshkapilavai**. Este conjunto de datos contiene características relacionadas con el comportamiento de las personas, clasificándolas en introvertidos y extrovertidos.
  - **Fuente de los datos**: [Kaggle - Extrovert vs Introvert Behavior Data](https://www.kaggle.com/datasets/rakeshkapilavai/extrovert-vs-introvert-behavior-data)
  - **Forma de obtención**: Los datos fueron descargados manualmente desde el portal de Kaggle
  Contiene un archivo CSV que contiene varias columnas con características del comportamiento de las personas.

---

## Especificación de los scripts para la carga de datos

- **Script utilizado para la carga de los datos**:

  El conjunto de datos puede ser cargado utilizando un script en Python con la librería `pandas`. El script básico para cargar los datos desde un archivo CSV podría ser el siguiente:

  ```python
  import pandas as pd

  # Ruta del archivo CSV
  data = pd.read_csv('path_to_your_file/extrovert_vs_introvert.csv')

  # Ver las primeras filas del dataset
  print(data.head())

---


## Referencias a rutas o bases de datos origen y destino


### **Rutas de origen de datos**

####  Especificar la ubicación de los archivos de origen de los datos

- **Ruta del archivo de origen**: Los datos se encuentran en un archivo CSV denominado `personality_dataset.csv`, ubicado en la carpeta `../../Datos/SinProcesar/`.
  - Ejemplo de código para cargar el archivo:
    ```python
    import pandas as pd
    data = pd.read_csv('../../Datos/SinProcesar/personality_dataset.csv')
    data.head()
    ```
    En este caso, `'../../Datos/SinProcesar/personality_dataset.csv'` es la ruta al archivo CSV que se encuentra en un directorio relativo a la ubicación del script Python.

####  Especificar la estructura de los archivos de origen de los datos

- **Estructura del archivo CSV**:
  - El archivo contiene varias columnas relacionadas con el comportamiento social de las personas. Cada fila representa un individuo y sus valores para variables como el tiempo pasado a solas, la asistencia a eventos sociales, la frecuencia de salir de casa, el tamaño del círculo de amigos y la frecuencia de publicaciones en redes sociales.
  - Ejemplo de las primeras filas del archivo:
    ```plaintext
    Time_spent_Alone, Social_event_attendance, Going_outside, Friends_circle_size, Post_frequency
    4.5, 3, 2, 7, 5
    1.0, 1, 0, 3, 0
    8.0, 5, 4, 10, 3
    ...
    ```

####  Describir los procedimientos de transformación y limpieza de los datos

- **Transformación y limpieza de datos**:
  - Se pueden aplicar varias transformaciones y procedimientos de limpieza antes de cargar los datos en la base de datos de destino. Algunos de estos procedimientos incluyen:
    1. **Eliminación de valores nulos**: Eliminar filas que contengan valores nulos o faltantes, o imputar estos valores cuando sea necesario.
    2. **Conversión de tipos de datos**: Verificar que los tipos de datos sean correctos para cada columna (por ejemplo, convertir a tipo numérico donde sea necesario).
    

---

## Base de datos de destino

###  Especificar la base de datos de destino para los datos

**Base de datos de destino:**  
La base de datos de destino será una base de datos SQLite. SQLite es una base de datos ligera y no requiere un servidor separado, ya que los datos se almacenan directamente en un archivo en el sistema de archivos.

**Conexión a la base de datos:**  
Para cargar los datos en SQLite se utilizará la biblioteca estándar de Python, sqlite3, que permite crear y gestionar archivos de base de datos SQLite sin necesidad de instalar librerías adicionales. Si el archivo de la base de datos no existe, se creará automáticamente al establecer la conexión. Una vez preparados los datos, se pueden insertar directamente desde un DataFrame de pandas utilizando el método to_sql(). Además, se puede indicar que si la tabla ya existe, sea reemplazada con los nuevos datos, y evitar que se incluya el índice del DataFrame como una columna adicional en la base de datos.

---

###  Especificar la estructura de la base de datos de destino

**Estructura de la base de datos:**  
La base de datos de destino debe contener una tabla con las mismas columnas que los datos originales, aplicando las transformaciones necesarias. La estructura básica de la tabla incluye las siguientes columnas y tipos de datos:

- `Time_spent_Alone`: FLOAT  
- `Social_event_attendance`: FLOAT  
- `Going_outside`: FLOAT  
- `Friends_circle_size`: FLOAT  
- `Post_frequency`: FLOAT

Estas columnas corresponden a las variables presentes en el archivo CSV y se almacenarán como tipo `FLOAT`, ya que los valores son numéricos y continuos.

---

###  Describir los procedimientos de carga y transformación de los datos en la base de datos de destino

**Transformación de datos:**  
Antes de cargar los datos en la base de datos, puede ser necesario aplicar transformaciones como la normalización o la conversión de tipos de datos, según lo mencionado previamente.

**Carga de datos:**  
Una vez que los datos estén preparados, se cargan en la base de datos utilizando herramientas de Python como `pandas`, que permiten insertar directamente los datos del dataframe en la tabla correspondiente de la base de datos.

**Verificación de datos:**  
Después de la carga, se deben realizar verificaciones para asegurar que los datos se hayan cargado correctamente. Esto se puede hacer mediante consultas SQL que validen la integridad y exactitud de los registros almacenados.
