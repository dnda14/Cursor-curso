# Gestor de Tareas - Aplicación Flask

## Estructura del Proyecto

```
Cursor-curso/
├── app.py                 # Aplicación Flask principal
├── templates/
│   └── index.html        # Plantilla HTML
├── tareas.json           # Archivo de persistencia (se crea automáticamente)
└── requirements.txt      # Dependencias
```

## Instalación

1. Asegúrate de tener el entorno virtual activado:
```bash
source venv/bin/activate
```

2. Instala las dependencias (si no están instaladas):
```bash
pip install -r requirements.txt
```

## Ejecución

Ejecuta la aplicación:
```bash
python app.py
```

O con Flask directamente:
```bash
flask run
```

La aplicación estará disponible en: **http://127.0.0.1:5000**

## Funcionalidades

- ✅ Agregar nuevas tareas
- ✅ Marcar tareas como completadas
- ✅ Persistencia en archivo JSON (las tareas se guardan automáticamente)
- ✅ Interfaz moderna y responsive

## Rutas

- `/` - Página principal (lista de tareas y formulario)
- `/agregar` - POST: Agregar nueva tarea
- `/completar/<id>` - GET: Marcar tarea como completada

## Notas

- Las tareas se guardan automáticamente en `tareas.json`
- Al reiniciar la aplicación, las tareas se cargan desde el archivo JSON
- Las tareas incompletas aparecen primero, luego las completadas
