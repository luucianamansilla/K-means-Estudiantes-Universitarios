import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import pandas as pd

# =========================================================
# Cargar los datos en un DataFrame 
# =========================================================
estudiantes = [
    {'edad': 42, 'horas_estudio': 2, 'promedio_academico': 8.87},
    {'edad': 26, 'horas_estudio': 8, 'promedio_academico': 9.11},
    {'edad': 56, 'horas_estudio': 5, 'promedio_academico': 7.29},
    {'edad': 29, 'horas_estudio': 14, 'promedio_academico': 7.27},
    {'edad': 43, 'horas_estudio': 8, 'promedio_academico': 8.5},
    {'edad': 34, 'horas_estudio': 10, 'promedio_academico': 4.45},
    {'edad': 51, 'horas_estudio': 3, 'promedio_academico': 6.12},
    {'edad': 22, 'horas_estudio': 12, 'promedio_academico': 4.33},
    {'edad': 47, 'horas_estudio': 6, 'promedio_academico': 7.0},
    {'edad': 38, 'horas_estudio': 9, 'promedio_academico': 4.75},
    {'edad': 60, 'horas_estudio': 2, 'promedio_academico': 9.0},
    {'edad': 31, 'horas_estudio': 11, 'promedio_academico': 2.0},
    {'edad': 45, 'horas_estudio': 4, 'promedio_academico': 8.0},
    {'edad': 27, 'horas_estudio': 13, 'promedio_academico': 3.2},
    {'edad': 50, 'horas_estudio': 5, 'promedio_academico': 7.0},
    {'edad': 36, 'horas_estudio': 7, 'promedio_academico': 5.0},
    {'edad': 40, 'horas_estudio': 6, 'promedio_academico': 6.0},
    {'edad': 24, 'horas_estudio': 15, 'promedio_academico': 3.0},
    {'edad': 55, 'horas_estudio': 3, 'promedio_academico': 9.0},
    {'edad': 33, 'horas_estudio': 10, 'promedio_academico': 3.0},
    {'edad': 48, 'horas_estudio': 4, 'promedio_academico': 8.0},
    {'edad': 28, 'horas_estudio': 12, 'promedio_academico': 2.0},
    {'edad': 52, 'horas_estudio': 5, 'promedio_academico': 7.0},
    {'edad': 30, 'horas_estudio': 11, 'promedio_academico': 2.0},
    {'edad': 46, 'horas_estudio': 6, 'promedio_academico': 6.0},
    {'edad': 35, 'horas_estudio': 9, 'promedio_academico': 4.0},
    {'edad': 41, 'horas_estudio': 7, 'promedio_academico': 5.0},
    {'edad': 23, 'horas_estudio': 14, 'promedio_academico': 1.0},
    {'edad': 53, 'horas_estudio': 3, 'promedio_academico': 8.0},
    {'edad': 32, 'horas_estudio': 10, 'promedio_academico': 3.0},
    {'edad': 49, 'horas_estudio': 4, 'promedio_academico': 8.0},
    {'edad': 25, 'horas_estudio': 13, 'promedio_academico': 2.0},
    {'edad': 54, 'horas_estudio': 5, 'promedio_academico': 7.0},
    {'edad': 37, 'horas_estudio': 8, 'promedio_academico': 4.0},
    {'edad': 39, 'horas_estudio': 7, 'promedio_academico': 5.0},
    {'edad': 21, 'horas_estudio': 15, 'promedio_academico': 9.0},
    {'edad': 58, 'horas_estudio': 2, 'promedio_academico': 9.0},
    {'edad': 44, 'horas_estudio': 6, 'promedio_academico': 6.0},
    {'edad': 29, 'horas_estudio': 12, 'promedio_academico': 2.0},
    {'edad': 50, 'horas_estudio': 5, 'promedio_academico': 7.0},
    {'edad': 34, 'horas_estudio': 9, 'promedio_academico': 3.0},
    {'edad': 42, 'horas_estudio': 7, 'promedio_academico': 6.0},
    {'edad': 26, 'horas_estudio': 14, 'promedio_academico': 3.0},
    {'edad': 57, 'horas_estudio': 3, 'promedio_academico': 9.0},
    {'edad': 30, 'horas_estudio': 11, 'promedio_academico': 2.0},
    {'edad': 47, 'horas_estudio': 4, 'promedio_academico': 7.0},
    {'edad': 31, 'horas_estudio': 10, 'promedio_academico': 3.0},
    {'edad': 45, 'horas_estudio': 6, 'promedio_academico': 6.0},
    {'edad': 27, 'horas_estudio': 13, 'promedio_academico': 1.0},
    {'edad': 55, 'horas_estudio': 5, 'promedio_academico': 8.0}
]

df = pd.DataFrame(estudiantes)

# =========================================================
# 1. Estandarizar los datos 
# =========================================================
X = df[['edad', 'horas_estudio', 'promedio_academico']]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# =========================================================
# 2. Agrupar Estudiantes en 4 segmentos 
# =========================================================
kmeans = KMeans(n_clusters=4, random_state=42)
df['cluster'] = kmeans.fit_predict(X_scaled)

# =========================================================
# 3. Visualizar en 2D: Edad vs Promedio 
# =========================================================
plt.figure(figsize=(10, 6))

# Colores para los 4 clusters 
colores = ['red', 'blue', 'green', 'orange']

# Bucle para graficar cada grupo
for cluster in range(4):
    grupo = df[df['cluster'] == cluster]
    plt.scatter(grupo['edad'], grupo['promedio_academico'], 
                label=f'Segmento {cluster}', color=colores[cluster], s=80)

plt.xlabel('Edad')
plt.ylabel('Promedio Académico')
plt.title('Segmentación de Estudiantes Universitarios (K-Means, 4 Clusters)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()