# 📦 Instalación de Tkinter en Linux

Tkinter no viene instalado por defecto en muchas distribuciones de Linux. Aquí están las instrucciones para instalarlo según tu distribución.

## 🐧 Debian/Ubuntu

```bash
sudo apt-get update
sudo apt-get install python3-tk
```

## 🔴 Fedora/RHEL/CentOS

```bash
sudo dnf install python3-tkinter
```

O si usas `yum`:
```bash
sudo yum install python3-tkinter
```

## 🟢 Arch Linux

```bash
sudo pacman -S tk
```

## 🟡 openSUSE

```bash
sudo zypper install python3-tk
```

## ✅ Verificar instalación

Después de instalar, verifica que tkinter funciona:

```bash
python3 -c "import tkinter; print('Tkinter instalado correctamente')"
```

Si no hay errores, tkinter está listo para usar.

## 🚀 Ejecutar el Editor de Notas

Una vez instalado tkinter, puedes ejecutar el editor:

```bash
python3 notas.py
```

## ⚠️ Nota

- En **Windows** y **Mac**, tkinter viene incluido con Python, no necesitas instalarlo.
- Si tienes problemas, asegúrate de que Python y tkinter sean de la misma versión.
