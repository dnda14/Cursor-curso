#!/usr/bin/env python3
"""
Script para organizar archivos en carpetas según su extensión.
"""

import argparse
from pathlib import Path
from collections import defaultdict

# Definir categorías de extensiones
CATEGORIAS = {
    "Imagenes": [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".svg", ".webp", ".ico"],
    "Documentos": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".xls", ".ppt", ".pptx", ".odt", ".rtf"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm", ".m4v"],
    "Musica": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a", ".wma"],
    "Archivos_Comprimidos": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2"],
    "Codigo": [".py", ".js", ".html", ".css", ".java", ".cpp", ".c", ".php", ".rb", ".go"],
    "Ejecutables": [".exe", ".msi", ".deb", ".rpm", ".dmg", ".app"],
    "Datos": [".csv", ".json", ".xml", ".sql", ".db", ".sqlite"],
}

CATEGORIA_OTROS = "Otros"


def crear_mapa_extensiones():
    """Crea un diccionario que mapea extensión -> categoría."""
    extension_a_categoria = {}
    for categoria, extensiones in CATEGORIAS.items():
        for ext in extensiones:
            extension_a_categoria[ext.lower()] = categoria
    return extension_a_categoria


def obtener_categoria(archivo, extension_a_categoria):
    """Determina la categoría de un archivo según su extensión."""
    ext = archivo.suffix.lower()
    return extension_a_categoria.get(ext, CATEGORIA_OTROS)


def manejar_duplicado(archivo, destino):
    """Maneja archivos duplicados añadiendo un número al nombre."""
    if destino.exists():
        # Obtener nombre sin extensión y extensión
        stem = destino.stem
        suffix = destino.suffix
        parent = destino.parent
        
        # Buscar un nombre disponible
        contador = 1
        while destino.exists():
            nuevo_nombre = f"{stem}_{contador}{suffix}"
            destino = parent / nuevo_nombre
            contador += 1
    
    return destino


def organizar_archivos(carpeta_objetivo, mover_duplicados=False, excluir_script=True):
    """
    Organiza archivos en la carpeta objetivo según su extensión.
    
    Args:
        carpeta_objetivo: Path de la carpeta a organizar
        mover_duplicados: Si True, renombra archivos duplicados en lugar de saltarlos
        excluir_script: Si True, excluye el script organizar.py del proceso
    """
    carpeta_objetivo = Path(carpeta_objetivo)
    
    if not carpeta_objetivo.exists():
        print(f"❌ Error: La carpeta {carpeta_objetivo} no existe.")
        return
    
    if not carpeta_objetivo.is_dir():
        print(f"❌ Error: {carpeta_objetivo} no es un directorio.")
        return
    
    print(f"📁 Organizando archivos en: {carpeta_objetivo}")
    print("=" * 60)
    
    # Crear mapa de extensiones
    extension_a_categoria = crear_mapa_extensiones()
    
    # Listar archivos (solo archivos, no directorios)
    archivos = [f for f in carpeta_objetivo.iterdir() if f.is_file()]
    
    # Excluir el script si está en la misma carpeta
    if excluir_script:
        nombre_script = Path(__file__).name
        archivos = [f for f in archivos if f.name != nombre_script]
    
    if not archivos:
        print("ℹ️  No se encontraron archivos para organizar.")
        return
    
    # Estadísticas
    estadisticas = defaultdict(int)
    movidos = 0
    errores = 0
    
    # Procesar cada archivo
    for archivo in archivos:
        try:
            categoria = obtener_categoria(archivo, extension_a_categoria)
            destino_dir = carpeta_objetivo / categoria
            
            # Crear carpeta si no existe
            destino_dir.mkdir(exist_ok=True)
            
            # Ruta destino del archivo
            destino_archivo = destino_dir / archivo.name
            
            # Manejar duplicados
            if destino_archivo.exists() and not mover_duplicados:
                print(f"⚠️  Saltado (duplicado): {archivo.name}")
                errores += 1
                continue
            
            if destino_archivo.exists() and mover_duplicados:
                destino_archivo = manejar_duplicado(archivo, destino_archivo)
            
            # Mover archivo
            archivo.rename(destino_archivo)
            print(f"✅ Movido: {archivo.name} → {categoria}/")
            
            estadisticas[categoria] += 1
            movidos += 1
            
        except Exception as e:
            print(f"❌ Error moviendo {archivo.name}: {e}")
            errores += 1
    
    # Mostrar resumen
    print("\n" + "=" * 60)
    print("📊 RESUMEN")
    print("=" * 60)
    print(f"✅ Archivos movidos: {movidos}")
    if errores > 0:
        print(f"⚠️  Archivos con problemas: {errores}")
    print("\nArchivos por categoría:")
    for categoria, cantidad in sorted(estadisticas.items()):
        print(f"  {categoria}: {cantidad} archivo(s)")


def main():
    """Función principal con argumentos de línea de comandos."""
    parser = argparse.ArgumentParser(
        description="Organiza archivos en carpetas según su extensión.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos:
  python organizar.py                          # Organiza Descargas
  python organizar.py -c /ruta/carpeta         # Organiza carpeta específica
  python organizar.py --duplicados             # Renombra duplicados automáticamente
        """
    )
    
    parser.add_argument(
        "-c", "--carpeta",
        type=str,
        default=str(Path.home() / "Downloads"),
        help="Carpeta a organizar (por defecto: Descargas del usuario)"
    )
    
    parser.add_argument(
        "--duplicados",
        action="store_true",
        help="Renombrar archivos duplicados en lugar de saltarlos"
    )
    
    parser.add_argument(
        "--no-excluir-script",
        action="store_true",
        help="No excluir el script organizar.py del proceso"
    )
    
    args = parser.parse_args()
    
    # Confirmar antes de ejecutar (solo si no es Descargas por defecto y es interactivo)
    carpeta = Path(args.carpeta)
    if carpeta != Path.home() / "Downloads":
        try:
            respuesta = input(f"¿Organizar archivos en {carpeta}? (s/n): ")
            if respuesta.lower() != 's':
                print("Operación cancelada.")
                return
        except EOFError:
            # Modo no interactivo, continuar sin confirmación
            print(f"Organizando archivos en {carpeta} (modo no interactivo)...")
    
    organizar_archivos(
        carpeta,
        mover_duplicados=args.duplicados,
        excluir_script=not args.no_excluir_script
    )


if __name__ == "__main__":
    main()
