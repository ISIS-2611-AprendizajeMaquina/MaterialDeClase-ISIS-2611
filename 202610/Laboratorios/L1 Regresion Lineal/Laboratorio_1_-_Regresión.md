# Laboratorio 1 - Exploración, preparación y regresión lineal 

[Caso](#contexto)

[Objetivos](#objetivos)

[Herramientas](#herramientas)

[Conjunto de datos](#datos)

[Actividades a realizar](#actividades)

[Consideraciones](#consideraciones)

[Análisis de resultados](#resultados)

[Entregables](#entregables)

[Criterios de evaluación](#rubrica)

[Uso de IAG en actividades del curso ISIS2611](#principios) 

## <a name="contexto"></a> Caso: AlpesHearth
Las enfermedades cardiovasculares (e.g., infarto de miocardio, ictus e insuficiencia cardiaca) causan más de 20,5 millones de muertes cada año en el mundo, según la "World Heart Federation", de las cuales el 80% son evitables. AlpesHearth busca reducir esta cifra promoviendo cambios en el  estilo de vida --alimentación, actividad física, y manejo del estres. 

Aunque históricamente el riesgo cardiovascular se ha asociado a edades avanzadas, hoy se reconoce que entre los **20 y 25 años** se consolidan hábitos poco saludables que incrementan el riesgo de forma silenciosa -- sedentarismo, mala alimentación, consumo de alcohol, tabaco, estrés crónico, y privación de sueño. La falta de síntomas no significa ausencia de riesgo, sino una **etapa clave para la prevención**, ya que descuidar la salud cardíaca en la adultez temprana compromete el bienestar a largo plazo.

Esto motiva a AlpesHearth a contratarlos para desarrollar un proyecto orientado a **calcular el riesgo cardiovascular de la población** e **identificar los factores más relevantes**, con el fin de implementar campañas preventivas que promuevan la concientización y la reeducación de hábitos para reducir este riesgo creciente y silencioso




## <a name="objetivos"></a> Objetivos

- Aplicar técnicas de regresión para construir un modelo predictivo que permita estimar el riesgo cardiovascular de una persona siguiendo el ciclo de machine learning. 
- Determinar los principales factores de riesgo cardiovascular con base en los datos.
- Aplicar y comprender un modelo de regresión lineal.
- Reconocer posibles sesgos del modelo de aprendizaje de máquina.
- Comunicar de forma clara y sintética los resultados obtenidos.
 


## <a name="herramientas"></a> Herramientas

Durante este laboratorio se trabajará con las siguientes herramientas:

- Librerías de Python para el procesamiento y analisis de datos como: 
    - Pandas
    - Scikit-Learn
    - Matplotlib, Seaborn
- Entorno de desarrollo Visual Studio instalado localmente mediante Anaconda o en la nube mediante Google Colab.


## <a name="datos"></a> Conjunto de datos

El conjunto de datos contiene información de pacientes como edad, peso, altura y algunos laboratorios relacionados con el riesgo cardiovascular. Es importante que revises el diccionario como primer paso para comprender estos datos. Los datos originales han sido tomados a partir de este enlace y han sido modificados para propósitos de este proyecto. El riesgo cardiovascular en los datos está representado por las variables CVD Risk Score,CVD Risk Level. En este laboratorio nos enfocamos en la variable CVD Risk Score (numérica continua).


* [Datos de entrenamiento](data/Datos%20Lab%201.csv)
* [Datos de prueba (no etiquetados)](data/Datos%20Test%20Lab%201.csv)
* [Diccionario de datos](data/DiccPacientes.xlsx)

## <a name="actividades"></a> Actividades a realizar

AlpesHeart desea que usted los apoye en el ciclo de machine learning para realizar este laboratorio por lo que le sugiere las sigueintes actividades:

- **Exploración de los datos:** Utilizando las funcionalidades de la librería pandas. Recuerda que este paso es muy importante para determinar problemas de calidad (por ejemplo, valores ausentes y registros duplicados) y tomar decisiones relacionadas con la preparación de los datos para el algoritmo de aprendizaje.

- **Preparación de datos:** Justificando las decisiones tomadas con base en los resultados obtenidos en el paso anterior y de acuerdo con el modelo que van a construir.

- **Construcción de un modelo de regresión lineal:** Utilizando la métrica RMSE para analizar el desempeño del modelo y con el uso de **pipelines**.

- **Evaluación cuantitativa:** Elaboración de una tabla comparativa mostrando el rendimiento sobre test de dos de los mejores dos modelos analizados (con mejores rendimientos) donde la etapa de preparación y en especial la ingeniería de características realizada son clave, con las métricas RMSE, MAE y R2.

- **Evaluación cualitativa:** Con base en el mejor modelo determinar las variables más importantes para la predicción.Recuerde validar los supuestos de la regresión lineal para esta etapa de interpretación de resultados.

- **Comunicar los resultados:** Elaboración de un video de máximo 3 minutos donde expliques los elementos relevantes del ejercicio realizado. Este video debe estar orientado al ingeniero de machine learning que lidera el grupo de AlpesHearth.

- **Uso del modelo:** Generación de predicciones sobre los datos compartidos que no se encuentran etiquetados utilizando el mejor modelo. Exportar las predicciones en formato CSV utlizando como base el mismo archivo de datos dado.

## <a name="consideraciones"></a> Consideraciones
Al hacer la división entrenamiento – test utiliza un valor de semilla de 42 (ramdon_state) y un porcentaje de 25% para el tamaño del conjunto de prueba (test_size=0.25).  

## <a name="resultados"></a> Análisis de resultados
Una vez construido los modelos, deberías estar en capacidad de responder estas preguntas: 

- ¿Cuál fue el valor de los diferentes coeficientes obtenidos en el mejor modelo? 

- A partir de la tabla comparativa, ¿cuál modelo ofrece el mejor rendimiento sobre el conjunto test? ¿Qué interpretación puedes darles a los valores obtenidos sobre las métricas de rendimiento? 

- ¿Cuáles variables fueron seleccionadas con el modelo seleccionado? A partir de estas, ¿qué interpretación de cara al problema puedes dar? Reflexiona sobre cómo este nuevo conocimiento podría ayudar a tomar decisiones en el contexto del problema. 

- A partir del contexto y los datos compartidos, ¿cómo representar la regresión lineal de forma matemática? Indique el método utilizado y el proceso para resolverlo. 

- En el ciclo de machine learning ¿Qué tipos de sesgo podría afectar los resultados y por qué? Describe dos tipos de sesgo.

## <a name="entregables"></a> Entregables

- Notebook (*.ipynb y *.html) por BloqueNeón con los nombres de los estudiantes. El Notebook debe estar documentado con las justificaciones de las decisiones tomadas en cada paso del ciclo de ML y las respuestas a las preguntas planteadas en el apartado “Análisis de resultados”. Además, deben ser visibles las ejecuciones de cada celda. 
- Archivo "Datos test Lab1.csv" con la etiqueta de las predicciones
- Video explicativo.

Esta entrega debe realizarse máximo el **16 de febrero 20:00**. Recuerda registrar en el grupo GL1, los dos integrantes que presentan este laboratorio, con el fin de habilitar el enlace de entrega.
Si la entrega la hacen después de el **16 de febrero 20:00** y antes del **17 febrero 2:00 a.m.**, su entrega tendrá una penalización del 30%, lo que significa que será calificada sobre 3.5 y no sobre 5.0. Después de esta última fecha toda entrega tendrá una nota de 0.


## <a name="rubrica"></a> Criterios de evaluación

A continuación se encuentra la rúbrica de calificación que se utiliza para valorar los entregables tomando como base los entregables:

| Actividad | Porcentaje |
|:---|:---:|
| 1. Se realiza la exploración y perfilamiento de los datos, describiendo los resultados.  | 10% |
| 2. Se realiza la limpieza y preparación de los datos, justificando las decisiones tomadas.| 10% |
| 3. Se construyen al menos dos modelos de regresión lineal con estrategias de preparación de datos diferentes y justificadas.  | 20% |
| 4. Se construye la tabla comparativa mostrando el rendimiento sobre test de los dos mejores modelos, sobre las métricas RMSE, MAE y R2.   | 10% |
| 5. Se deriva una tabla que muestra la importancia de cada variable con base en el modelo seleccionado.  | 10% |
| 6. Se presenta el análisis de resultados con base en las preguntas de la sección Análisis de resultados.  | 25% |
| 7. Se realiza un video corto donde se expliquen los elementos más relevantes del ejercicio.  | 5% |
| 8. Se registra el uso de IA generativa en el desarrollo del laboratorio, de forma clara y siguiendo los principios establecidos en el curso (ver en la siguiente sección).  | 5% |
| 9. Archivo y resultado de predicciones (columna CVD Risk Score) sobre los datos de prueba compartidos en formato CSV ("Datos Test Lab 1.csv"). Se tomará como base el RMSE para ordenar y asignar la nota del grupo. | ++5% (+ otro 5% de máxima bonificación) |

**++ Los valores de RMSE serán calculados entre todos los grupos del curso. Se toma como base el archivo que entregan con la estimación del valor de CVD Risk Score. Los grupos que obtengan un valor de RMSE que esté dentro del "top 10" reciben un 5% adicional como bonificación.**

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
