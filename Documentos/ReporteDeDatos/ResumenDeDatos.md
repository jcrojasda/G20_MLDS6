###  Resumen general de los datos

El análisis se realizó sobre un conjunto de datos compuesto por **2.900 observaciones** y **8 variables**. Estas variables están relacionadas con comportamientos sociales y características personales que permiten explorar patrones de personalidad.

- **Cantidad total de observaciones**: 2.900 registros.
- **Cantidad de variables**: 8 variables, de las cuales:
  - 5 son **numéricas** (`float64`): `Time_spent_Alone`, `Social_event_attendance`, `Going_outside`, `Friends_circle_size`, `Post_frequency`.
  - 3 son **categóricas** (`object`): `Stage_fear`, `Drained_after_socializing`, `Personality`.
- **Valores nulos**: No se identificaron valores faltantes en ninguna de las columnas del dataset.
- **Rango de valores en las variables numéricas**:
  - `Time_spent_Alone`: de 0 a 11 horas.
  - `Friends_circle_size`: entre 0 y 15 personas.
  - Otras variables como `Post_frequency` y `Social_event_attendance` están acotadas entre 0 y 10.
- **Estadísticos generales**:
  - La media de `Time_spent_Alone` es de 4.5 horas, y la de `Post_frequency` es de 3.56 publicaciones.
  - El 50% de los encuestados reportan salir (`Going_outside`) unas 3 veces por semana y asistir a eventos sociales con frecuencia media.
- **Variable objetivo**: `Personality`, con dos categorías: `Introvert` y `Extrovert`.
###  Resumen de calidad de los datos

El conjunto de datos presenta una calidad adecuada para el análisis, con las siguientes características destacadas:

- **Valores faltantes**:
  - No se identificaron valores nulos en ninguna de las columnas. Todas las variables cuentan con 2.900 valores no nulos.

- **Valores extremos**:
  - Algunas variables, como `Friends_circle_size` (máximo de 15) y `Time_spent_Alone` (máximo de 11), presentan valores máximos alejados de la mediana, pero se encuentran dentro de rangos esperados y no muestran signos claros de ser outliers anómalos.

- **Errores de codificación**:
  - No se detectaron errores evidentes en los tipos de datos. Las variables categóricas están correctamente definidas como tipo `object` y las numéricas como `float64`.

- **Duplicados**:
  - No se reportaron registros duplicados explícitamente, aunque sería recomendable aplicar una validación adicional (`data.duplicated().sum()`) en un análisis posterior.

- **Acciones realizadas**:
  - Se mapearon las variables categóricas (`Stage_fear`, `Drained_after_socializing`, `Personality`) a formato numérico para permitir el análisis de correlación y aplicar técnicas de aprendizaje automático.
  - Se estandarizaron las variables numéricas previo a los análisis de clustering y reducción de dimensionalidad.
###  Variable objetivo

La variable objetivo en este análisis es **`Personality`**, que clasifica a cada individuo como **`Introvert`** o **`Extrovert`**.

- **Tipo de variable**: Categórica (binaria).
- **Codificación** utilizada para el análisis:
  - `Extrovert` → 1
  - `Introvert` → 0

- **Distribución de clases**:
  - Se utilizó una tabla de frecuencia para analizar la proporción entre introvertidos y extrovertidos.
  - Esta distribución es importante para evaluar el balance del dataset y la aplicabilidad de modelos predictivos.

- **Visualización**:
  - Se generaron gráficos para visualizar la distribución de la variable objetivo, facilitando la comprensión de su comportamiento y su relación con otras variables.

Esta variable se utilizó como referencia principal en los análisis de correlación, agrupamiento (clustering) y reducción de dimensionalidad (PCA), permitiendo explorar cómo los distintos comportamientos sociales se relacionan con el tipo de personalidad.

###  Variables individuales

Se realizó un análisis exploratorio detallado de cada una de las variables del conjunto de datos. A continuación, se presentan los principales hallazgos:

- **Variables numéricas** (`Time_spent_Alone`, `Social_event_attendance`, `Going_outside`, `Friends_circle_size`, `Post_frequency`):
  - Se calcularon estadísticas descriptivas (media, mediana, desviación estándar, valores mínimo y máximo).
  - Se identificaron posibles asimetrías y concentración de valores mediante histogramas.
  - Se exploró la relación de cada variable con la variable objetivo `Personality` mediante gráficos de densidad y boxplots.

- **Variables categóricas** (`Stage_fear`, `Drained_after_socializing`):
  - Se codificaron a valores binarios (`Yes` = 1, `No` = 0) para facilitar el análisis.
  - Se analizaron sus frecuencias y cómo se distribuyen entre introvertidos y extrovertidos.

- **Posibles transformaciones**:
  - Se estandarizaron las variables numéricas antes de aplicar técnicas de clustering y reducción de dimensionalidad.
  - No fue necesario imputar valores ni transformar distribuciones con técnicas como logaritmos, dado que no se identificaron sesgos severos.

Este análisis permitió detectar patrones relevantes y preparar los datos para técnicas más avanzadas como PCA y K-Means.

###  Ranking de variables

Para identificar las variables más relevantes en la predicción de la personalidad (`Introvert` vs `Extrovert`), se aplicaron técnicas de análisis de correlación y reducción de dimensionalidad.

- **Análisis de correlación**:
  - Se creó una matriz de correlación entre las variables numéricas, incluyendo la variable objetivo codificada (`Personality_num`).
  - Se identificaron asociaciones positivas con `Stage_fear` y `Drained_after_socializing`, y asociaciones negativas con `Friends_circle_size` y `Post_frequency`.

- **Reducción de dimensionalidad con PCA**:
  - Se aplicó Análisis de Componentes Principales (PCA) sobre 7 variables normalizadas.
  - El componente principal 1 (`PC1`) agrupa comportamientos relacionados con el aislamiento o la incomodidad social (con mayor peso en `Stage_fear` y `Drained_after_socializing`).
  - El componente principal 2 (`PC2`) está dominado por `Friends_circle_size` y `Post_frequency`.

- **Contribución porcentual de cada variable a los componentes**:

| Variable                   | Contribución a PC1 (%) | Contribución a PC2 (%) |
|---------------------------|------------------------|------------------------|
| Stage_fear                | 16.41                  | 0.06                   |
| Drained_after_socializing| 16.34                  | 0.09                   |
| Going_outside             | 13.98                  | 4.97                   |
| Social_event_attendance   | 13.51                  | 1.56                   |
| Time_spent_Alone          | 13.42                  | 2.36                   |
| Post_frequency            | 13.42                  | 23.80                  |
| Friends_circle_size       | 12.92                  | 67.16                  |

Estas métricas permitieron establecer una jerarquía de importancia de las variables en función de su peso en la diferenciación entre tipos de personalidad.

###  Relación entre variables explicativas y variable objetivo

Se examinó la relación entre las variables explicativas y la variable objetivo (`Personality`) utilizando diferentes técnicas estadísticas y visuales:

- **Matriz de correlación**:
  - Se generó una matriz de correlación con todas las variables numéricas.
  - Se observó que `Stage_fear` y `Drained_after_socializing` tienen una correlación positiva con la personalidad extrovertida (codificada como 1), mientras que variables como `Friends_circle_size` y `Post_frequency` presentan una correlación negativa.

- **Diagramas de dispersión**:
  - Se utilizaron para explorar visualmente las relaciones entre pares de variables.
  - Al comparar contra la variable objetivo, se evidenciaron patrones en los cuales los extrovertidos tienden a tener mayor frecuencia de publicaciones, círculos sociales más grandes y menor miedo escénico.

- **Modelado exploratorio**:
  - Se aplicó K-Means con 2 clústeres sobre las variables escaladas.
  - El análisis mostró una correspondencia significativa entre los clústeres generados y las categorías de la variable `Personality`, confirmando que existen patrones naturales diferenciables.

- **Reducción de dimensionalidad (PCA)**:
  - Se proyectaron los datos en dos componentes principales (`PC1` y `PC2`) y se visualizaron en un plano bidimensional con colores según la personalidad.
  - La separación visual de los grupos sugiere que las variables analizadas capturan adecuadamente las diferencias entre introvertidos y extrovertidos.

Este análisis combinó herramientas estadísticas y visuales para validar que las variables del dataset tienen una relación significativa y explicativa con respecto a la personalidad.
