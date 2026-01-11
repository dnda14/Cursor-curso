#!/usr/bin/env python3
"""
Editor de Notas - Aplicación de escritorio con Tkinter
Un bloc de notas simplificado con funcionalidad de abrir y guardar archivos.
"""

import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import os


class EditorNotas(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # Configuración de la ventana
        self.title("Editor de Notas")
        self.geometry("800x600")
        self.minsize(400, 300)
        
        # Variables de estado
        self.archivo_actual = None
        self.cambios_sin_guardar = False
        
        # Crear interfaz
        self.crear_widgets()
        self.crear_menu()
        
        # Configurar protocolo de cierre de ventana
        self.protocol("WM_DELETE_WINDOW", self.salir)
        
        # Atajos de teclado
        self.bind('<Control-s>', lambda e: self.guardar_archivo())
        self.bind('<Control-o>', lambda e: self.abrir_archivo())
        self.bind('<Control-n>', lambda e: self.nuevo_archivo())
        self.bind('<Control-q>', lambda e: self.salir())
        
        # Detectar cambios en el texto
        self.text_area.bind('<KeyPress>', self.marcar_cambios)
        self.text_area.bind('<Button-1>', self.marcar_cambios)
    
    def crear_widgets(self):
        """Crea los widgets de la interfaz."""
        # Área de texto con scrollbar
        self.text_area = scrolledtext.ScrolledText(
            self,
            wrap=tk.WORD,
            font=('Arial', 11),
            undo=True  # Habilitar deshacer/rehacer
        )
        self.text_area.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)
        
        # Barra de estado (opcional)
        self.status_bar = tk.Label(
            self,
            text="Listo",
            bd=1,
            relief=tk.SUNKEN,
            anchor=tk.W
        )
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
    
    def crear_menu(self):
        """Crea el menú de la aplicación."""
        menubar = tk.Menu(self)
        
        # Menú Archivo
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(
            label="Nuevo",
            command=self.nuevo_archivo,
            accelerator="Ctrl+N"
        )
        filemenu.add_command(
            label="Abrir...",
            command=self.abrir_archivo,
            accelerator="Ctrl+O"
        )
        filemenu.add_command(
            label="Guardar",
            command=self.guardar_archivo,
            accelerator="Ctrl+S"
        )
        filemenu.add_command(
            label="Guardar como...",
            command=self.guardar_como
        )
        filemenu.add_separator()
        filemenu.add_command(
            label="Salir",
            command=self.salir,
            accelerator="Ctrl+Q"
        )
        menubar.add_cascade(label="Archivo", menu=filemenu)
        
        # Menú Editar
        editmenu = tk.Menu(menubar, tearoff=0)
        editmenu.add_command(
            label="Deshacer",
            command=lambda: self.text_area.event_generate("<<Undo>>"),
            accelerator="Ctrl+Z"
        )
        editmenu.add_command(
            label="Rehacer",
            command=lambda: self.text_area.event_generate("<<Redo>>"),
            accelerator="Ctrl+Y"
        )
        editmenu.add_separator()
        editmenu.add_command(
            label="Cortar",
            command=lambda: self.text_area.event_generate("<<Cut>>"),
            accelerator="Ctrl+X"
        )
        editmenu.add_command(
            label="Copiar",
            command=lambda: self.text_area.event_generate("<<Copy>>"),
            accelerator="Ctrl+C"
        )
        editmenu.add_command(
            label="Pegar",
            command=lambda: self.text_area.event_generate("<<Paste>>"),
            accelerator="Ctrl+V"
        )
        editmenu.add_separator()
        editmenu.add_command(
            label="Seleccionar todo",
            command=lambda: self.text_area.event_generate("<<SelectAll>>"),
            accelerator="Ctrl+A"
        )
        menubar.add_cascade(label="Editar", menu=editmenu)
        
        # Menú Ayuda
        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Acerca de...", command=self.mostrar_acerca_de)
        menubar.add_cascade(label="Ayuda", menu=helpmenu)
        
        self.config(menu=menubar)
    
    def marcar_cambios(self, event=None):
        """Marca que hay cambios sin guardar."""
        if not self.cambios_sin_guardar:
            self.cambios_sin_guardar = True
            self.actualizar_titulo()
    
    def actualizar_titulo(self):
        """Actualiza el título de la ventana según el estado."""
        titulo = "Editor de Notas"
        if self.archivo_actual:
            titulo += f" - {os.path.basename(self.archivo_actual)}"
        if self.cambios_sin_guardar:
            titulo += " *"
        self.title(titulo)
        self.actualizar_status()
    
    def actualizar_status(self):
        """Actualiza la barra de estado."""
        if self.archivo_actual:
            self.status_bar.config(text=f"Archivo: {self.archivo_actual}")
        else:
            self.status_bar.config(text="Sin archivo abierto")
    
    def nuevo_archivo(self):
        """Crea un nuevo archivo."""
        if self.confirmar_guardar_cambios():
            self.text_area.delete(1.0, tk.END)
            self.archivo_actual = None
            self.cambios_sin_guardar = False
            self.actualizar_titulo()
    
    def abrir_archivo(self):
        """Abre un archivo existente."""
        if self.confirmar_guardar_cambios():
            filepath = filedialog.askopenfilename(
                title="Abrir archivo",
                filetypes=[
                    ("Archivos de texto", "*.txt"),
                    ("Archivos Python", "*.py"),
                    ("Archivos Markdown", "*.md"),
                    ("Todos los archivos", "*.*")
                ]
            )
            
            if not filepath:
                return
            
            try:
                with open(filepath, "r", encoding="utf-8") as file:
                    contenido = file.read()
                
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, contenido)
                self.archivo_actual = filepath
                self.cambios_sin_guardar = False
                self.actualizar_titulo()
                
            except UnicodeDecodeError:
                messagebox.showerror(
                    "Error",
                    "No se pudo abrir el archivo.\n"
                    "El archivo no es de texto o tiene una codificación no soportada."
                )
            except Exception as e:
                messagebox.showerror(
                    "Error",
                    f"No se pudo abrir el archivo:\n{e}"
                )
    
    def guardar_archivo(self):
        """Guarda el archivo actual."""
        if self.archivo_actual:
            try:
                contenido = self.text_area.get(1.0, tk.END)
                with open(self.archivo_actual, "w", encoding="utf-8") as file:
                    file.write(contenido.rstrip() + '\n')
                
                self.cambios_sin_guardar = False
                self.actualizar_titulo()
                messagebox.showinfo("Éxito", "Archivo guardado correctamente.")
                
            except Exception as e:
                messagebox.showerror(
                    "Error",
                    f"No se pudo guardar el archivo:\n{e}"
                )
        else:
            self.guardar_como()
    
    def guardar_como(self):
        """Guarda el archivo con un nuevo nombre."""
        filepath = filedialog.asksaveasfilename(
            title="Guardar como",
            defaultextension=".txt",
            filetypes=[
                ("Archivos de texto", "*.txt"),
                ("Archivos Python", "*.py"),
                ("Archivos Markdown", "*.md"),
                ("Todos los archivos", "*.*")
            ]
        )
        
        if not filepath:
            return
        
        try:
            contenido = self.text_area.get(1.0, tk.END)
            with open(filepath, "w", encoding="utf-8") as file:
                file.write(contenido.rstrip() + '\n')
            
            self.archivo_actual = filepath
            self.cambios_sin_guardar = False
            self.actualizar_titulo()
            messagebox.showinfo("Éxito", "Archivo guardado correctamente.")
            
        except Exception as e:
            messagebox.showerror(
                "Error",
                f"No se pudo guardar el archivo:\n{e}"
            )
    
    def confirmar_guardar_cambios(self):
        """
        Pregunta al usuario si desea guardar cambios antes de continuar.
        Returns: True si puede continuar, False si debe cancelar.
        """
        if self.cambios_sin_guardar:
            respuesta = messagebox.askyesnocancel(
                "Cambios sin guardar",
                "¿Desea guardar los cambios antes de continuar?"
            )
            
            if respuesta is None:  # Cancelar
                return False
            elif respuesta:  # Sí, guardar
                self.guardar_archivo()
                return True
            else:  # No, descartar cambios
                return True
        
        return True
    
    def salir(self):
        """Cierra la aplicación."""
        if self.confirmar_guardar_cambios():
            self.destroy()
    
    def mostrar_acerca_de(self):
        """Muestra información sobre la aplicación."""
        messagebox.showinfo(
            "Acerca de",
            "Editor de Notas\n\n"
            "Un bloc de notas simple desarrollado con Python y Tkinter.\n\n"
            "Versión 1.0\n"
            "Desarrollado como parte del curso de Python con Cursor."
        )


if __name__ == "__main__":
    app = EditorNotas()
    app.mainloop()
