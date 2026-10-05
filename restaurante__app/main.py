import tkinter as tk
import os

from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView


# ==========================================================
# RUTAS
# ==========================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

RUTA_USUARIOS = os.path.join(
    BASE_DIR,
    "datos",
    "usuarios.json"
)

RUTA_PRODUCTOS = os.path.join(
    BASE_DIR,
    "datos",
    "productos.json"
)

RUTA_VENTAS = os.path.join(
    BASE_DIR,
    "datos",
    "ventas.json"
)


# ==========================================================
# CARGAR DATOS
# ==========================================================

archivo = ArchivoServicio()


try:
    usuarios = archivo.leer_json(RUTA_USUARIOS)
except Exception as e:
    print("Error al cargar usuarios:", e)
    usuarios = []


try:
    productos = archivo.leer_json(RUTA_PRODUCTOS)
except Exception as e:
    print("Error al cargar productos:", e)
    productos = []


try:
    ventas = archivo.leer_json(RUTA_VENTAS)
except Exception:
    ventas = []


# ==========================================================
# SERVICIO
# ==========================================================

servicio = RestauranteServicio(
    usuarios,
    productos,
    archivo,
    RUTA_PRODUCTOS,
    RUTA_USUARIOS,
    ventas,
    RUTA_VENTAS
)


# ==========================================================
# VENTANA PRINCIPAL
# ==========================================================

root = tk.Tk()

root.title("Restaurante App")
root.geometry("1000x700")
root.resizable(True, True)


# ==========================================================
# MOSTRAR PANEL PRINCIPAL
# ==========================================================

def mostrar_principal(usuario=None):

    for widget in root.winfo_children():
        widget.destroy()

    MainView(
        root,
        servicio,
        mostrar_login,
        usuario
    )


# ==========================================================
# MOSTRAR LOGIN
# ==========================================================

def mostrar_login():

    for widget in root.winfo_children():
        widget.destroy()

    LoginView(
        root,
        servicio,
        mostrar_principal
    )


# ==========================================================
# INICIAR
# ==========================================================

mostrar_login()

root.mainloop()