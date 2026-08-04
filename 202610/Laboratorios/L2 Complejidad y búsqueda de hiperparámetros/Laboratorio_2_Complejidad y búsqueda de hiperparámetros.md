# Laboratorio 2 - Complejidad y búsqueda de hiperparámetros


[Caso](#contexto)

[Objetivos](#objetivos)

[Herramientas](#herramientas)

[Conjunto de datos](#datos)

[Actividades a realizar](#actividades)

[Análisis de resultados](#resultados)

[Entregables](#entregables)

[Criterios de evaluación](#rubrica)

[Uso de IAG en actividades del curso ISIS2611](#principios) 

## <a name="contexto"></a> Caso: AlpesHearth
En el Laboratorio 1, se logró construir para AlpesHearth un primer modelo de regresión lineal para estimar un score de riesgo cardiovascular, así como identificar las variables más influyentes y reflexionar sobre posibles fuentes de sesgo. Sin embargo, el equipo de ingeniería de aprendizaje de máquina considera que este primer acercamiento puede fortalecerse. Ahora, desean evaluar otros enfoques de modelado, como la regresión polinomial y regularizada, además de cuantificar la incertidumbre del modelo utilizando intervalos de confianza que permitan evaluar su estabilidad.


## <a name="objetivos"></a> Objetivos

- Comparar diferentes enfoques de modelado (regresión polinomial y regularizada) para la estimación del riesgo cardiovascular.
- Analizar el impacto de la complejidad sobre la capacidad de generalización de los modelos.
- Aplicar técnicas de selección de modelos para la búsqueda sistemática de hiperparámetros con el fin de seleccionar el modelo con mejor capacidad de generalización.
- Estimar intervalos de confianza para las métricas de evaluación mediante técnicas de remuestreo, con el fin de cuantificar la incertidumbre y estabilidad del modelo.
- Comunicar de forma clara, estructurada y sintética los resultados obtenidos, sustentando las decisiones metodológicas adoptadas.

 
## <a name="herramientas"></a> Herramientas

Durante este laboratorio se trabajará con las siguientes herramientas:

- Librerías de Python para el procesamiento y analisis de datos como: 
    - Pandas
    - Scikit-Learn
    - Matplotlib, Seaborn
- Entorno de desarrollo Visual Studio instalado localmente mediante Anaconda o en la nube mediante Google Colab.


## <a name="datos"></a> Conjunto de datos

En este laboratorio se trabajará con el mismo conjunto de datos utilizado en el Laboratorio 1, pero con la versión resultante del proceso de limpieza y preparación. Por tanto, el énfasis no estará en la exploración ni en el procesamiento de los datos, sino en el modelado, la validación y el análisis del desempeño predictivo de los modelos.


## <a name="actividades"></a> Actividades a realizar

**1. Construcción de un modelo de regresión polinomial.** Implementar un pipeline que incluya la generación de características polinomiales y un modelo de regresión lineal. La búsqueda de hiperparámetros deberá realizarse mediante validación cruzada utilizando GridSearchCV, explorando el grado del polinomio y diferentes estrategias de escalamiento dentro del pipeline. Se deberán reportar las métricas RMSE, MAE y R². El objetivo es analizar cómo varía el desempeño del modelo a medida que aumenta su complejidad e identificar posibles indicios de sobreajuste.

**2. Generación de curvas de validación.** A partir del modelo polinomial anterior, generar curvas de validación que muestren el desempeño del modelo en función del grado del polinomio. Se deberán graficar los errores promedio, y su variabilidad, obtenidos mediante validación cruzada, identificando el punto a partir del cual comienza a evidenciarse sobreajuste. La interpretación deberá realizarse en términos del trade-off sesgo-varianza y del control de la complejidad del modelo.

**3. Construcción de modelos de regresión lineal regularizados.** Implementar pipelines que incorporen regularización L2 (Ridge) y L1 (Lasso), incluyendo el parámetro de penalización como hiperparámetro dentro de la búsqueda con GridSearchCV, así como distintas estrategias de escalamiento. Se deberá comparar el desempeño de los modelos sin regularización, con Ridge y con Lasso, analizando el efecto de la penalización sobre la generalización y la magnitud de los coeficientes. En el caso de Lasso, se deberá examinar qué variables son llevadas a cero y reflexionar sobre sus implicaciones en términos de selección automática de características e interpretabilidad.

**4. Construcción de un modelo de regresión polinomial regularizado.** Implementar un pipeline que combine la generación de características polinomiales con un modelo regularizado (Ridge o Lasso). La búsqueda de hiperparámetros deberá explorar el grado del polinomio, el parámetro de penalización y la estrategia de escalamiento. El desempeño se evaluará mediante RMSE, MAE y R² obtenidos por validación cruzada. El análisis deberá discutir si la regularización permite controlar el sobreajuste al incrementar la complejidad del modelo.

**5. Comparación y selección del mejor modelo.** Con base en los resultados obtenidos (en los puntos 1, 3 y 4), se deberá seleccionar el mejor modelo considerando no solo el valor promedio de la métrica principal sino también su estabilidad (desviación estándar en validación cruzada). Se deberán reportar claramente los mejores hiperparámetros encontrados y argumentar la elección final considerando desempeño, complejidad y estabilidad.

**6. Construcción de intervalos de confianza.** Utilizando el modelo seleccionado en el paso anterior, implementar un procedimiento de bootstrapping sobre el conjunto de test (al menos 500 remuestreos) para estimar intervalos de confianza al 95% de las métricas de desempeño. Se deberá graficar la distribución de los errores y discutir la estabilidad del modelo, la variabilidad observada y la confiabilidad de las predicciones.

**7. Comunicar los resultados.** Elaboración de un video de máximo 3 minutos donde expliques los elementos relevantes del ejercicio realizado. Este video debe estar orientado al ingeniero de machine learning que lidera el grupo de AlpesHearth.


## <a name="resultados"></a> Análisis de resultados
Una vez construido los modelos, deberías estar en capacidad de responder estas preguntas: 

**Análisis cuantitatvo.**

- ¿Cuál modelo obtuvo el mejor desempeño en el conjunto de test?

- ¿Coincide el mejor desempeño en test con el mejor promedio en validación cruzada? Si no coincide, ¿cuál puede ser la explicación?

- ¿El modelo con mejor métrica promedio es necesariamente el más adecuado? Justifica considerando también la desviación estándar del desempeño.

- Con base en las curvas de validación, ¿cómo cambia el error a medida que aumenta la complejidad? ¿En qué punto se evidencia sobreajuste?

- ¿Cómo afecta la regularización la magnitud y estabilidad de los coeficientes?

- ¿Los intervalos de confianza obtenidos mediante bootstrapping sugieren estabilidad o alta variabilidad en el desempeño? ¿Qué implicaciones tiene esto?

**Análisis cualitativo.**

- ¿Qué variables fueron seleccionadas como más relevantes por el modelo Lasso?

- ¿Qué interpretación práctica tienen los coeficientes del modelo final en el contexto del riesgo cardiovascular?

- ¿Existen diferencias relevantes entre el modelo más preciso y el más interpretable?

- ¿Qué decisiones estratégicas podría tomar AlpesHearth a partir de los resultados obtenidos?

- ¿Mayor precisión implica necesariamente mayor valor para la organización? 

- ¿Un modelo más complejo necesariamente genera mayor valor empresarial? Discute considerando interpretabilidad, estabilidad y costo de implementación.

**Reflexión conceptual.**

- ¿Qué relación observas entre complejidad del modelo, capacidad de generalización y estabilidad del desempeño?

- ¿Qué fuentes de sesgo podrían estar presentes en los datos o en el proceso de modelado?

- Si el tamaño de muestra fuera mayor, ¿esperarías cambios en la estabilidad de los modelos? Explique.


## <a name="entregables"></a> Entregables

- Notebook (*.ipynb y *.html) por BloqueNeón con los nombres de los estudiantes. El Notebook debe estar documentado con las justificaciones de las decisiones tomadas en cada paso del ciclo de ML y las respuestas a las preguntas planteadas en el apartado “Análisis de resultados”. Además, deben ser visibles las ejecuciones de cada celda. 
- Video explicativo.

Esta entrega debe realizarse máximo el **2 de marzo 20:00**. Recuerda registrar en el grupo GL2, los dos integrantes que presentan este laboratorio, con el fin de habilitar el enlace de entrega.
Si la entrega la hacen después de el **2 de marzo 20:00** y antes del **3 marzo 2:00 a.m.**, su entrega tendrá una penalización del 30%, lo que significa que será calificada sobre 3.5 y no sobre 5.0. Después de esta última fecha toda entrega tendrá una nota de 0.


## <a name="rubrica"></a> Criterios de evaluación

A continuación se encuentra la rúbrica de calificación que se utiliza para valorar los entregables tomando como base los entregables:

| Actividad | Porcentaje |
|:---|:---:|
| 1. Se construye el modelo de regresión polinomial, justificando las decisiones tomadas.  | 15% |
| 2. Se construyen los dos modelos de regresión regularizada (Ridge y Lasso), justificando las decisiones tomadas.| 15% |
| 3. Se construye el modelo de regresión polinomial regularizado, justificando las decisiones tomadas.  | 10% |
| 4. Se deriva una tabla comparativa de los resultados de los modelos y se argumenta la selección del mejor.   | 5% |
| 5. Se construyen los intervalos de confianza para el mejor modelo.  | 10% |
| 6. Se presenta el análisis de resultados con base en las preguntas de la sección Análisis de resultados.  | 35% |
| 7. Se realiza un video corto donde se expliquen los elementos más relevantes del ejercicio.  | 5% |
| 8. Se registra el uso de IA generativa en el desarrollo del laboratorio, de forma clara y siguiendo los principios establecidos en el curso (ver en la siguiente sección).  | 5% |


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
