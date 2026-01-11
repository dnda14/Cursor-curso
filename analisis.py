import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Backend no interactivo para evitar warnings
import matplotlib.pyplot as plt

# Leer el CSV
df = pd.read_csv('datos.csv')

print("Datos cargados:")
print(df.head())
print("\n" + "="*50 + "\n")

# Calcular estadísticas para cada columna
print("Estadísticas de col1:")
print(f"  Media: {df['col1'].mean():.2f}")
print(f"  Mediana: {df['col1'].median():.2f}")
print(f"  Desviación estándar: {df['col1'].std():.2f}")

print("\nEstadísticas de col2:")
print(f"  Media: {df['col2'].mean():.2f}")
print(f"  Mediana: {df['col2'].median():.2f}")
print(f"  Desviación estándar: {df['col2'].std():.2f}")

# Traza un scatter plot de col1 vs. col2
plt.figure(figsize=(8, 6))
plt.scatter(df['col1'], df['col2'], alpha=0.7, s=100, color='blue', edgecolors='black', linewidth=0.5)
plt.xlabel('col1', fontsize=12)
plt.ylabel('col2', fontsize=12)
plt.title('Gráfica de Dispersión: col1 vs. col2', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.tight_layout()

# Guardar la figura
plt.savefig('grafica_dispersion.png', dpi=150, bbox_inches='tight')
print("\nGráfica guardada como 'grafica_dispersion.png'")
plt.close()  # Cerrar la figura para liberar memoria
