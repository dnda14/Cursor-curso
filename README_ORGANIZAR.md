# 📁 Organizador de Archivos

Script en Python para organizar automáticamente archivos en carpetas según su extensión.

## 🚀 Características

- ✅ Organiza archivos por categorías (Imágenes, Documentos, Videos, Música, etc.)
- ✅ Manejo inteligente de duplicados
- ✅ Excluye automáticamente el script del proceso
- ✅ Interfaz de línea de comandos con argparse
- ✅ Estadísticas detalladas al finalizar
- ✅ Seguro: no sobreescribe archivos sin confirmación (opcional)

## 📋 Categorías Predefinidas

- **Imagenes**: .png, .jpg, .jpeg, .gif, .bmp, .svg, .webp, .ico
- **Documentos**: .pdf, .doc, .docx, .txt, .xlsx, .xls, .ppt, .pptx, .odt, .rtf
- **Videos**: .mp4, .avi, .mkv, .mov, .wmv, .flv, .webm, .m4v
- **Musica**: .mp3, .wav, .flac, .aac, .ogg, .m4a, .wma
- **Archivos_Comprimidos**: .zip, .rar, .7z, .tar, .gz, .bz2
- **Codigo**: .py, .js, .html, .css, .java, .cpp, .c, .php, .rb, .go
- **Ejecutables**: .exe, .msi, .deb, .rpm, .dmg, .app
- **Datos**: .csv, .json, .xml, .sql, .db, .sqlite
- **Otros**: Cualquier archivo que no coincida con las categorías anteriores

## 💻 Uso

### Uso Básico

```bash
# Organizar archivos en la carpeta Descargas (por defecto)
python organizar.py

# Organizar archivos en una carpeta específica
python organizar.py -c /ruta/a/carpeta

# Organizar y renombrar archivos duplicados automáticamente
python organizar.py --duplicados

# No excluir el script organizar.py del proceso
python organizar.py --no-excluir-script
```

### Opciones Disponibles

- `-c, --carpeta`: Especifica la carpeta a organizar (por defecto: Descargas del usuario)
- `--duplicados`: Renombra archivos duplicados en lugar de saltarlos
- `--no-excluir-script`: No excluye el script organizar.py del proceso

### Ejemplos

```bash
# Organizar Descargas
python organizar.py

# Organizar carpeta específica
python organizar.py -c ~/Documentos/Archivos

# Organizar con manejo de duplicados
python organizar.py -c ~/Downloads --duplicados
```

## 🧪 Pruebas

Para probar el script sin afectar archivos reales:

```bash
# 1. Crear archivos de prueba
python crear_archivos_prueba.py

# 2. Organizar la carpeta de prueba
python organizar.py -c carpeta_prueba

# 3. Verificar resultados
ls -R carpeta_prueba/
```

## ⚠️ Precauciones

- **Prueba primero**: Usa la carpeta de prueba antes de organizar carpetas importantes
- **Backup**: Considera hacer una copia de seguridad antes de organizar carpetas con archivos importantes
- **Duplicados**: Por defecto, el script salta archivos duplicados. Usa `--duplicados` para renombrarlos automáticamente

## 🔧 Personalización

Puedes modificar las categorías editando el diccionario `CATEGORIAS` en `organizar.py`:

```python
CATEGORIAS = {
    "Mi_Categoria": [".ext1", ".ext2", ".ext3"],
    # ... más categorías
}
```

## 📊 Salida

El script muestra:
- Progreso en tiempo real (archivos movidos)
- Resumen final con estadísticas
- Archivos por categoría
- Errores si los hay

## 🛠️ Requisitos

- Python 3.6+
- Solo librerías estándar (no requiere instalación de paquetes externos)

## 📝 Notas

- El script solo organiza archivos en el nivel raíz de la carpeta especificada
- No organiza recursivamente subcarpetas
- Los archivos se mueven (no se copian), así que ten cuidado
- El script se excluye automáticamente del proceso para evitar moverse a sí mismo
