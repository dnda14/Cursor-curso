import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Backend no interactivo
import matplotlib.pyplot as plt

# 1. Cargar datos del CSV
print("=" * 60)
print("ANÁLISIS DE VENTAS")
print("=" * 60)

df = pd.read_csv('ventas.csv', parse_dates=['fecha'])

# Verificar tipos de datos
print("\n📊 Información del dataset:")
print(f"Total de registros: {len(df)}")
print(f"\nTipos de datos:")
print(df.dtypes)
print(f"\nPrimeras filas:")
print(df.head())

# Asegurar que cantidad y precio son numéricos
df['cantidad'] = pd.to_numeric(df['cantidad'])
df['precio'] = pd.to_numeric(df['precio'])

# 2. Calcular ventas totales por mes
print("\n" + "=" * 60)
print("VENTAS POR MES")
print("=" * 60)

# Crear columna de mes
df['mes'] = df['fecha'].dt.to_period('M')

# Calcular ingresos por venta
df['ingreso'] = df['cantidad'] * df['precio']

# Agrupar por mes y sumar ingresos
ventas_por_mes = df.groupby('mes')['ingreso'].sum().sort_index()

print("\nVentas totales por mes:")
print(ventas_por_mes.to_frame())
print(f"\nTotal general: {ventas_por_mes.sum():.2f} €")

# 3. Determinar producto más vendido y con mayor ingresos
print("\n" + "=" * 60)
print("ANÁLISIS POR PRODUCTO")
print("=" * 60)

# Agrupar por producto
ventas_prod = df.groupby('producto').agg({
    'cantidad': 'sum',
    'ingreso': 'sum'
}).sort_values('ingreso', ascending=False)

print("\nResumen por producto:")
print(ventas_prod)

# Producto más vendido en cantidad
mas_vendido = ventas_prod['cantidad'].idxmax()
cantidad_total = ventas_prod.loc[mas_vendido, 'cantidad']

# Producto con mayores ingresos
mayor_ingreso = ventas_prod['ingreso'].idxmax()
ingreso_total = ventas_prod.loc[mayor_ingreso, 'ingreso']

print(f"\n🏆 Producto más vendido (en unidades): {mas_vendido}")
print(f"   Total: {cantidad_total} unidades")

print(f"\n💰 Producto con mayores ingresos: {mayor_ingreso}")
print(f"   Total: {ingreso_total:.2f} €")

# 4. Graficar ventas por mes
print("\n" + "=" * 60)
print("GENERANDO GRÁFICOS...")
print("=" * 60)

# Convertir índice Period a string para mejor visualización
ventas_por_mes_str = ventas_por_mes.copy()
ventas_por_mes_str.index = ventas_por_mes_str.index.astype(str)

plt.figure(figsize=(10, 6))
ventas_por_mes_str.plot(kind='bar', color='steelblue', edgecolor='black')
plt.title("Ventas por Mes", fontsize=16, fontweight='bold')
plt.xlabel("Mes", fontsize=12)
plt.ylabel("Ventas (€)", fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig("ventas_por_mes.png", dpi=150, bbox_inches='tight')
print("✅ Gráfico guardado: ventas_por_mes.png")
plt.close()

# 5. Graficar top 5 productos por ingresos
top5 = ventas_prod.nlargest(5, 'ingreso')

plt.figure(figsize=(10, 6))
plt.bar(top5.index, top5['ingreso'], color='coral', edgecolor='black')
plt.title("Top 5 Productos por Ingresos", fontsize=16, fontweight='bold')
plt.ylabel("Ingresos (€)", fontsize=12)
plt.xlabel("Producto", fontsize=12)
plt.xticks(rotation=0)
plt.grid(axis='y', alpha=0.3)

# Añadir valores en las barras
for i, v in enumerate(top5['ingreso']):
    plt.text(i, v, f'{v:.0f}€', ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.savefig("top5_productos.png", dpi=150, bbox_inches='tight')
print("✅ Gráfico guardado: top5_productos.png")
plt.close()

print("\n" + "=" * 60)
print("✅ ANÁLISIS COMPLETADO")
print("=" * 60)
print("\nArchivos generados:")
print("  - ventas_por_mes.png")
print("  - top5_productos.png")
