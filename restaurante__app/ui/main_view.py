import tkinter as tk
from tkinter import ttk, messagebox
import os


class MainView:

    def __init__(self, root, servicio, cerrar_sesion):
        self.root = root
        self.servicio = servicio
        self.cerrar_sesion = cerrar_sesion

        # ======================================================
        # RUTA DE LOS ICONOS
        # ======================================================
        carpeta_assets = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            "assets"
        )

        # ======================================================
        # CARGAR IMÁGENES
        # ======================================================
        self.logo_img = self.cargar_imagen(
            os.path.join(carpeta_assets, "logo.png")
        )

        self.usuarios_img = self.cargar_imagen(
            os.path.join(carpeta_assets, "usuarios.png")
        )

        self.productos_img = self.cargar_imagen(
            os.path.join(carpeta_assets, "productos.png")
        )

        self.ventas_img = self.cargar_imagen(
            os.path.join(carpeta_assets, "ventas.png")
        )

        self.salir_img = self.cargar_imagen(
            os.path.join(carpeta_assets, "salir.png")
        )

        # ======================================================
        # FRAME PRINCIPAL
        # ======================================================
        self.frame = tk.Frame(
            self.root,
            bg="white"
        )

        self.frame.pack(
            expand=True,
            fill="both"
        )

        # ======================================================
        # LOGO
        # ======================================================
        if self.logo_img:
            logo_label = tk.Label(
                self.frame,
                image=self.logo_img,
                bg="white"
            )
            logo_label.pack(pady=(10, 0))

        # ======================================================
        # TÍTULO
        # ======================================================
        titulo = tk.Label(
            self.frame,
            text="Panel Principal - Restaurante",
            font=("Arial", 20, "bold"),
            bg="white",
            fg="#8B3A62"
        )

        titulo.pack(pady=10)

        # ======================================================
        # MENÚ
        # ======================================================
        menu = tk.Frame(
            self.frame,
            bg="white"
        )

        menu.pack(pady=5)

        # ======================================================
        # BOTÓN PRODUCTOS
        # ======================================================
        boton_productos = ttk.Button(
            menu,
            text="Ver Productos",
            image=self.productos_img,
            compound="top",
            command=self.mostrar_productos
        )

        boton_productos.grid(
            row=0,
            column=0,
            padx=10
        )

        # ======================================================
        # BOTÓN USUARIOS
        # ======================================================
        boton_usuarios = ttk.Button(
            menu,
            text="Ver Usuarios",
            image=self.usuarios_img,
            compound="top",
            command=self.mostrar_usuarios
        )

        boton_usuarios.grid(
            row=0,
            column=1,
            padx=10
        )

        # ======================================================
        # SEMANA 15
        # BOTÓN VENTAS
        # ======================================================
        boton_ventas = ttk.Button(
            menu,
            text="Ventas",
            image=self.ventas_img,
            compound="top",
            command=self.mostrar_ventas
        )

        boton_ventas.grid(
            row=0,
            column=2,
            padx=10
        )

        # ======================================================
        # BOTÓN CERRAR SESIÓN
        # ======================================================
        boton_salir = ttk.Button(
            menu,
            text="Cerrar sesión",
            image=self.salir_img,
            compound="top",
            command=self.cerrar
        )

        boton_salir.grid(
            row=0,
            column=3,
            padx=10
        )

        # ======================================================
        # CONTENIDO
        # ======================================================
        self.contenido = tk.Frame(
            self.frame,
            bg="white"
        )

        self.contenido.pack(
            expand=True,
            fill="both",
            padx=15,
            pady=10
        )

    # ==========================================================
    # CARGAR IMAGEN
    # ==========================================================

    def cargar_imagen(self, ruta):
        try:
            if os.path.exists(ruta):
                return tk.PhotoImage(file=ruta)
            else:
                print(f"No se encontró la imagen: {ruta}")
                return None

        except Exception as error:
            print(f"No se pudo cargar la imagen {ruta}: {error}")
            return None

    # ==========================================================
    # LIMPIAR CONTENIDO
    # ==========================================================

    def limpiar_contenido(self):
        for widget in self.contenido.winfo_children():
            widget.destroy()

    # ==========================================================
    # PRODUCTOS
    # ==========================================================

    def mostrar_productos(self):

        self.limpiar_contenido()

        formulario = tk.LabelFrame(
            self.contenido,
            text="Gestión de productos",
            padx=10,
            pady=10
        )

        formulario.pack(
            fill="x",
            pady=5
        )

        tk.Label(
            formulario,
            text="ID:"
        ).grid(
            row=0,
            column=0,
            padx=5,
            pady=5
        )

        self.id_entry = tk.Entry(formulario)

        self.id_entry.grid(
            row=0,
            column=1,
            padx=5,
            pady=5
        )

        tk.Label(
            formulario,
            text="Nombre:"
        ).grid(
            row=1,
            column=0,
            padx=5,
            pady=5
        )

        self.nombre_entry = tk.Entry(formulario)

        self.nombre_entry.grid(
            row=1,
            column=1,
            padx=5,
            pady=5
        )

        tk.Label(
            formulario,
            text="Precio:"
        ).grid(
            row=0,
            column=2,
            padx=5,
            pady=5
        )

        self.precio_entry = tk.Entry(formulario)

        self.precio_entry.grid(
            row=0,
            column=3,
            padx=5,
            pady=5
        )

        tk.Label(
            formulario,
            text="Cantidad:"
        ).grid(
            row=1,
            column=2,
            padx=5,
            pady=5
        )

        self.cantidad_entry = tk.Entry(formulario)

        self.cantidad_entry.grid(
            row=1,
            column=3,
            padx=5,
            pady=5
        )

        botones = tk.Frame(formulario)

        botones.grid(
            row=2,
            column=0,
            columnspan=4,
            pady=10
        )

        ttk.Button(
            botones,
            text="Registrar",
            command=self.registrar_producto
        ).grid(
            row=0,
            column=0,
            padx=5
        )

        ttk.Button(
            botones,
            text="Cargar por ID",
            command=self.cargar_producto
        ).grid(
            row=0,
            column=1,
            padx=5
        )

        ttk.Button(
            botones,
            text="Actualizar",
            command=self.actualizar_producto
        ).grid(
            row=0,
            column=2,
            padx=5
        )

        ttk.Button(
            botones,
            text="Eliminar",
            command=self.eliminar_producto
        ).grid(
            row=0,
            column=3,
            padx=5
        )

        ttk.Button(
            botones,
            text="Limpiar",
            command=self.limpiar_formulario
        ).grid(
            row=0,
            column=4,
            padx=5
        )

        tabla_frame = tk.LabelFrame(
            self.contenido,
            text="Productos registrados"
        )

        tabla_frame.pack(
            expand=True,
            fill="both",
            pady=5
        )

        columnas = (
            "id",
            "nombre",
            "precio",
            "cantidad"
        )

        self.tabla_productos = ttk.Treeview(
            tabla_frame,
            columns=columnas,
            show="headings"
        )

        self.tabla_productos.heading(
            "id",
            text="ID"
        )

        self.tabla_productos.heading(
            "nombre",
            text="Nombre"
        )

        self.tabla_productos.heading(
            "precio",
            text="Precio"
        )

        self.tabla_productos.heading(
            "cantidad",
            text="Cantidad"
        )

        self.tabla_productos.column(
            "id",
            width=60
        )

        self.tabla_productos.column(
            "nombre",
            width=180
        )

        self.tabla_productos.column(
            "precio",
            width=100
        )

        self.tabla_productos.column(
            "cantidad",
            width=100
        )

        scrollbar = ttk.Scrollbar(
            tabla_frame,
            orient="vertical",
            command=self.tabla_productos.yview
        )

        self.tabla_productos.configure(
            yscrollcommand=scrollbar.set
        )

        self.tabla_productos.pack(
            side="left",
            expand=True,
            fill="both"
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        self.cargar_tabla_productos()

    # ==========================================================
    # CARGAR TABLA PRODUCTOS
    # ==========================================================

    def cargar_tabla_productos(self):

        for item in self.tabla_productos.get_children():
            self.tabla_productos.delete(item)

        productos = self.servicio.listar_productos()

        for producto in productos:

            self.tabla_productos.insert(
                "",
                "end",
                values=(
                    producto.id,
                    producto.nombre,
                    f"${producto.precio:.2f}",
                    producto.cantidad
                )
            )

    # ==========================================================
    # REGISTRAR PRODUCTO
    # ==========================================================

    def registrar_producto(self):

        id = self.id_entry.get()
        nombre = self.nombre_entry.get()
        precio = self.precio_entry.get()
        cantidad = self.cantidad_entry.get()

        if not id or not nombre or not precio or not cantidad:

            messagebox.showwarning(
                "Campos vacíos",
                "Complete todos los campos."
            )

            return

        correcto, mensaje = self.servicio.registrar_producto(
            id,
            nombre,
            precio,
            cantidad
        )

        if correcto:

            messagebox.showinfo(
                "Registro",
                mensaje
            )

            self.limpiar_formulario()
            self.cargar_tabla_productos()

        else:

            messagebox.showerror(
                "Error",
                mensaje
            )

    # ==========================================================
    # CARGAR PRODUCTO
    # ==========================================================

    def cargar_producto(self):

        id = self.id_entry.get()

        if not id:

            messagebox.showwarning(
                "Campo vacío",
                "Ingrese el ID del producto."
            )

            return

        producto = self.servicio.buscar_producto(id)

        if producto is None:

            messagebox.showerror(
                "Error",
                "Producto no encontrado."
            )

            return

        self.nombre_entry.delete(
            0,
            tk.END
        )

        self.nombre_entry.insert(
            0,
            producto.nombre
        )

        self.precio_entry.delete(
            0,
            tk.END
        )

        self.precio_entry.insert(
            0,
            producto.precio
        )

        self.cantidad_entry.delete(
            0,
            tk.END
        )

        self.cantidad_entry.insert(
            0,
            producto.cantidad
        )

    # ==========================================================
    # ACTUALIZAR PRODUCTO
    # ==========================================================

    def actualizar_producto(self):

        id = self.id_entry.get()
        nombre = self.nombre_entry.get()
        precio = self.precio_entry.get()
        cantidad = self.cantidad_entry.get()

        if not id or not nombre or not precio or not cantidad:

            messagebox.showwarning(
                "Campos vacíos",
                "Complete todos los campos."
            )

            return

        correcto, mensaje = self.servicio.actualizar_producto(
            id,
            nombre,
            precio,
            cantidad
        )

        if correcto:

            messagebox.showinfo(
                "Actualización",
                mensaje
            )

            self.limpiar_formulario()
            self.cargar_tabla_productos()

        else:

            messagebox.showerror(
                "Error",
                mensaje
            )

    # ==========================================================
    # ELIMINAR PRODUCTO
    # ==========================================================

    def eliminar_producto(self):

        id = self.id_entry.get()

        if not id:

            messagebox.showwarning(
                "Campo vacío",
                "Ingrese el ID del producto."
            )

            return

        confirmar = messagebox.askyesno(
            "Eliminar producto",
            "¿Está seguro de eliminar este producto?"
        )

        if not confirmar:
            return

        correcto, mensaje = self.servicio.eliminar_producto(id)

        if correcto:

            messagebox.showinfo(
                "Eliminación",
                mensaje
            )

            self.limpiar_formulario()
            self.cargar_tabla_productos()

        else:

            messagebox.showerror(
                "Error",
                mensaje
            )

    # ==========================================================
    # LIMPIAR FORMULARIO
    # ==========================================================

    def limpiar_formulario(self):

        self.id_entry.delete(
            0,
            tk.END
        )

        self.nombre_entry.delete(
            0,
            tk.END
        )

        self.precio_entry.delete(
            0,
            tk.END
        )

        self.cantidad_entry.delete(
            0,
            tk.END
        )

    # ==========================================================
    # USUARIOS
    # ==========================================================

    def mostrar_usuarios(self):

        self.limpiar_contenido()

        grupo = tk.LabelFrame(
            self.contenido,
            text="Usuarios registrados",
            padx=10,
            pady=10
        )

        grupo.pack(
            expand=True,
            fill="both"
        )

        columnas = (
            "id",
            "nombre",
            "usuario"
        )

        tabla = ttk.Treeview(
            grupo,
            columns=columnas,
            show="headings"
        )

        tabla.heading(
            "id",
            text="ID"
        )

        tabla.heading(
            "nombre",
            text="Nombre"
        )

        tabla.heading(
            "usuario",
            text="Usuario"
        )

        tabla.column(
            "id",
            width=60
        )

        tabla.column(
            "nombre",
            width=200
        )

        tabla.column(
            "usuario",
            width=150
        )

        scrollbar = ttk.Scrollbar(
            grupo,
            orient="vertical",
            command=tabla.yview
        )

        tabla.configure(
            yscrollcommand=scrollbar.set
        )

        tabla.pack(
            side="left",
            expand=True,
            fill="both"
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        usuarios = self.servicio.listar_usuarios()

        for usuario in usuarios:

            tabla.insert(
                "",
                "end",
                values=(
                    usuario.id,
                    usuario.nombre,
                    usuario.usuario
                )
            )

    # ==========================================================
    # VENTAS - SEMANA 15
    # ==========================================================

    def mostrar_ventas(self):

        self.limpiar_contenido()

        formulario = tk.LabelFrame(
            self.contenido,
            text="Registrar venta",
            padx=15,
            pady=15
        )

        formulario.pack(
            fill="x",
            pady=5
        )

        # ------------------------------------------------------
        # USUARIO
        # ------------------------------------------------------

        tk.Label(
            formulario,
            text="Usuario:"
        ).grid(
            row=0,
            column=0,
            padx=5,
            pady=8
        )

        self.usuario_combo = ttk.Combobox(
            formulario,
            state="readonly",
            width=30
        )

        self.usuario_combo.grid(
            row=0,
            column=1,
            padx=5,
            pady=8
        )

        usuarios = self.servicio.listar_usuarios()

        self.usuarios_ventas = usuarios

        self.usuario_combo["values"] = [
            f"{usuario.id} - {usuario.nombre}"
            for usuario in usuarios
        ]

        # ------------------------------------------------------
        # PRODUCTO
        # ------------------------------------------------------

        tk.Label(
            formulario,
            text="Producto:"
        ).grid(
            row=1,
            column=0,
            padx=5,
            pady=8
        )

        self.producto_combo = ttk.Combobox(
            formulario,
            state="readonly",
            width=30
        )

        self.producto_combo.grid(
            row=1,
            column=1,
            padx=5,
            pady=8
        )

        productos = self.servicio.listar_productos()

        self.productos_ventas = productos

        self.producto_combo["values"] = [
            f"{producto.id} - {producto.nombre}"
            for producto in productos
        ]

        # ------------------------------------------------------
        # BOTÓN
        # ------------------------------------------------------

        ttk.Button(
            formulario,
            text="Registrar venta",
            command=self.registrar_venta
        ).grid(
            row=0,
            column=2,
            rowspan=2,
            padx=20,
            pady=8
        )

        # ------------------------------------------------------
        # TABLA
        # ------------------------------------------------------

        tabla_frame = tk.LabelFrame(
            self.contenido,
            text="Ventas registradas"
        )

        tabla_frame.pack(
            expand=True,
            fill="both",
            pady=10
        )

        columnas = (
            "usuario",
            "producto",
            "fecha"
        )

        self.tabla_ventas = ttk.Treeview(
            tabla_frame,
            columns=columnas,
            show="headings"
        )

        self.tabla_ventas.heading(
            "usuario",
            text="Usuario"
        )

        self.tabla_ventas.heading(
            "producto",
            text="Producto"
        )

        self.tabla_ventas.heading(
            "fecha",
            text="Fecha"
        )

        self.tabla_ventas.column(
            "usuario",
            width=200
        )

        self.tabla_ventas.column(
            "producto",
            width=200
        )

        self.tabla_ventas.column(
            "fecha",
            width=180
        )

        scrollbar = ttk.Scrollbar(
            tabla_frame,
            orient="vertical",
            command=self.tabla_ventas.yview
        )

        self.tabla_ventas.configure(
            yscrollcommand=scrollbar.set
        )

        self.tabla_ventas.pack(
            side="left",
            expand=True,
            fill="both"
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        self.cargar_tabla_ventas()

    # ==========================================================
    # CALLBACK DE VENTA
    # ==========================================================

    def registrar_venta(self):

        usuario_seleccionado = self.usuario_combo.get()
        producto_seleccionado = self.producto_combo.get()

        if not usuario_seleccionado:

            messagebox.showwarning(
                "Usuario",
                "Seleccione un usuario."
            )

            return

        if not producto_seleccionado:

            messagebox.showwarning(
                "Producto",
                "Seleccione un producto."
            )

            return

        # Obtener los ID seleccionados

        usuario_id = usuario_seleccionado.split(" - ")[0]
        producto_id = producto_seleccionado.split(" - ")[0]

        # Delegar la operación al servicio

        correcto, mensaje = self.servicio.registrar_venta(
            usuario_id,
            producto_id
        )

        if correcto:

            messagebox.showinfo(
                "Venta",
                mensaje
            )

            # Limpiar las selecciones

            self.usuario_combo.set("")
            self.producto_combo.set("")

            # Actualizar la tabla

            self.cargar_tabla_ventas()

        else:

            messagebox.showerror(
                "Error",
                mensaje
            )

    # ==========================================================
    # CARGAR VENTAS
    # ==========================================================

    def cargar_tabla_ventas(self):

        for item in self.tabla_ventas.get_children():
            self.tabla_ventas.delete(item)

        ventas = self.servicio.listar_ventas()

        for venta in ventas:

            self.tabla_ventas.insert(
                "",
                "end",
                values=(
                    venta.get("usuario", ""),
                    venta.get("producto", ""),
                    venta.get("fecha", "")
                )
            )

    # ==========================================================
    # CERRAR SESIÓN
    # ==========================================================

    def cerrar(self):

        self.frame.destroy()
        self.cerrar_sesion()