# Reporte del Modelo Final

## Resumen Ejecutivo

Este documento presenta los resultados obtenidos con el modelo final de clasificación desarrollado para distinguir entre personas extrovertidas e introvertidas. El modelo final implementado fue una regresión logística optimizada mediante búsqueda en malla (`GridSearchCV`), la cual alcanzó un **93.79% de precisión en el conjunto de prueba**. 

Las métricas obtenidas en los conjuntos de validación y prueba muestran un rendimiento equilibrado entre clases, con valores F1 superiores al 0.90. Esto indica que el modelo es robusto y generaliza bien sobre nuevos datos. La regresión logística fue seleccionada por su interpretabilidad, bajo riesgo de sobreajuste y eficiencia computacional.

## Descripción del Problema

El problema abordado consiste en construir un modelo predictivo capaz de clasificar a un individuo como extrovertido o introvertido, basándose en características personales y patrones de comportamiento social. Este problema se enmarca en el contexto de personalización de servicios, contenidos y experiencias digitales, donde conocer el tipo de personalidad del usuario puede ser un factor crítico.

El conjunto de datos proviene de **Kaggle**, y contiene información como el tiempo pasado a solas, la asistencia a eventos sociales, la frecuencia de salir de casa, el tamaño del círculo de amigos y la frecuencia de publicaciones en redes sociales. El objetivo era lograr una precisión mínima del 80%, con un análisis exploratorio que destacara las variables más relevantes para la clasificación.

## Descripción del Modelo

El modelo final fue una **regresión logística** entrenada sobre datos normalizados. Se eliminó información irrelevante y se aplicó escalamiento de características utilizando `StandardScaler`. Los hiperparámetros del modelo se optimizaron mediante validación cruzada con `GridSearchCV`, explorando diferentes valores para `C`, `solver` y `max_iter`.

La arquitectura final se entrena sobre un conjunto del 60% de los datos, validando sobre un 20% y probando en el 20% restante. El modelo optimizado fue el siguiente:

- **Modelo**: `LogisticRegression`
- **Mejores hiperparámetros**:

| Parámetro           | Valor         |
|---------------------|---------------|
| `penalty`           | 'l2'          |
| `dual`              | False         |
| `tol`               | 0.0001        |
| `C`                 | 1e-05         |
| `fit_intercept`     | True          |
| `intercept_scaling`| 1             |
| `class_weight`      | None          |
| `random_state`      | None          |
| `solver`            | 'liblinear'   |
| `max_iter`          | 500           |
| `multi_class`       | 'deprecated'  |
| `verbose`           | 0             |
| `warm_start`        | False         |
| `n_jobs`            | None          |
| `l1_ratio`          | None          |


Este modelo fue seleccionado por su buena relación entre simplicidad, interpretabilidad y desempeño.

## Evaluación del Modelo

Se utilizaron las siguientes métricas para evaluar el rendimiento del modelo:

- **Accuracy**: proporción de predicciones correctas.
- **Precision**: proporción de verdaderos positivos sobre todos los positivos predichos.
- **Recall**: proporción de verdaderos positivos sobre todos los positivos reales.
- **F1-score**: media armónica entre precisión y recall.
- **Matriz de confusión**: para visualizar aciertos y errores por clase.

### Resultados en el conjunto de validación:

- **Accuracy**: 91.21%

| Clase | Precision | Recall | F1-score | Soporte |
|-------|-----------|--------|----------|---------|
| 0     | 0.87      | 0.93   | 0.90     | 253     |
| 1     | 0.95      | 0.90   | 0.92     | 327     |
| **Total** | **0.91** | **0.91** | **0.91** | **580** |

### Resultados en el conjunto de prueba:

- **Accuracy**: 93.79%

| Clase | Precision | Recall | F1-score | Soporte |
|-------|-----------|--------|----------|---------|
| 0     | 0.94      | 0.94   | 0.94     | 286     |
| 1     | 0.94      | 0.94   | 0.94     | 294     |
| **Total** | **0.94** | **0.94** | **0.94** | **580** |

## Conclusiones y Recomendaciones

El modelo final cumple con creces el objetivo del proyecto, superando la meta del 80% de precisión establecida inicialmente. El rendimiento es alto, con métricas F1 equilibradas en ambas clases y una accuracy superior al 93% en datos de prueba.

### Puntos fuertes:
- Alto desempeño predictivo.
- Generalización adecuada.
- Modelo interpretable y eficiente.

### Puntos débiles:
- No captura relaciones no lineales complejas que otros modelos más sofisticados podrían explotar.
- Dependencia del preprocesamiento manual para remover variables irrelevantes.

### Recomendaciones:
- Explorar modelos adicionales como Random Forest, SVM o redes neuronales para comparativa.
- Aplicar técnicas de reducción de dimensionalidad o selección automática de características.
- Evaluar el modelo en datos reales o no vistos, en un entorno productivo.

## Referencias

- [Scikit-learn Documentation](https://scikit-learn.org)
- [Dataset de Kaggle: extrovert-vs-introvert-behavior-data](https://www.kaggle.com/datasets/rakeshkapilavai/extrovert-vs-introvert-behavior-data)
- Documentación interna del proyecto (Julio 2025)
- Evaluación basada en métricas de `sklearn.metrics`
- GridSearchCV para ajuste de hiperparámetros
