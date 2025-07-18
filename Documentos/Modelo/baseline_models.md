# Reporte del Modelo Baseline

Este documento contiene los resultados del modelo baseline.

## Descripción del modelo

El modelo baseline consiste en una regresión logística entrenada para predecir el tipo de personalidad de un individuo, representado por la variable `Personality_num`. Este modelo utiliza características extraídas de una base de datos procesada, con datos numéricos ya normalizados. La regresión logística fue seleccionada por su simplicidad, interpretabilidad y buen rendimiento en tareas de clasificación binaria. La búsqueda de hiperparámetros se realizó mediante validación cruzada con `GridSearchCV`.

## Variables de entrada

Las variables de entrada utilizadas en el modelo son:

- `Time_spent_Alone`
- `Stage_fear`
- `Social_event_attendance`
- `Going_outside`
- `Drained_after_socializing`

No se incluyeron:

- `Post_frequency` (eliminada por no ser relevante según el PCA hecho)
- `Friends_circle_size` (eliminada por no ser relevante según el PCA hecho)

## Variable objetivo

La variable objetivo es `Personality_num`, que representa numéricamente el tipo de personalidad clasificado como 0 o 1.

## Evaluación del modelo

### Métricas de evaluación

Se utilizaron las siguientes métricas para evaluar el rendimiento del modelo:

- **Accuracy (Exactitud)**: proporción de predicciones correctas.
- **Precision (Precisión)**: proporción de verdaderos positivos entre los elementos clasificados como positivos.
- **Recall (Exhaustividad)**: proporción de verdaderos positivos entre todos los elementos que realmente pertenecen a la clase positiva.
- **F1-score**: media armónica entre precisión y recall.
- **Matriz de confusión**: para visualizar la distribución de aciertos y errores por clase.

### Resultados de evaluación

**Accuracy de validación**: 91.21%  
**Accuracy de prueba**: 93.79%

**Reporte de clasificación (Validación):**

| Clase | Precision | Recall | F1-score | Soporte |
|-------|-----------|--------|----------|---------|
| 0     | 0.87      | 0.93   | 0.90     | 253     |
| 1     | 0.95      | 0.90   | 0.92     | 327     |
| **Total** | **0.91** | **0.91** | **0.91** | **580** |

**Reporte de clasificación (Prueba):**

| Clase | Precision | Recall | F1-score | Soporte |
|-------|-----------|--------|----------|---------|
| 0     | 0.94      | 0.94   | 0.94     | 286     |
| 1     | 0.94      | 0.94   | 0.94     | 294     |
| **Total** | **0.94** | **0.94** | **0.94** | **580** |

## Análisis de los resultados

El modelo baseline logra un rendimiento sólido tanto en el conjunto de validación como en el de prueba. Las métricas de clasificación muestran una buena capacidad para distinguir entre las dos clases, con puntuaciones F1 superiores al 0.90 en ambos conjuntos.

**Fortalezas:**

- Alto rendimiento general, con precisión y recall equilibrados.
- Generalización adecuada (accuracy de validación y prueba muy similares).
- El modelo fue capaz de adaptarse bien a los datos tras la normalización y el ajuste de hiperparámetros.

**Debilidades:**

- Aunque los resultados son buenos, la regresión logística puede no capturar relaciones no lineales complejas entre las variables.
- Podría haber variables redundantes o no relevantes aún presentes en el conjunto de datos.

## Conclusiones

El modelo baseline basado en regresión logística establece una línea base sólida con una accuracy de prueba del 93.79%. Este rendimiento sugiere que el conjunto de datos es suficientemente informativo y que las características numéricas procesadas son adecuadas para la tarea de clasificación.

Sin embargo, se recomienda:

- Explorar modelos más complejos como Random Forest, SVM o redes neuronales para capturar relaciones no lineales.
- Realizar análisis de importancia de variables para reducir dimensionalidad.
- Aplicar técnicas de selección de características o PCA.

## Referencias

- [Scikit-learn Documentation](https://scikit-learn.org)
- GridSearchCV para ajuste de hiperparámetros
- Regresión logística como modelo de clasificación
- [Dataset de Kaggle: extrovert-vs-introvert-behavior-data](https://www.kaggle.com/datasets/rakeshkapilavai/extrovert-vs-introvert-behavior-data)
