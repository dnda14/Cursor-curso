#!/usr/bin/env python3
"""
Script auxiliar para crear archivos de prueba para organizar.py
"""

from pathlib import Path
import os

def crear_archivos_prueba(carpeta="carpeta_prueba"):
    """Crea una carpeta con archivos de prueba de diferentes tipos."""
    carpeta_prueba = Path(carpeta)
    carpeta_prueba.mkdir(exist_ok=True)
    
    # Archivos de prueba
    archivos_prueba = {
        "foto1.jpg": "Imagen JPEG",
        "imagen.png": "Imagen PNG",
        "documento.pdf": "Documento PDF",
        "texto.txt": "Archivo de texto",
        "video.mp4": "Video MP4",
        "cancion.mp3": "Audio MP3",
        "codigo.py": "Script Python",
        "datos.csv": "Datos CSV",
        "comprimido.zip": "Archivo ZIP",
        "programa.exe": "Ejecutable",
        "sin_extension": "Archivo sin extensión",
    }
    
    print(f"📁 Creando archivos de prueba en: {carpeta_prueba}")
    print("=" * 60)
    
    for nombre, contenido in archivos_prueba.items():
        archivo = carpeta_prueba / nombre
        archivo.write_text(contenido)
        print(f"✅ Creado: {nombre}")
    
    print(f"\n✅ {len(archivos_prueba)} archivos creados en {carpeta_prueba}")
    print(f"\nPara probar organizar.py, ejecuta:")
    print(f"  python organizar.py -c {carpeta_prueba}")

if __name__ == "__main__":
    crear_archivos_prueba()
