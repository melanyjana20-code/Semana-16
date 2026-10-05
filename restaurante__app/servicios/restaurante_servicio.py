from modelos.producto import Producto
from modelos.usuario import Usuario


class RestauranteServicio:

    def __init__(
        self,
        usuarios,
        productos,
        archivo_servicio=None,
        ruta_productos=None,
        ruta_usuarios=None,
        ventas=None,
        ruta_ventas=None
    ):
        # =========================================================
        # USUARIOS
        # =========================================================

        self.usuarios = [
            Usuario(
                usuario["id"],
                usuario["nombre"],
                usuario["usuario"],
                usuario["contraseña"],
                usuario.get("rol", "Cliente")
            )
            for usuario in usuarios
        ]

        # =========================================================
        # PRODUCTOS
        # =========================================================

        self.productos = [
            Producto(
                producto["id"],
                producto["nombre"],
                producto["precio"],
                producto["cantidad"]
            )
            for producto in productos
        ]

        # =========================================================
        # CONFIGURACIÓN DE ARCHIVOS
        # =========================================================

        self.archivo_servicio = archivo_servicio
        self.ruta_productos = ruta_productos
        self.ruta_usuarios = ruta_usuarios
        self.ruta_ventas = ruta_ventas

        # =========================================================
        # VENTAS
        # =========================================================

        self.ventas = ventas if isinstance(ventas, list) else []

    # =========================================================
    # LOGIN
    # =========================================================

    def validar_usuario(self, usuario, contraseña):

        for u in self.usuarios:

            if u.usuario == usuario and u.contraseña == contraseña:
                return True

        return False

    def obtener_usuario(self, usuario, contraseña):

        for u in self.usuarios:

            if u.usuario == usuario and u.contraseña == contraseña:
                return u

        return None

    # =========================================================
    # USUARIOS
    # =========================================================

    def listar_usuarios(self):
        return self.usuarios

    def buscar_usuario(self, id):

        for usuario in self.usuarios:

            if str(usuario.id) == str(id):
                return usuario

        return None

    def registrar_usuario(
        self,
        id,
        nombre,
        usuario,
        contraseña,
        rol
    ):

        for u in self.usuarios:

            if str(u.id) == str(id):
                return False, "El ID del usuario ya existe."

            if u.usuario == usuario:
                return False, "El nombre de usuario ya existe."

        try:

            nuevo_usuario = Usuario(
                int(id),
                nombre,
                usuario,
                contraseña,
                rol
            )

        except ValueError:

            return False, "Los datos ingresados no son válidos."

        self.usuarios.append(nuevo_usuario)

        self.guardar_usuarios()

        return True, "Usuario registrado correctamente."

    def actualizar_usuario(
        self,
        id,
        nombre,
        usuario,
        contraseña,
        rol
    ):

        usuario_encontrado = self.buscar_usuario(id)

        if usuario_encontrado is None:
            return False, "Usuario no encontrado."

        usuario_encontrado.nombre = nombre
        usuario_encontrado.usuario = usuario
        usuario_encontrado.rol = rol

        if contraseña:
            usuario_encontrado.contraseña = contraseña

        self.guardar_usuarios()

        return True, "Usuario actualizado correctamente."

    def eliminar_usuario(self, id, usuario_actual=None):

        usuario_encontrado = self.buscar_usuario(id)

        if usuario_encontrado is None:
            return False, "Usuario no encontrado."

        # Evitar eliminar al usuario que está usando el sistema
        if (
            usuario_actual is not None
            and str(usuario_encontrado.id) == str(usuario_actual.id)
        ):
            return False, "No puede eliminar el usuario que está actualmente conectado."

        self.usuarios.remove(usuario_encontrado)

        self.guardar_usuarios()

        return True, "Usuario eliminado correctamente."

    def guardar_usuarios(self):

        if self.archivo_servicio is None:
            return

        if self.ruta_usuarios is None:
            return

        datos = []

        for usuario in self.usuarios:

            datos.append({
                "id": usuario.id,
                "nombre": usuario.nombre,
                "usuario": usuario.usuario,
                "contraseña": usuario.contraseña,
                "rol": usuario.rol
            })

        self.archivo_servicio.guardar_json(
            self.ruta_usuarios,
            datos
        )

    # =========================================================
    # PRODUCTOS
    # =========================================================

    def listar_productos(self):
        return self.productos

    def buscar_producto(self, id):

        for producto in self.productos:

            if str(producto.id) == str(id):
                return producto

        return None

    def registrar_producto(
        self,
        id,
        nombre,
        precio,
        cantidad
    ):

        for producto in self.productos:

            if str(producto.id) == str(id):
                return False, "El ID del producto ya existe."

        try:

            nuevo_producto = Producto(
                int(id),
                nombre,
                float(precio),
                int(cantidad)
            )

        except ValueError:

            return False, "Los datos ingresados no son válidos."

        self.productos.append(nuevo_producto)

        self.guardar_productos()

        return True, "Producto registrado correctamente."

    def actualizar_producto(
        self,
        id,
        nombre,
        precio,
        cantidad
    ):

        producto = self.buscar_producto(id)

        if producto is None:
            return False, "Producto no encontrado."

        try:

            producto.nombre = nombre
            producto.precio = float(precio)
            producto.cantidad = int(cantidad)

        except ValueError:

            return False, "Los datos ingresados no son válidos."

        self.guardar_productos()

        return True, "Producto actualizado correctamente."

    def eliminar_producto(self, id):

        producto = self.buscar_producto(id)

        if producto is None:
            return False, "Producto no encontrado."

        self.productos.remove(producto)

        self.guardar_productos()

        return True, "Producto eliminado correctamente."

    # =========================================================
    # GUARDAR PRODUCTOS
    # =========================================================

    def guardar_productos(self):

        if self.archivo_servicio is None:
            return

        if self.ruta_productos is None:
            return

        datos = []

        for producto in self.productos:

            datos.append({
                "id": producto.id,
                "nombre": producto.nombre,
                "precio": producto.precio,
                "cantidad": producto.cantidad
            })

        self.archivo_servicio.guardar_json(
            self.ruta_productos,
            datos
        )

    # =========================================================
    # VENTAS
    # =========================================================

    def registrar_venta(self, usuario_id, producto_id):

        producto = self.buscar_producto(producto_id)

        if producto is None:
            return False, "Producto no encontrado."

        # Comprobar stock
        if producto.cantidad <= 0:
            return False, "No hay stock disponible."

        # Buscar usuario
        usuario_encontrado = None

        for usuario in self.usuarios:

            if str(usuario.id) == str(usuario_id):
                usuario_encontrado = usuario
                break

        if usuario_encontrado is None:
            return False, "Usuario no encontrado."

        # Disminuir cantidad
        producto.cantidad -= 1

        # Crear venta
        from datetime import datetime

        venta = {
            "usuario": usuario_encontrado.nombre,
            "usuario_id": usuario_encontrado.id,
            "producto": producto.nombre,
            "producto_id": producto.id,
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        self.ventas.append(venta)

        # Guardar productos
        self.guardar_productos()

        # Guardar ventas
        self.guardar_ventas()

        return True, "Venta registrada correctamente."

    def listar_ventas(self):
        return self.ventas

    # =========================================================
    # GUARDAR VENTAS
    # =========================================================

    def guardar_ventas(self):

        if self.archivo_servicio is None:
            return

        if self.ruta_ventas is None:
            return

        self.archivo_servicio.guardar_json(
            self.ruta_ventas,
            self.ventas
        )