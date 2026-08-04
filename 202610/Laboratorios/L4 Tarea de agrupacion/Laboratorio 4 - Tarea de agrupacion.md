# Laboratorio 4 - Tarea de agrupación

[Caso](#contexto)

[Objetivos](#objetivos)

[Herramientas](#herramientas)

[Conjunto de datos](#datos)

[Actividades a realizar](#actividades)

[Análisis de resultados](#resultados)

[Entregables](#entregables)

[Criterios de evaluación](#rubrica)

[Uso de IAG en actividades del curso ISIS2611](#principios) 


## <a name="contexto"></a> Caso


VuelaAlpes es una aerolínea con concentración en los Alpes y con un gran número de vuelos entrantes y salientes relacionados con destinos internacionales. 
Luego de dos años de baja productividad y con el ánimo de mejorar el servicio que da a sus pasajeros, decidió iniciar un proceso de mejora continua realizando de una serie de encuestas a pasajeros que pueden guiar las decisiones que deben tomar en el corto plazo.

A partir de la información recolectada, VuelaAlpes ha decido emprender un proyecto de aprendizaje automático cuyo objetivo es la aplicación de técnicas de agrupación para identificar patrones de comportamiento que permitan caracterizar diferentes pasajeros. La expectativa de la empresa es que los resultados de este estudio generen beneficios en tres dimensiones principales: (i) innovación, mediante el análisis de los elementos que afectan el nivel de satisfacción de los pasajeros, poder definir ofertas que incluyen precios competentes o nuevos servicios; (ii) focalización de la capacitación de la tripulación de vuelo, a partir de los hallazgos que están afectando negativamente la experiencia de los pasajeros en sus vuelos, definir casos que puedan permitirles reflexionar sobre aspectos que deben tener en cuenta según las características de los pasajeros; (iii) calidad mediante la identificación de características de los pasajeros y los vuelos a realizar donde se deben ofrecer nuevos servicios que permitan diferenciarse de otras aerolíneas y aumentar la relación de precio-calidad.

Para llevar a cabo este proyecto, la empresa nos ha contratado como científicos de datos, proporcionándonos no solo el conjunto de datos generado, sino también la documentación correspondiente a la descripción detallada de cada atributo (diccionario).


## <a name="objetivos"></a> Objetivos

- Aplicar el proceso de aprendizaje para resolver una tarea de agrupación, desde la preparación de los datos hasta la interpretación de los resultados. 
- Comparar diferentes algoritmos de clústering para resolver el objetivo del caso de estudio. 
- Derivar conclusiones a partir de los mejores grupos identificados, que sean útiles para la organización.
- Comunicar los hallazgos encontrados a la organización, explicando por qué tienen valor para la empresa los hallazgos identificados.


## <a name="herramientas"></a> Herramientas

Durante este laboratorio trabajaremos con las siguientes herramientas:

 - Python
	 - Distribución sugerida: [Anaconda](https://www.continuum.io/downloads) 
		 - La versión de Anaconda es 4.4
		 - La versión usada es la de python 2.7, usar python 3 no debería requerir muchos cambios.
	 - Ambiente de desarrollo
	   	 - JupyterLab
	   	 - Google Colab
	 - Librerías
	 	 - Pandas
		 - Scikit-learn
		 - Matplot
		 - Seaborn 

## <a name="datos"></a> Conjunto de datos

VuelaAlpes nos proporcionó un conjunto de datos con información histórica de pasajeros que han viajado con la aerolínea. Dentro de la información compartida se tienen datos demográficos del pasajero, características del vuelo y calificación de diferentes criterios de calidad. Los datos se tomaron de este [enlace](https://www.kaggle.com/datasets/teejmahal20/airline-passenger-satisfaction) y se adaptaron para este laboratorio. A continuación, encuentran los datos ajustados y el diccionario de datos que los describe.

*[Datos de entrenamiento](Datos_VuelaAlpes.csv)

*[Diccionario de datos](Diccionario%20VuelaAlpes.xlsx)



## <a name="actividades"></a> Actividades a realizar 

VuelaAlpesdesea que usted los apoye en la construcción del modelo de agrupación previamente descrito con base en las etapas de la metodología "CRISP-ML":

1. **Exploración de los datos** para identificar problemas de calidad y otras características.

2. **Propuesta de limpieza y Preparación de datos:** justificando las decisiones tomadas con base en los resultados obtenidos en el paso anterior y de acuerdo con los algoritmos que se van a utilizar. 

3. **Modelamiento:** Describir y aplicar tres algoritmos distintos de agrupación. Incluya la búsqueda de hiperparámetros y estructure el proceso mediante el uso de pipelines, de manera que el preprocesamiento y el modelo queden integrados en un flujo de trabajo reproducible y ordenado. 

4. **Evaluación cuantitativa:** La calidad desde el punto de vista cuantitativo puede validarse utilizando diferentes métricas intrínsecas, como por ejemplo, el coeficiente de silueta.Construya una tabla de comparación de los tres algoritmos, la cual debe incluir hiperparámetros optimizados, valores y métrica cuantitativa de evaluación.
    
5. **Evaluación cualitativa:** Una vez realizada la validación cuantitativa, se debe hacer una descripción de los grupos obtenidos y relacionarlo con el objetivo que tiene la organización para determinar la utilidad del resultado obtenido, y su posible uso.

6. **Elaboración de un video** de máximo 3 minutos donde se expliquen los elementos relevantes del ejercicio realizado. Este video debe estar orientado a la organización VuelaAlpes.


## <a name="resultados"></a> Análisis de resultados
Una vez realizados los diferentes pasos del laboratorio, deberías estar en capacidad de responder estas preguntas:

1. ¿Qué restricciones tiene cada uno de los algoritmos seleccionados? ¿Cómo afectan estas restricciones la calidad de la solución obtenida?
2. ¿Qué criterios son importantes para la selección del algoritmo?
3. ¿Cómo medir la calidad del modelo construido? ¿Cómo saber que el modelo construido tiene una buena calidad?  
4. ¿Cómo varía la calidad de la solución obtenida si se aplican diferentes algoritmos?
5. ¿Cómo interpretar el resultado de la ejecución de los algoritmos de agrupación seleccionados?


## <a name="entregables"></a> Entregables
- Cuaderno ejecutado(*.ipynb y *.html), por BloqueNeón con los nombres de los estudiantes. 
- El cuaderno debe estar documentado con las justificaciones de las decisiones tomadas en cada paso del ciclo de ML y las respuestas a las preguntas planteadas en el apartado “Análisis de resultados”. Además, deben ser visibles las ejecuciones de cada celda.
- Incluir el uso que le dieron a la IA generativa en el desarrollo del laboratorio.
   
Esta entrega debe realizarse máximo el 11 de mayo 20:00. Recuerda registrar en el grupo GL4, los dos integrantes que presentan este laboratorio, con el fin de habilitar el enlace de entrega. Si la entrega la hacen después de el 11 de mayo 20:00 y antes del 12 de mayo 2:00 a.m., su entrega tendrá una penalización del 30%, lo que significa que será calificada sobre 3.5 y no sobre 5.0. Después de esta última fecha toda entrega tendrá una nota de 0.


## <a name="rubrica"></a> Criterios de evaluación

A continuación se encuentra la rúbrica de calificación  que se utiliza para valorar los entregables tomando como base los entregables.

| Actividad | Porcentaje |
|:---:|:---:|
| 1. Exploración de los datos y propuesta de limpieza y preparación. | 15% |
| 2. Descripción y aplicación de tres algoritmos de agrupación | 30% |
| 3. Tabla comparativa de los resultados de los modelos y se argumenta la selección del mejor. | 15% |
| 4. Evaluación cualitativa (interpretación de los resultados obtenidos) | 15% |
| 5. Respuesta a las preguntas planteadas en el laboratorio | 10% |
| 6. Video corto donde se expliquen los elementos más relevantes del ejercicio.| 10% |
| 7. Registro del uso de IA generativa en el desarrollo del laboratorio, de forma clara, incluyendo los prompts utilizados (ver en la siguiente sección).| 5% |

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



