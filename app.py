import json
from flask import Flask, request, redirect, render_template

app = Flask(__name__)

# Estructura de datos en memoria
tareas = []
siguiente_id = 1
ARCHIVO_DATOS = 'tareas.json'

# Funciones para manejar tareas
def agregar_tarea(texto):
    global siguiente_id
    tareas.append({'id': siguiente_id, 'texto': texto, 'hecho': False})
    siguiente_id += 1
    guardar_datos()

def completar_tarea(id):
    for tarea in tareas:
        if tarea['id'] == id:
            tarea['hecho'] = True
            guardar_datos()
            break

# Persistencia con JSON
def guardar_datos():
    with open(ARCHIVO_DATOS, 'w', encoding='utf-8') as f:
        json.dump({'siguiente_id': siguiente_id, 'tareas': tareas}, f, ensure_ascii=False, indent=2)

def cargar_datos():
    global siguiente_id, tareas
    try:
        with open(ARCHIVO_DATOS, 'r', encoding='utf-8') as f:
            data = json.load(f)
            tareas = data['tareas']
            siguiente_id = data['siguiente_id']
    except FileNotFoundError:
        pass

# Cargar datos al iniciar
cargar_datos()

# Rutas
@app.route('/')
def index():
    # Ordenar tareas: incompletas primero, luego completadas
    tareas_ordenadas = sorted(tareas, key=lambda t: t['hecho'])
    return render_template('index.html', tareas=tareas_ordenadas)

@app.route('/agregar', methods=['POST'])
def agregar():
    texto_tarea = request.form.get('texto_tarea', '').strip()
    if texto_tarea:
        agregar_tarea(texto_tarea)
    return redirect('/')

@app.route('/completar/<int:id>')
def completar(id):
    completar_tarea(id)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
