import re
from collections import Counter

archivo = input("Introduce la ruta del archivo de texto: ")

try:
    with open(archivo, "r", encoding="utf-8") as f:
        contenido = f.read()
except FileNotFoundError:
    print(f"El archivo {archivo} no existe")
    exit(1)
except Exception as e:
    print(f"Error al leer el archivo: {e}")
    exit(1)

# Separar el contenido en palabras
palabras = re.findall(r"\w+", contenido.lower())
total_palabras = len(palabras)
print(f"Total de palabras: {total_palabras}")

# Contar palabras más frecuentes
contador = Counter(palabras)
mas_comunes = contador.most_common(10)

print("Palabras más frecuentes:")   
for palabra, freq in mas_comunes:
    print(f"{palabra}: {freq}")

