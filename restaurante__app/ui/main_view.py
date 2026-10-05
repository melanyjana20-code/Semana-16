import tkinter as tk
from tkinter import ttk, messagebox
import os

class MainView:


  def __init__(self, root, servicio, cerrar_sesion, usuario_actual=None):

    self.root = root
    self.servicio = servicio
    self.cerrar_sesion = cerrar_sesion
    self.usuario_actual = usuario_actual

    self.frame = tk.Frame(
        self.root,
        bg="white"
    )

    self.frame.pack(
        expand=True,
        fill="both"
    )

    # ======================================================
    # ASSETS
    # ======================================================

    carpeta_assets = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "assets"
    )

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
    # LOGO
    # ======================================================

    if self.logo_img:

        tk.Label(
            self.frame,
            image=self.logo_img,
            bg="white"
        ).pack(
            pady=(10, 0)
        )

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

    ttk.Button(
        menu,
        text="Ver Productos",
        image=self.productos_img,
        compound="top",
        command=self.mostrar_productos
    ).grid(
        row=0,
        column=0,
        padx=10
    )

    # Solo Administrador puede gestionar usuarios

    if self.es_administrador():

        ttk.Button(
            menu,
            text="Ver Usuarios",
            image=self.usuarios_img,
            compound="top",
            command=self.mostrar_usuarios
        ).grid(
            row=0,
            column=1,
            padx=10
        )

    ttk.Button(
        menu,
        text="Ventas",
        image=self.ventas_img,
        compound="top",
        command=self.mostrar_ventas
    ).grid(
        row=0,
        column=2,
        padx=10
    )

    ttk.Button(
        menu,
        text="Cerrar sesión",
        image=self.salir_img,
        compound="top",
        command=self.cerrar
    ).grid(
        row=0,
        column=3,
        padx=10
    )

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
  # IMÁGENES
  # ==========================================================

  def cargar_imagen(self, ruta):

      try:

          if os.path.exists(ruta):
              return tk.PhotoImage(file=ruta)

      except Exception:
          return None

      return None

  # ==========================================================
  # ADMINISTRADOR
  # ==========================================================
 
  def es_administrador(self):

      if self.usuario_actual is None:
          return False

      if hasattr(self.usuario_actual, "rol"):
          return self.usuario_actual.rol == "Administrador"

      return False

  # ==========================================================
  # LIMPIAR CONTENIDO
  # ==========================================================

  def limpiar_contenido(self):

      for widget in self.contenido.winfo_children():
          widget.destroy()

  # ==========================================================
  # USUARIOS - SEMANA 16
  # ==========================================================

  def mostrar_usuarios(self):

      if not self.es_administrador():

          messagebox.showwarning(
              "Acceso",
              "Solo el Administrador puede gestionar usuarios."
          )

          return

      self.limpiar_contenido()

      formulario = tk.LabelFrame(
          self.contenido,
          text="Gestión de usuarios",
          padx=10,
          pady=10
      )

      formulario.pack(
          fill="x",
          pady=5
      )

      # ------------------------------------------------------
      # ID
      # ------------------------------------------------------

      tk.Label(
          formulario,
          text="ID:"
      ).grid(
          row=0,
          column=0,
          padx=5,
          pady=5
      )

      self.usuario_id_entry = tk.Entry(formulario)

      self.usuario_id_entry.grid(
          row=0,
          column=1,
          padx=5,
          pady=5
      )

      # ------------------------------------------------------
      # NOMBRE
      # ------------------------------------------------------

      tk.Label(
          formulario,
          text="Nombre:"
      ).grid(
          row=0,
          column=2,
          padx=5,
          pady=5
      )

      self.usuario_nombre_entry = tk.Entry(formulario)

      self.usuario_nombre_entry.grid(
          row=0,
          column=3,
          padx=5,
          pady=5
      )

      # ------------------------------------------------------
      # USUARIO
      # ------------------------------------------------------

      tk.Label(
          formulario,
          text="Usuario:"
      ).grid(
          row=1,
          column=0,
          padx=5,
          pady=5
      )

      self.usuario_usuario_entry = tk.Entry(formulario)

      self.usuario_usuario_entry.grid(
          row=1,
          column=1,
          padx=5,
          pady=5
      )

      # ------------------------------------------------------
      # CONTRASEÑA
      # ------------------------------------------------------

      tk.Label(
          formulario,
          text="Contraseña:"
      ).grid(
          row=1,
          column=2,
          padx=5,
          pady=5
      )

      self.usuario_contrasena_entry = tk.Entry(
          formulario,
          show="*"
      )

      self.usuario_contrasena_entry.grid(
          row=1,
          column=3,
          padx=5,
          pady=5
      )

      # ------------------------------------------------------
      # ROL
      # ------------------------------------------------------

      tk.Label(
          formulario,
          text="Rol:"
      ).grid(
          row=2,
          column=0,
          padx=5,
          pady=5
      )

      self.rol_combo = ttk.Combobox(
          formulario,
          state="readonly",
          values=[
              "Administrador",
              "Empleado",
              "Cliente"
          ],
          width=20
      )

      self.rol_combo.grid(
          row=2,
          column=1,
          padx=5,
          pady=5
      )

      self.rol_combo.bind(
          "<<ComboboxSelected>>",
          self.cambio_rol
      )

      # ------------------------------------------------------
      # BOTONES
      # ------------------------------------------------------

      botones = tk.Frame(
          formulario
      )

      botones.grid(
          row=3,
          column=0,
          columnspan=4,
          pady=10
      )

      ttk.Button(
          botones,
          text="Registrar",
          command=self.registrar_usuario
      ).grid(
          row=0,
          column=0,
          padx=5
      )

      ttk.Button(
          botones,
          text="Actualizar",
          command=self.actualizar_usuario
      ).grid(
          row=0,
          column=1,
          padx=5
      )

      ttk.Button(
          botones,
          text="Eliminar",
          command=self.eliminar_usuario
      ).grid(
          row=0,
          column=2,
          padx=5
      )

      ttk.Button(
          botones,
          text="Limpiar",
          command=self.limpiar_usuario
      ).grid(
          row=0,
          column=3,
          padx=5
      )

      # ------------------------------------------------------
      # EVENTOS DE TECLADO
      # ------------------------------------------------------

      formulario.bind(
          "<Return>",
          self.evento_return
      )

      formulario.bind(
          "<Escape>",
          self.evento_escape
      )

      self.usuario_id_entry.bind(
          "<Return>",
          self.evento_return
      )

      self.usuario_nombre_entry.bind(
          "<Return>",
          self.evento_return
      )

      self.usuario_usuario_entry.bind(
          "<Return>",
          self.evento_return
      )

      self.usuario_contrasena_entry.bind(
          "<Return>",
          self.evento_return
      )

      self.rol_combo.bind(
          "<Return>",
          self.evento_return
      )

      # ------------------------------------------------------
      # TABLA
      # ------------------------------------------------------

      tabla_frame = tk.LabelFrame(
          self.contenido,
          text="Usuarios registrados"
      )

      tabla_frame.pack(
          expand=True,
          fill="both",
          pady=5
      )

      columnas = (
          "id",
          "nombre",
          "usuario",
          "rol"
      )

      self.tabla_usuarios = ttk.Treeview(
          tabla_frame,
          columns=columnas,
          show="headings"
      )

      self.tabla_usuarios.heading(
          "id",
          text="ID"
      )

      self.tabla_usuarios.heading(
          "nombre",
          text="Nombre"
      )

      self.tabla_usuarios.heading(
          "usuario",
          text="Usuario"
      )

      self.tabla_usuarios.heading(
          "rol",
          text="Rol"
      )

      self.tabla_usuarios.column(
          "id",
          width=60
      )

      self.tabla_usuarios.column(
          "nombre",
          width=200
      )

      self.tabla_usuarios.column(
          "usuario",
          width=150
      )

      self.tabla_usuarios.column(
          "rol",
          width=130
      )

      scrollbar = ttk.Scrollbar(
          tabla_frame,
          orient="vertical",
          command=self.tabla_usuarios.yview
      )

      self.tabla_usuarios.configure(
          yscrollcommand=scrollbar.set
      )

      self.tabla_usuarios.pack(
          side="left",
          expand=True,
          fill="both"
      )

      scrollbar.pack(
          side="right",
          fill="y"
      )

      # EVENTO OBLIGATORIO

      self.tabla_usuarios.bind(
          "<<TreeviewSelect>>",
          self.seleccionar_usuario
      )

      self.cargar_tabla_usuarios()

      self.usuario_id_entry.focus()

  # ==========================================================
  # CARGAR TABLA USUARIOS
  # ==========================================================

  def cargar_tabla_usuarios(self):

      for item in self.tabla_usuarios.get_children():
          self.tabla_usuarios.delete(item)

      usuarios = self.servicio.listar_usuarios()

      for usuario in usuarios:

          self.tabla_usuarios.insert(
              "",
              "end",
              values=(
                  usuario.id,
                  usuario.nombre,
                  usuario.usuario,
                  usuario.rol
              )
          )

  # ==========================================================
  # TREEVIEWSELECT
  # ==========================================================

  def seleccionar_usuario(self, event):

      seleccion = self.tabla_usuarios.selection()

      if not seleccion:
          return

      item = self.tabla_usuarios.item(
          seleccion[0]
      )

      valores = item["values"]

      if not valores:
          return

      usuario_id = valores[0]

      usuario = self.servicio.buscar_usuario(
          usuario_id
      )

      if usuario is None:
          return

      self.usuario_id_entry.delete(
          0,
          tk.END
      )

      self.usuario_id_entry.insert(
          0,
          usuario.id
      )

      self.usuario_nombre_entry.delete(
          0,
          tk.END
      )

      self.usuario_nombre_entry.insert(
          0,
          usuario.nombre
      )

      self.usuario_usuario_entry.delete(
          0,
          tk.END
      )

      self.usuario_usuario_entry.insert(
          0,
          usuario.usuario
      )

      self.usuario_contrasena_entry.delete(
          0,
          tk.END
      )

      self.rol_combo.set(
          usuario.rol
      )

  # ==========================================================
  # REGISTRAR USUARIO
  # ==========================================================

  def registrar_usuario(self):

      id = self.usuario_id_entry.get().strip()
      nombre = self.usuario_nombre_entry.get().strip()
      usuario = self.usuario_usuario_entry.get().strip()
      contraseña = self.usuario_contrasena_entry.get().strip()
      rol = self.rol_combo.get().strip()

      if not id or not nombre or not usuario or not contraseña or not rol:

          messagebox.showwarning(
              "Campos vacíos",
              "Complete todos los campos."
          )

          return

      correcto, mensaje = self.servicio.registrar_usuario(
          id,
          nombre,
          usuario,
          contraseña,
          rol
      )

      if correcto:

          messagebox.showinfo(
              "Registro",
              mensaje
          )

          self.limpiar_usuario()
          self.cargar_tabla_usuarios()

      else:

          messagebox.showerror(
              "Error",
              mensaje
          )

  # ==========================================================
  # ACTUALIZAR USUARIO
  # ==========================================================

  def actualizar_usuario(self):

      id = self.usuario_id_entry.get().strip()
      nombre = self.usuario_nombre_entry.get().strip()
      usuario = self.usuario_usuario_entry.get().strip()
      contraseña = self.usuario_contrasena_entry.get().strip()
      rol = self.rol_combo.get().strip()

      if not id or not nombre or not usuario or not rol:

          messagebox.showwarning(
              "Campos vacíos",
              "Complete los campos obligatorios."
          )

          return

      correcto, mensaje = self.servicio.actualizar_usuario(
          id,
          nombre,
          usuario,
          contraseña,
          rol
      )

      if correcto:

          messagebox.showinfo(
              "Actualización",
              mensaje
          )

          self.limpiar_usuario()
          self.cargar_tabla_usuarios()

      else:

          messagebox.showerror(
              "Error",
              mensaje
          )

  # ==========================================================
  # ELIMINAR USUARIO
  # ==========================================================

  def eliminar_usuario(self):

      id = self.usuario_id_entry.get().strip()

      if not id:

          messagebox.showwarning(
              "Campo vacío",
              "Seleccione un usuario."
          )

          return

      confirmar = messagebox.askyesno(
          "Eliminar usuario",
          "¿Está seguro de eliminar este usuario?"
      )

      if not confirmar:
          return

      correcto, mensaje = self.servicio.eliminar_usuario(
          id,
          self.usuario_actual
      )

      if correcto:

          messagebox.showinfo(
              "Eliminación",
              mensaje
          )

          self.limpiar_usuario()
          self.cargar_tabla_usuarios()

      else:

          messagebox.showerror(
              "Error",
              mensaje
          )

  # ==========================================================
  # COMBOBOXSELECTED
  # ==========================================================

  def cambio_rol(self, event):

      rol = self.rol_combo.get()

      if rol == "Administrador":

          self.usuario_rol_mensaje = "Usuario con permisos administrativos."

      elif rol == "Empleado":

          self.usuario_rol_mensaje = "Usuario con permisos de empleado."

      elif rol == "Cliente":

          self.usuario_rol_mensaje = "Usuario con permisos de cliente."

      else:

          self.usuario_rol_mensaje = ""

  # ==========================================================
  # RETURN
  # ==========================================================

  def evento_return(self, event):

      self.registrar_usuario()

      return "break"

  # ==========================================================
  # ESCAPE
  # ==========================================================

  def evento_escape(self, event):

      self.limpiar_usuario()

      return "break"

  # ==========================================================
  # LIMPIAR USUARIO
  # ==========================================================

  def limpiar_usuario(self):

      self.usuario_id_entry.delete(
          0,
          tk.END
      )

      self.usuario_nombre_entry.delete(
          0,
          tk.END
      )

      self.usuario_usuario_entry.delete(
          0,
          tk.END
      )

      self.usuario_contrasena_entry.delete(
          0,
          tk.END
      )

      self.rol_combo.set("")

      for item in self.tabla_usuarios.selection():
          self.tabla_usuarios.selection_remove(item)

      self.usuario_id_entry.focus()

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

      tk.Label(formulario, text="ID:").grid(
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

      tk.Label(formulario, text="Nombre:").grid(
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

      tk.Label(formulario, text="Precio:").grid(
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

      tk.Label(formulario, text="Cantidad:").grid(
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

      for columna, texto in [
          ("id", "ID"),
          ("nombre", "Nombre"),
          ("precio", "Precio"),
          ("cantidad", "Cantidad")
      ]:

          self.tabla_productos.heading(
              columna,
              text=texto
          )

      self.tabla_productos.pack(
          expand=True,
          fill="both"
      )

      self.cargar_tabla_productos()

  def cargar_tabla_productos(self):

      for item in self.tabla_productos.get_children():
          self.tabla_productos.delete(item)

      for producto in self.servicio.listar_productos():

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

  def cargar_producto(self):

      id = self.id_entry.get()

      producto = self.servicio.buscar_producto(id)

      if producto is None:

          messagebox.showerror(
              "Error",
              "Producto no encontrado."
          )

          return

      self.nombre_entry.delete(0, tk.END)
      self.nombre_entry.insert(0, producto.nombre)

      self.precio_entry.delete(0, tk.END)
      self.precio_entry.insert(0, producto.precio)

      self.cantidad_entry.delete(0, tk.END)
      self.cantidad_entry.insert(0, producto.cantidad)

  def actualizar_producto(self):

      correcto, mensaje = self.servicio.actualizar_producto(
          self.id_entry.get(),
          self.nombre_entry.get(),
          self.precio_entry.get(),
          self.cantidad_entry.get()
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

  def eliminar_producto(self):

      id = self.id_entry.get()

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

  def limpiar_formulario(self):

      self.id_entry.delete(0, tk.END)
      self.nombre_entry.delete(0, tk.END)
      self.precio_entry.delete(0, tk.END)
      self.cantidad_entry.delete(0, tk.END)

  # ==========================================================
  # VENTAS
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

      self.usuario_combo["values"] = [
          f"{usuario.id} - {usuario.nombre}"
          for usuario in usuarios
      ]

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

      self.producto_combo["values"] = [
          f"{producto.id} - {producto.nombre}"
          for producto in productos
      ]

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

      self.tabla_ventas.pack(
          expand=True,
          fill="both"
      )

      self.cargar_tabla_ventas()

  def registrar_venta(self):

      usuario = self.usuario_combo.get()
      producto = self.producto_combo.get()

      if not usuario or not producto:

          messagebox.showwarning(
              "Venta",
              "Seleccione usuario y producto."
          )

          return

      usuario_id = usuario.split(" - ")[0]
      producto_id = producto.split(" - ")[0]

      correcto, mensaje = self.servicio.registrar_venta(
          usuario_id,
          producto_id
      )

      if correcto:

          messagebox.showinfo(
              "Venta",
              mensaje
          )

          self.usuario_combo.set("")
          self.producto_combo.set("")

          self.cargar_tabla_ventas()

      else:

          messagebox.showerror(
              "Error",
              mensaje
          )

  def cargar_tabla_ventas(self):

      for item in self.tabla_ventas.get_children():
          self.tabla_ventas.delete(item)

      for venta in self.servicio.listar_ventas():

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

