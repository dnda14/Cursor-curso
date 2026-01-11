import pandas as pd
import random
from datetime import datetime, timedelta

# Generar datos sintéticos de ventas
productos = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
precios_base = {'A': 10.0, 'B': 20.0, 'C': 15.0, 'D': 25.0, 'E': 30.0, 'F': 12.0, 'G': 18.0, 'H': 22.0}

# Generar fechas desde enero 2025 hasta marzo 2025
fecha_inicio = datetime(2025, 1, 1)
fecha_fin = datetime(2025, 3, 31)

ventas = []
fecha_actual = fecha_inicio

while fecha_actual <= fecha_fin:
    # Generar entre 2 y 8 ventas por día
    num_ventas_dia = random.randint(2, 8)
    
    for _ in range(num_ventas_dia):
        producto = random.choice(productos)
        cantidad = random.randint(1, 5)
        precio = precios_base[producto]
        
        ventas.append({
            'fecha': fecha_actual.strftime('%Y-%m-%d'),
            'producto': producto,
            'cantidad': cantidad,
            'precio': precio
        })
    
    fecha_actual += timedelta(days=1)

# Crear DataFrame y guardar
df = pd.DataFrame(ventas)
df.to_csv('ventas.csv', index=False)

print(f"✅ Datos generados: {len(df)} ventas")
print(f"📅 Rango de fechas: {df['fecha'].min()} a {df['fecha'].max()}")
print(f"📦 Productos: {df['producto'].unique()}")
print("\nPrimeras 5 filas:")
print(df.head())
