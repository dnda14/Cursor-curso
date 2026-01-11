# 🚀 Cursor Curso - Proyectos de Python

Este repositorio contiene cuatro proyectos completos desarrollados con Python, cada uno demostrando diferentes aspectos de programación y desarrollo.

## 📋 Proyectos Incluidos

### 1. 📝 Gestor de Tareas (Flask Web App)
**Archivos principales:** `app.py`, `templates/index.html`

Aplicación web completa desarrollada con Flask para gestionar tareas (to-do list).

**Características:**
- ✅ Agregar nuevas tareas
- ✅ Marcar tareas como completadas
- ✅ Persistencia en archivo JSON
- ✅ Interfaz moderna y responsive
- ✅ Ordenamiento automático (incompletas primero)

**Ejecución:**
```bash
# Activar entorno virtual
source venv/bin/activate

# Ejecutar aplicación
python app.py
```

La aplicación estará disponible en: **http://127.0.0.1:5000**

**Documentación:** Ver `INSTRUCCIONES.md` para más detalles.

---

### 2. 📊 Análisis de Ventas (Data Science)
**Archivos principales:** `main.py`, `generar_datos_ventas.py`

Proyecto de análisis de datos que procesa ventas de una tienda y genera visualizaciones.

**Características:**
- 📈 Análisis de ventas por mes
- 🏆 Identificación de productos más vendidos
- 💰 Cálculo de ingresos por producto
- 📉 Gráficos de barras (ventas mensuales y top 5 productos)
- 📊 Estadísticas detalladas

**Ejecución:**
```bash
# 1. Generar datos sintéticos (si no existen)
python generar_datos_ventas.py

# 2. Ejecutar análisis
python main.py
```

**Salidas generadas:**
- `ventas_por_mes.png` - Gráfico de ventas mensuales
- `top5_productos.png` - Top 5 productos por ingresos
- Estadísticas en consola

**Tecnologías:** pandas, matplotlib

---

### 3. 📁 Organizador de Archivos
**Archivos principales:** `organizar.py`, `crear_archivos_prueba.py`

Script para organizar automáticamente archivos en carpetas según su extensión.

**Características:**
- 🗂️ Organización automática por categorías (9 predefinidas)
- 🔄 Manejo inteligente de duplicados
- 📊 Estadísticas de organización
- 🛡️ Seguro: no sobreescribe archivos
- 💻 Interfaz de línea de comandos

**Categorías:**
- Imagenes, Documentos, Videos, Musica
- Archivos_Comprimidos, Codigo, Ejecutables, Datos
- Otros (archivos sin categoría)

**Ejecución:**
```bash
# Organizar Descargas (por defecto)
python organizar.py

# Organizar carpeta específica
python organizar.py -c /ruta/carpeta

# Con manejo de duplicados
python organizar.py --duplicados
```

**Documentación:** Ver `README_ORGANIZAR.md` para uso completo.

---

### 4. 📝 Editor de Notas (Aplicación de Escritorio)
**Archivos principales:** `notas.py`

Aplicación de escritorio con interfaz gráfica (GUI) desarrollada con Tkinter.

**Características:**
- ✏️ Editor de texto multilínea
- 💾 Abrir y guardar archivos
- 📋 Menú Editar (cortar, copiar, pegar, deshacer/rehacer)
- ⚠️ Detección de cambios sin guardar
- ⌨️ Atajos de teclado (Ctrl+S, Ctrl+O, etc.)
- 📊 Barra de estado
- 🎨 Interfaz moderna y funcional

**Ejecución:**
```bash
python notas.py
```

**Requisitos especiales:**
- En Linux, instalar tkinter: `sudo apt-get install python3-tk` (Debian/Ubuntu)
- En Windows y Mac, tkinter viene incluido con Python

**Tecnologías:** Tkinter (biblioteca estándar de Python)

---

## 🛠️ Instalación y Configuración

### Requisitos
- Python 3.6+
- pip

### Instalación de dependencias del sistema

**Linux (Debian/Ubuntu):**
```bash
# Instalar tkinter (requerido para el editor de notas)
sudo apt-get update
sudo apt-get install python3-tk
```

**Linux (Fedora/RHEL):**
```bash
sudo dnf install python3-tkinter
```

**Mac:**
- Tkinter viene incluido con Python instalado desde python.org

**Windows:**
- Tkinter viene incluido con Python

### Instalación de dependencias de Python

```bash
# Crear entorno virtual (si no existe)
python3 -m venv venv

# Activar entorno virtual
source venv/bin/activate  # Linux/Mac
# o
venv\Scripts\activate  # Windows

# Instalar dependencias
pip install -r requirements.txt
```

### Dependencias principales
- Flask >= 3.0.0 (para el gestor de tareas)
- pandas >= 2.0.0 (para análisis de datos)
- matplotlib >= 3.7.0 (para visualizaciones)
- Tkinter (biblioteca estándar, requiere instalación en Linux)

---

## 📁 Estructura del Proyecto

```
Cursor-curso/
├── app.py                      # Aplicación Flask (Gestor de Tareas)
├── main.py                     # Script de análisis de ventas
├── notas.py                    # Editor de Notas (GUI con Tkinter)
├── organizar.py                # Organizador de archivos
├── generar_datos_ventas.py    # Generador de datos sintéticos
├── crear_archivos_prueba.py   # Generador de archivos de prueba
├── templates/                  # Plantillas HTML (Flask)
│   └── index.html
├── requirements.txt            # Dependencias del proyecto
├── README.md                   # Este archivo
├── README_ORGANIZAR.md         # Documentación del organizador
├── INSTRUCCIONES.md            # Instrucciones del gestor de tareas
└── venv/                       # Entorno virtual (no incluido en git)
```

---

## 🎯 Ejercicios Adicionales

El repositorio también incluye varios ejercicios de práctica:

- `main2.py`, `main3.py`, `main4.py`, `main5.py`, `main6.py` - Ejercicios variados
- `analisis.py` - Análisis de texto (conteo de palabras)
- `main_.py` - Ejercicios adicionales

---

## 📝 Notas

- **Archivos generados:** Los archivos `.png`, `.csv`, `.json` generados por los scripts están excluidos del repositorio (ver `.gitignore`)
- **Entorno virtual:** El directorio `venv/` no debe subirse al repositorio
- **Datos de prueba:** La carpeta `carpeta_prueba/` es para pruebas del organizador y está excluida

---

## 🚀 Uso Rápido

### Gestor de Tareas
```bash
python app.py
# Abrir http://127.0.0.1:5000
```

### Análisis de Ventas
```bash
python generar_datos_ventas.py  # Generar datos
python main.py                   # Ejecutar análisis
```

### Organizador de Archivos
```bash
python organizar.py -c ~/Downloads
```

### Editor de Notas
```bash
# Asegúrate de tener tkinter instalado (ver sección de instalación)
python notas.py
```

---

## 📚 Recursos de Aprendizaje

Estos proyectos fueron desarrollados como parte de un curso práctico de Python, cubriendo:
- Desarrollo web con Flask
- Análisis de datos con pandas
- Visualización de datos con matplotlib
- Desarrollo de aplicaciones de escritorio con Tkinter
- Manipulación de archivos y sistema de archivos
- Programación orientada a objetos y funciones
- Programación dirigida por eventos (GUI)
- Buenas prácticas de Python

---

## 📄 Licencia

Este es un proyecto educativo. Siéntete libre de usar y modificar el código para tus propios proyectos de aprendizaje.

---

## 👤 Autor

Desarrollado como parte del curso de Python con Cursor.

---

**¡Happy Coding! 🎉**
