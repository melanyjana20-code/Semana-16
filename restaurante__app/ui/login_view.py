import tkinter as tk
from tkinter import messagebox


class LoginView:

    def __init__(self, root, servicio, mostrar_principal):

        self.root = root
        self.servicio = servicio
        self.mostrar_principal = mostrar_principal

        # ==========================================================
        # FRAME PRINCIPAL
        # ==========================================================

        self.frame = tk.Frame(
            self.root,
            bg="white"
        )

        self.frame.pack(
            expand=True,
            fill="both"
        )

        # ==========================================================
        # TÍTULO
        # ==========================================================

        titulo = tk.Label(
            self.frame,
            text="RESTAURANTE APP",
            font=("Arial", 24, "bold"),
            bg="white",
            fg="#8B3A62"
        )

        titulo.pack(
            pady=(60, 30)
        )

        subtitulo = tk.Label(
            self.frame,
            text="Inicio de sesión",
            font=("Arial", 14),
            bg="white"
        )

        subtitulo.pack(
            pady=5
        )

        # ==========================================================
        # USUARIO
        # ==========================================================

        tk.Label(
            self.frame,
            text="Usuario:",
            font=("Arial", 11),
            bg="white"
        ).pack(
            pady=(20, 5)
        )

        self.usuario_entry = tk.Entry(
            self.frame,
            font=("Arial", 11),
            width=30
        )

        self.usuario_entry.pack(
            pady=5
        )

        # ==========================================================
        # CONTRASEÑA
        # ==========================================================

        tk.Label(
            self.frame,
            text="Contraseña:",
            font=("Arial", 11),
            bg="white"
        ).pack(
            pady=(10, 5)
        )

        self.contraseña_entry = tk.Entry(
            self.frame,
            show="*",
            font=("Arial", 11),
            width=30
        )

        self.contraseña_entry.pack(
            pady=5
        )

        # ==========================================================
        # BOTÓN INGRESAR
        # ==========================================================

        tk.Button(
            self.frame,
            text="Ingresar",
            font=("Arial", 11, "bold"),
            width=20,
            bg="#8B3A62",
            fg="white",
            command=self.ingresar
        ).pack(
            pady=25
        )

        # ==========================================================
        # EVENTOS
        # ==========================================================

        self.usuario_entry.bind(
            "<Return>",
            self.ingresar
        )

        self.contraseña_entry.bind(
            "<Return>",
            self.ingresar
        )

        # ==========================================================
        # ENFOQUE INICIAL
        # ==========================================================

        self.usuario_entry.focus()


    # ==========================================================
    # INGRESAR
    # ==========================================================

    def ingresar(self, event=None):

        usuario = self.usuario_entry.get().strip()

        contraseña = self.contraseña_entry.get().strip()

        # ----------------------------------------------------------
        # CAMPOS VACÍOS
        # ----------------------------------------------------------

        if not usuario or not contraseña:

            messagebox.showwarning(
                "Campos vacíos",
                "Ingrese usuario y contraseña."
            )

            return "break"

        # ----------------------------------------------------------
        # VALIDAR USUARIO
        # ----------------------------------------------------------

        if self.servicio.validar_usuario(
            usuario,
            contraseña
        ):

            # Obtener el usuario completo
            usuario_actual = self.servicio.obtener_usuario(
                usuario,
                contraseña
            )

            # Quitar eventos del Login
            self.usuario_entry.unbind("<Return>")
            self.contraseña_entry.unbind("<Return>")

            # Eliminar Login
            self.frame.destroy()

            # Enviar usuario autenticado al MainView
            self.mostrar_principal(
                usuario_actual
            )

        else:

            messagebox.showerror(
                "Acceso denegado",
                "Usuario o contraseña incorrectos."
            )

            self.contraseña_entry.delete(
                0,
                tk.END
            )

            self.contraseña_entry.focus()

        return "break"