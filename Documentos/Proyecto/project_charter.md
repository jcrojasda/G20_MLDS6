# Project Charter - Entendimiento del Negocio

## Nombre del Proyecto

Clasificación de Personalidad: Extrovertidos vs Introvertidos

## Objetivo del Proyecto

El objetivo principal de este proyecto es construir un modelo de clasificación que permita predecir si una persona es extrovertida o introvertida basándose en su comportamiento social y características personales. Este modelo podría ser útil para mejorar la personalización de servicios, contenidos y experiencias para cada tipo de personalidad. Además, nos ayudará a comprender mejor los patrones que definen a las personas extrovertidas e introvertidas a partir de sus hábitos sociales.

## Alcance del Proyecto

### Incluye:

- Los datos disponibles provienen de Kaggle y contienen información sobre el comportamiento social de los individuos, como el tiempo pasado a solas, asistencia a eventos sociales, frecuencia de salir de casa, tamaño del círculo de amigos y frecuencia de publicaciones en redes sociales.
- El resultado esperado es un modelo predictivo capaz de clasificar a los individuos como extrovertidos o introvertidos con precisión, basado en las características observadas en los datos.
- Los criterios de éxito del proyecto son:
  - Desarrollar un modelo preciso que logre una clasificación correcta en al menos un 80% de los casos.
  - Generar un análisis exploratorio de los datos que permita entender las variables más relevantes para la clasificación.

### Excluye:

- No se incluirán datos adicionales más allá de los proporcionados en el conjunto de Kaggle.
- No se contemplará el uso de datos en tiempo real ni la implementación de un sistema de retroalimentación continua para mejorar el modelo después de su despliegue.

## Metodología

La metodología utilizada para este proyecto será principalmente supervisada, usando un enfoque de clasificación binaria entre dos categorías: extrovertidos e introvertidos. Se realizarán los siguientes pasos:
1. **Preprocesamiento de datos**: Limpieza de los datos, manejo de valores faltantes y transformación de las variables según sea necesario.
2. **Análisis exploratorio de datos (EDA)**: Análisis visual y estadístico para entender las relaciones entre las variables y la variable objetivo.
3. **Modelado**: Selección y entrenamiento de varios modelos de clasificación, como regresión logística, árboles de decisión y máquinas de soporte vectorial.
4. **Evaluación**: Evaluación del modelo utilizando métricas como precisión, recall, F1-score y la matriz de confusión.
5. **Despliegue**: Creación de un modelo final listo para su uso en un entorno real.

## Cronograma

| Etapa | Duración Estimada | Fechas |
|-------|--------------------|--------|
| Entendimiento del negocio y carga de datos | 1 semana | del 27 de junio al 3 de julio |
| Preprocesamiento, análisis exploratorio | 1 semana | del 4 de julio al 10 de julio |
| Modelamiento y extracción de características | 1 semana | del 11 de julio al 17 de julio |
| Despliegue | 1 semana | del 18 de julio al 24 de julio |
| Evaluación y entrega final | 3 días | del 25 de julio al 27 de julio |

## Equipo del Proyecto

- Sara Lucía Jimenez Becerra, Líder de Proyecto, Gerente del Proyecto y Arquitecta de soluciones
- Juan Camilo Rojas Dávila, Científico de Datos

## Presupuesto

El presupuesto asignado al proyecto es de $50,000, cubriendo costos de recursos humanos, software y hardware necesario para el modelado y despliegue del sistema.

## Stakeholders

- **Sergio Jiménez**, Profesor de NLP: Le interesa observar los resultados para sus trabajos de grado.

## Aprobaciones

- **Sara Jiménez**, CEO
- Firma del aprobador: _Sara Jiménez_
- Fecha de aprobación: 3 de julio de 2025
