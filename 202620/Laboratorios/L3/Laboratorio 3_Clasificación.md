# Laboratorio 3 - La tarea de clasificación

[Caso](#contexto)

[Objetivos](#objetivos)

[Herramientas](#herramientas)

[Conjunto de datos](#datos)

[Actividades a realizar](#actividades)

[Análisis de resultados](#resultados)

[Entregables](#entregables)

[Criterios de evaluación](#rubrica)

[Uso de IAG en actividades del curso ISIS2611](#principios)

## <a name="contexto"></a> Caso: Ruta Alpes

Ruta Alpes es una aplicación de asistencia de conducción que, además de navegación, ofrece recomendaciones personalizadas de cupones a los conductores mientras se desplazan, como descuentos en restaurantes, cafeterías o bares, así como  servicios de comida para llevar, que estén cercanos a su ruta. La empresa ha identificado que enviar el mismo tipo de oferta a todos los usuarios genera baja efectividad y, en algunos casos, molestia (notificaciones irrelevantes en momentos inoportunos). Por esta razón, ha recopilado información de escenarios reales de conducción, junto con características demográficas y hábitos de consumo de los conductores, con el fin de identificar, para un tipo de cupón determinado, cuándo un conductor tiene mayor probabilidad de aceptarlo. Este conocimiento permitiría personalizar la estrategia para la oferta de cupones. 

Como primera aproximación, Ruta Alpes quiere trabajar sobre dos tipos de cupones relacionados con "Cafetería"y "Restaurante(<20)". Para llevar adelante este estudio, la empresa los ha contratado para explorar esta información y construir soluciones basadas en estos datos que les permitan determinar cuándo un conductor tiene mayor probabilidad de aceptar estos cupones. Además, quieren evaluar los riesgos de sesgo y las implicaciones éticas de personalizar ofertas utilizando datos demográficos.

## <a name="objetivos"></a> Objetivos

- Comparar distintos algoritmos de clasificación (regresión logística, árboles de decisión y Random Forest) con el fin de identificar el más adecuado para anticipar la aceptación de cada tipo de cupón.
- Evaluar si el desbalance de clases afecta el desempeño de los modelos y si una técnica de balanceo mejora los resultados.
- Reconocer posibles sesgos en un modelo de aprendizaje de máquina, en particular aquellos derivados del uso de variables demográficas para personalización.
- Comunicar de forma clara y estructurada los resultados obtenidos, sustentando las decisiones metodológicas adoptadas.

## <a name="herramientas"></a> Herramientas

Durante este laboratorio se trabajará con las siguientes herramientas:

- Librerías de Python para el procesamiento y análisis de datos como:
    - Pandas
    - Scikit-Learn (incluye `LogisticRegression`, `DecisionTreeClassifier`, `RandomForestClassifier`)
    - imbalanced-learn, para la actividad de balanceo de clases.
    - Matplotlib, Seaborn
- Entorno de desarrollo Visual Studio instalado localmente mediante Anaconda o en la nube mediante Google Colab.

## <a name="datos"></a> Conjunto de datos

El conjunto de datos reúne escenarios de conducción, junto con información demográfica y hábitos de consumo de los conductores. Para cada escenario, la columna `acepta_cupon` indica si el conductor aceptó o no el cupón ofrecido (`Sí` / `No`). El conjunto de datos ha sido tomado de este [enlace](https://archive.ics.uci.edu/dataset/603/in+vehicle+coupon+recommendation) y modificados para propósitos de este Laboratorio.

## <a name="actividades"></a> Actividades para realizar.

- **1.** Exploración de los datos para identificar problemas de calidad y otras características relevantes de cada subconjunto (Cafetería y Restaurante(<20)), incluyendo la distribución de `acepta_cupon` en cada uno.

- **2.** Propuesta de limpieza y preparación de los datos, justificando las decisiones tomadas con base en los resultados obtenidos en el paso anterior. 

- **3.** Desarrollar dos modelos de **regresión logística**, uno para cada tipo de cupón, incorporando una búsqueda de hiperparámetros con validación cruzada, explorando al menos el tipo de regularización y el solver utilizado. Este proceso debe estructurarse mediante un pipeline.

- **4.** Desarrollar dos modelos basados en **árboles de decisión**, uno para cada tipo de cupón, incorporando una búsqueda de hiperparámetros con validación cruzada que explore la profundidad máxima, el número mínimo de muestras por hoja y el criterio de división. Debe estructurarse mediante un pipeline.

- **5.** Desarrollar dos modelos basados en **Random Forest**, uno para cada tipo de cupón, incorporando una búsqueda de hiperparámetros con validación cruzada que explore al menos el número de árboles, la profundidad máxima de estos y el número mínimo de muestras por hoja. Debe estructurarse mediante un pipeline.

- **6.** Para el modelo de **Restaurante(<20)**, evaluar si aplicar una técnica de balanceo de clases (por ejemplo, SMOTE) mejora el desempeño frente al modelo sin balancear. La comparación debe incluir no solo el F1-score general, sino también el recall de la clase minoritaria, y debe concluirse con una recomendación justificada sobre si conviene o no aplicar la técnica.

- **7.** Elaboración de una tabla comparativa mostrando el rendimiento sobre test de los modelos construidos (regresión logística, árbol de decisión, Random Forest), para cada tipo de cupón, con base en las métricas recall, precisión y F1-score.

- **8.** Identificación de las variables más relevantes en la predicción para los dos tipos de cupón, con el fin de comprender qué factores del contexto o del perfil del conductor influyen más en cada caso.

- **9.** Elaboración de un video de máximo 3 minutos donde se expliquen los elementos relevantes del ejercicio realizado. Este video debe estar orientado a la empresa Ruta Alpes.

- **10.** Generación de predicciones sobre los datos compartidos que no se encuentran etiquetados (Lab3_datos_Prueba), utilizando el mejor modelo obtenido para cada tipo de cupón. Exportar las predicciones en formato CSV utilizando como base el mismo archivo de datos dado.

## <a name="resultados"></a> Análisis de resultados.

Una vez construidos los modelos, debes responder estas preguntas en una sección de análisis:

- ¿Qué características del contexto de conducción o del perfil del conductor parecen estar más relacionadas con la aceptación de cada tipo de cupón?

- ¿Existen variables que podrían ser redundantes o poco informativas?

- ¿El desempeño y el comportamiento de los modelos difieren entre Cafetería y Restaurante(<20)? Si es así, ¿A qué atribuye esa diferencia?

- ¿Aplicar balanceo de clases en Restaurante(<20) mejoró el modelo? Justifique considerando tanto el F1-score general, así como el recall de la clase minoritaria.

- A partir de alguno de los modelos de árbol o Random Forest describa, en términos de reglas o de importancia de variables, las características que llevan a aceptar o rechazar un cupón. Incluya la utilidad y la limitación de este tipo de interpretación.

- ¿Cómo podría integrarse este tipo de modelo en una aplicación de conducción para decidir en tiempo real qué cupón mostrar?

- ¿Qué limitaciones tendría un sistema automático que decide qué ofertas mostrar a cada conductor según su perfil demográfico?

- ¿Qué fuentes de sesgo podrían estar presentes en los datos o en el proceso de modelado, en particular al usar variables como edad, género, estado civil o nivel de ingreso para personalizar ofertas? ¿Qué implicaciones tendría este tipo de personalización si se usara para fines distintos a cupones (por ejemplo, precios dinámicos)?

## <a name="entregables"></a> Entregables

- Notebook (*.ipynb y *.html) por BloqueNeón con los nombres de los estudiantes. El Notebook debe estar documentado con las justificaciones de las decisiones tomadas en cada paso del ciclo de ML y las respuestas a las preguntas planteadas en el apartado "Análisis de resultados". Además, deben ser visibles las ejecuciones de cada celda.
- Video explicativo.
- Archivo "Lab3_datos_Prueba" con la etiqueta de las predicciones.

Esta entrega debe realizarse máximo el **19 de octubre, 8:00 p.m.** Recuerda registrar en el grupo asignado en Bloque Neón los dos integrantes que presentan este laboratorio, con el fin de habilitar el enlace de entrega.

Si la entrega la hacen después del **19 de octubre, 8:00 p.m.** y antes del **20 de octubre, 2:00 a.m.**, su entrega tendrá una penalización del 30%, lo que significa que será calificada sobre 3.5 y no sobre 5.0. Después de esta última fecha toda entrega tendrá una nota de 0.

## <a name="rubrica"></a> Criterios de evaluación

A continuación se encuentra la rúbrica de calificación que se utiliza para valorar los entregables tomando como base los entregables:

| Actividad | Porcentaje |
|:---|:---:|
| 1. Exploración de los datos. | 5% |
| 2. Propuesta de limpieza y preparación. | 5% |
| 3. Modelos de regresión logística (Cafetería y Restaurante(<20)). | 10% |
| 4. Modelos de árboles de decisión (Cafetería y Restaurante(<20)). | 10% |
| 5. Modelos de Random Forest (Cafetería y Restaurante(<20)). | 10% |
| 6. Evaluación de balanceo de clases (SMOTE) en Restaurante(<20). | 5% |
| 7. Tabla comparativa de los tres algoritmos, argumentando la selección del mejor. | 5% |
| 8. Identificación de las variables más relevantes. | 5% |
| 9. Análisis de resultados con base en las preguntas de la sección F. | 30% |
| 10. Video corto donde se expliquen los elementos más relevantes del ejercicio. | 5% |
| 11. Archivo con resultado de predicciones sobre los datos de prueba compartidos en formato CSV ("Lab3_datos_Prueba.csv"). Se tomará como base el f1-score para ordenar y asignar la nota del grupo. | 5% |
| 12. Registro del uso de IA generativa en el desarrollo del laboratorio, de forma clara, incluyendo los prompts utilizados (ver en la siguiente sección). | 5% |

## <a name="principios"></a> Uso de IAG en actividades del curso ISIS2611

La información que se presenta a continuación también está publicada en Bloque Neón, en la sección del curso **"Uso de la IA generativa"**.

**Principios que rigen el uso de la IA en el curso**

- **Autoría humana.** El estudiante es el responsable final de todo el contenido entregado, incluyendo código, resultados, análisis y conclusiones.

- **Transparencia.** El uso de IAG debe ser claramente declarado, indicando cómo y para qué se utilizó.

- **Pensamiento crítico.** Las respuestas generadas por IAG no deben aceptarse de forma automática; deben ser evaluadas, contrastadas y, cuando sea necesario, corregidas.

- **Aprendizaje y no sustitución.** La IAG debe apoyar el aprendizaje, no reemplazar el proceso de razonamiento, diseño o toma de decisiones por parte del estudiante.

**Reglas prácticas de uso (obligatorias).**

En todas las actividades donde se utilice la IAG, los estudiantes deberán incluir una sección titulada: "Uso de herramientas de IA generativa".

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

**B. Usos no recomendados.** No se considera un uso responsable:

- Copiar y entregar código o texto sin comprensión.
- Utilizar IAG para definir decisiones clave sin justificación.
- Presentar resultados sin saber explicar cómo fueron obtenidos.
- Usar IA para responder evaluaciones individuales no autorizadas.
- Omitir la declaración de uso de IA cuando esta fue utilizada.

**Uso de IAG en la elaboración del enunciado de este laboratorio.**

El equipo docente comprometido con el uso transparente de IAG, declara de forma explícita que, en el contexto de este laboratorio, la IAG fue utilizada únicamente para revisar la redacción del enunciado, la cual posteriormente fue verificada y ajustada, en caso de ser necesario, por parte del equipo docente.

