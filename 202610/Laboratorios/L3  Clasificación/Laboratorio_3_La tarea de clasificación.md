# Laboratorio 3 - CLasificación 

[Caso](#contexto)

[Objetivos](#objetivos)

[Herramientas](#herramientas)

[Conjunto de datos](#datos)

[Actividades a realizar](#actividades)

[Análisis de resultados](#resultados)

[Entregables](#entregables)

[Criterios de evaluación](#rubrica)

[Uso de IAG en actividades del curso ISIS2611](#principios) 

## <a name="contexto"></a> Caso: SmartAlpes
SmartAlpes es una cadena de gimnasios que ofrece programas de entrenamiento personalizados, orientados a mejorar el rendimiento y bienestar de sus clientes. Actualmente, la recomendación de planes de entrenamiento y nutrición se basa principalmente en la experiencia de los entrenadores, lo que puede generar inconsistencias a medida que aumenta el número de usuarios. Con el fin de fortalecer este proceso, la empresa ha recopilado información detallada de sus clientes, incluyendo datos demográficos, medidas físicas, nivel de actividad, experiencia deportiva, preferencias dietéticas, horas de sueño y hábitos de vida. También se consideran indicadores de bienestar diario, como número de pasos, ingesta de proteína y consumo de agua.
El objetivo de la organización es utilizar estos datos para mejorar la recomendación de planes de entrenamiento y nutrición, de manera que cada cliente reciba una sugerencia acorde con su perfil y estilo de vida. Esto permitiría mejorar la personalización del servicio, aumentar la satisfacción de los usuarios y optimizar el trabajo de los entrenadores. Para llevar a cabo este estudio los ha contratado con el fin de explorar la información disponible y desarrollar soluciones basadas en datos que apoyen la toma de decisiones en la recomendación de planes personalizados.


## <a name="objetivos"></a> Objetivos

- Comparar distintos enfoques de modelado con el fin de identificar el más adecuado para recomendar planes personalizados según el perfil físico, los hábitos y el estilo de vida de cada cliente.
- Aplicar técnicas de selección de modelos para la búsqueda sistemática de hiperparámetros.
- Reconocer posibles sesgos en un modelo de aprendizaje de máquina.
- Comunicar de forma clara y estructurada los resultados obtenidos, sustentando las decisiones metodológicas adoptadas.


 
## <a name="herramientas"></a> Herramientas

Durante este laboratorio se trabajará con las siguientes herramientas:

- Librerías de Python para el procesamiento y analisis de datos como: 
    - Pandas
    - Scikit-Learn
    - Matplotlib, Seaborn
- Entorno de desarrollo Visual Studio instalado localmente mediante Anaconda o en la nube mediante Google Colab.


## <a name="datos"></a> Conjunto de datos

El conjunto de datos reúne información demográfica, física y de estilo de vida de los usuarios del gimnasio, así como indicadores de bienestar diario. Además, contiene la recomendación de plan de entrenamiento y nutrición asignada a cada cliente. El conjunto de datos ha sido tomado de este [enlace](https://www.kaggle.com/datasets/ayyappanmarimuthu/fitness-goal-achievement-dataset) y modificado para propósitos de este proyecto.

## <a name="actividades"></a> Actividades a realizar

- **1. Exploración de los datos para identificar problemas de calidad y otras características. 

- **2. Propuesta de limpieza y preparación de los datos, justificando las decisiones tomadas con base en los resultados obtenidos en el paso anterior y de acuerdo con los modelos que se van a construir.

- **3. Desarrollar dos modelos de regresión logística, uno para la recomendación de planes de entrenamiento y otro para la recomendación de planes de nutrición, incorporando una búsqueda de hiperparámetros con validación cruzada, explorando al menos el tipo de regularización y el solver utilizado. Este proceso debe estructurarse mediante un pipeline, de manera que el preprocesamiento y el modelo queden integrados en un flujo de trabajo reproducible y ordenado.

- **4. Desarrollar dos modelos basados en árboles de decisión, uno para la recomendación de planes de entrenamiento y otro para la recomendación de planes de nutrición, incorporando una búsqueda de hiperparámetros con validación cruzada que permita explorar aspectos como la profundidad máxima del árbol, el número mínimo de muestras por nodo y los criterios de división. Este proceso debe estructurarse mediante un pipeline, integrando el preprocesamiento y el modelo en un flujo de trabajo reproducible y ordenado.

- **5. Elaboración de una tabla comparativa mostrando el rendimiento sobre test de los mejores dos modelos, por cada objetivo, obtenidos en los puntos 3 y 4, con base en las métricas recall, precisión y F1-score.

- **6. Identificación de las variables más relevantes en la predicción, utilizando tanto en el modelo de árboles de decisión como el de regresión logística (para ambos objetivos). Posteriormente, comparar la importancia de las características según cada modelo con el fin de evaluar cómo distintos enfoques destacan diferentes factores del perfil de los usuarios para comprender mejor qué variables pueden influir más en las decisiones de recomendación.

- **7. Elaboración de un video de máximo 3 minutos donde se expliquen los elementos relevantes del ejercicio realizado. Este video debe estar orientado a la organización SmartAlpes.

- **8. Generación de predicciones sobre los datos compartidos que no se encuentran etiquetados utilizando el mejor modelo. Exportar las predicciones en formato CSV utilizando como base el mismo archivo de datos dado.

- **9. BONO. Como extensión de la actividad, se propone la construcción de un modelo de clasificación multietiqueta (multi-label) que permita predecir simultáneamente el plan de entrenamiento y el plan de nutrición. Para ello, los grupos deben investigar cómo implementar este tipo de modelos en scikit-learn, utilizando alguno de los algoritmos utilizado en las etapas previas. El modelo deberá integrarse en un pipeline que incluya las etapas de preprocesamiento y entrenamiento. Además, se espera que identifiquen y justifiquen métricas adecuadas para problemas multietiqueta y comparen el desempeño de este enfoque con la estrategia original de entrenar modelos separados para cada objetivo.


## <a name="resultados"></a> Análisis de resultados
Una vez construido los modelos, deberías estar en capacidad de responder estas preguntas: 

- ¿Qué características del cliente parecen estar más relacionadas con el tipo de plan recomendado?

- ¿Existen variables que podrían ser redundantes o poco informativas?

- ¿El modelo logra reproducir adecuadamente las recomendaciones presentes en los datos?

- A partir de alguno de los modelos creados con árboles de decisión, describa en términos de reglas, las características que cumplen las variables involucradas en la recomendación que se da. Incluya además, la utilidad y la limitación que tienen este estilo de reglas en modelos de árboles de decisión principalmente en el proceso de explicabilidad del modelo.

- ¿Cómo podría integrarse este tipo de modelo en una plataforma digital de fitness o bienestar?

- ¿Qué limitaciones tendría utilizar un sistema automático para recomendar planes de entrenamiento?

- ¿Qué fuentes de sesgo podrían estar presentes en los datos o en el proceso de modelado?


## <a name="entregables"></a> Entregables

- Notebook (*.ipynb y *.html) por BloqueNeón con los nombres de los estudiantes. El Notebook debe estar documentado con las justificaciones de las decisiones tomadas en cada paso del ciclo de ML y las respuestas a las preguntas planteadas en el apartado “Análisis de resultados”. Además, deben ser visibles las ejecuciones de cada celda. 
- Video explicativo.
- Archivo "Datos test Lab3" con la etiqueta de las predicciones

Esta entrega debe realizarse máximo el **20 de abril 20:00**. Recuerda registrar en el grupo GL3, los dos integrantes que presentan este laboratorio, con el fin de habilitar el enlace de entrega.
Si la entrega la hacen después de el **20 de abril 20:00** y antes del **21 de abril 2:00 a.m.**, su entrega tendrá una penalización del 30%, lo que significa que será calificada sobre 3.5 y no sobre 5.0. Después de esta última fecha toda entrega tendrá una nota de 0.


## <a name="rubrica"></a> Criterios de evaluación

A continuación se encuentra la rúbrica de calificación que se utiliza para valorar los entregables tomando como base los entregables:

| Actividad | Porcentaje |
|:---|:---:|
| 1. Exploración de los datos y propuesta de limpieza y preparación.  | 15% |
| 2. Modelo de regresión logística.  | 15% |
| 3. Modelo de árboles de decisión.  | 15% |
| 4. Tabla comparativa de los resultados de los modelos y se argumenta la selección del mejor.   | 5% |
| 5. Identificación de las variables más relevantes.  | 10% |
| 6. Análisis de resultados con base en las preguntas de la sección F.  | 25% |
| 7. Video corto donde se expliquen los elementos más relevantes del ejercicio.  | 5% |
| 8. Archivo con resultado de predicciones sobre los datos de prueba compartidos en formato CSV ("Datos Test Lab 3.csv"). Se tomará como base el f1-score para ordenar y asignar la nota del grupo.  | 5% |
| 9. Registro del uso de IA generativa en el desarrollo del laboratorio, de forma clara, incluyendo los prompts utilizados (ver en la siguiente sección).  | 5% |
| 10. BONO. Modelo multietiqueta.  | 10% |


## <a name="principios"></a> Uso de IAG en actividades del curso ISIS2611
La información que se presenta a continuación también está publicada en Bloque Neón, en la sección del curso **"Uso de la IA generativa"**. 

**Principios que rigen el uso de la IA en el curso**

- **Autoría humana.** El estudiante es el responsable final de todo el contenido entregado, incluyendo código, resultados, análisis y conclusiones.

- **Transparencia.** El uso de IAG debe ser claramente declarado, indicando cómo y para qué se utilizó.

- **Pensamiento crítico.** Las respuestas generadas por IAG no deben aceptarse de forma automática; deben ser evaluadas, contrastadas y, cuando sea necesario, corregidas.

- **Aprendizaje y no sustitución.** La IAG debe apoyar el aprendizaje, no reemplazar el proceso de razonamiento, diseño o toma de decisiones por parte del estudiante.

**Reglas prácticas de uso (obligatorias).**

En todas las actividades donde se utilice la IAG, los estudiantes deberán incluir una sección titulada: “Uso de herramientas de IA generativa”.

Esta sección deberá contener:

- Declaración del uso. Nombre de la herramienta utilizada y tipo de uso (ayuda conceptual, generación inicial de código, explicación teórica, depuración, redacción, etc.).

- Prompts utilizados. Se deben documentar los prompts principales, de forma textual o resumida. No es necesario incluir interacciones menores, pero sí aquellas que influyeron directamente en el resultado entregado.

- Análisis crítico del resultado. El estudiante deberá responder, al menos, a dos de las siguientes preguntas: ¿Qué partes del contenido generado fueron correctas y útiles? ¿Qué errores, imprecisiones o limitaciones se identificaron? ¿Qué decisiones técnicas fueron modificadas respecto a la respuesta de la IAG y por qué? ¿Qué conceptos del curso permitieron evaluar o mejorar la respuesta generada?

- Aportes propios del estudiante. Debe explicitarse claramente: ¿Qué fue desarrollado, modificado o decidido por el estudiante? ¿Qué ajustes se realizaron sobre el código o la explicación original? ¿Qué aprendizajes se obtuvieron del proceso?

**¿Qué se considera un buen uso y un mal uso?**

**A. Usos recomendados.** Se recomienda el uso de IA generativa para:

- Aclarar conceptos teóricos complejos.
- Comparar enfoques o algoritmos.
- Generar esqueletos iniciales de código (que luego deben ser comprendidos y adaptados).
- Identificar errores de implementación y proponer soluciones.
- Mejorar la redacción técnica de reportes (sin alterar el contenido conceptual).

**B.Usos no recomendados.** No se considera un uso responsable:

- Copiar y entregar código o texto sin comprensión.
- Utilizar IAG para definir decisiones clave sin justificación.
- Presentar resultados sin saber explicar cómo fueron obtenidos.
- Usar IA para responder evaluaciones individuales no autorizadas.
- Omitir la declaración de uso de IA cuando esta fue utilizada.
