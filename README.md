# Segmentación de Estudiantes Universitarios con K-Means

## 👥 Datos del trabajo

  * **Integrantes:**
    * Yapura Valentina
    * Mansilla Angeles
    * Bejerano Thomas
    * Lugo Facundo
  * **Materia:** Procesamiento de Aprendizaje Automático
  * **Carrera:** Tecnicatura Superior en Ciencia de Datos e Inteligencia Artificial
  * **Profesora:** Yanina Scudero

* * *

## 📌 Descripción

Programa en Python que utiliza el algoritmo de clustering **K-Means** para agrupar a 50 estudiantes universitarios simulados en **cuatro segmentos** según su:
  * Edad
  * Horas de estudio semanales
  * Promedio académico

**Datos:** Set de datos simulado provisto por la cátedra (50 registros).

## 🛠️ Tecnologías

  * Python 3
  * pandas
  * scikit-learn (`KMeans`, `StandardScaler`)
  * matplotlib

## 📂 Archivos del Repositorio

  * `estudiantesUniversitarios.py`: Script con el código fuente de la solución.
  * `grafico_estudiantes.png`: Gráfico de dispersión generado por el programa.
  * `Informe Segmentación de Estudiantes Universitarios con K-Means.pdf`: Documento con el análisis completo de los resultados.
  * `README.md`: Archivo de presentación.

## 🧠 Cómo funciona

  1. **Carga de datos:** se arma un `DataFrame` con las columnas `edad`, `horas_estudio` y `promedio_academico`.
  2. **Estandarización:** se aplica `StandardScaler` para que las tres variables tengan la misma escala y el algoritmo no se vea sesgado por los valores numéricos más grandes (como la edad).
  3. **K-Means:** se aplica `KMeans(n_clusters=4, random_state=42)` sobre los datos escalados.
  4. **Resultados:** se agrega la columna `cluster` al DataFrame original.
  5. **Gráfico:** dispersión en 2D (Edad en el eje X, Promedio en el eje Y) con colores distintos para cada uno de los 4 segmentos.

## 🚀 Cómo ejecutar

    pip install pandas scikit-learn matplotlib
    python estudiantesUniversitarios.py

## 📊 Resultados

| Segmento | Descripción del Perfil | Edad Prom. | Horas Estudio Prom. | Promedio Prom. |
| :--- | :--- | :--- | :--- | :--- |
| **0 (Rojo)** | Mayores con Alto Rendimiento | ~52 años | ~3.5 hs | ~8.4 |
| **1 (Azul)** | Jóvenes con Bajo Rendimiento | ~25 años | ~12.8 hs | ~2.2 |
| **2 (Verde)** | Jóvenes con Alto Rendimiento (Casos aislados) | ~24 años | ~13 hs | ~8.7 |
| **3 (Naranja)** | Adultos con Rendimiento Medio | ~42 años | ~7.1 hs | ~5.8 |

## 🔎 Conclusiones

  * **No hay correlación directa entre horas de estudio y promedio:** El grupo que más horas estudia (Segmento 1 - Azul, ~13 hs) es el que tiene los promedios más bajos (~2.2).
  * **La edad es un factor clave:** Los estudiantes mayores (Segmento 0 - Rojo) logran promedios altos (~8.4) estudiando muy pocas horas (~3.5). 
  * **Casos particulares:** El Segmento 2 (Verde) agrupa a muy pocos estudiantes jóvenes que, a pesar de su edad, logran un rendimiento académico sobresaliente.
  * Como el algoritmo agrupa usando las 3 variables pero el gráfico solo muestra 2 (Edad vs Promedio), la interpretación de los segmentos requiere analizar la tabla de promedios para entender el impacto real de las horas de estudio.
