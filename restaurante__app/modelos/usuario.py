class Usuario:

    def __init__(
        self,
        id,
        nombre,
        usuario,
        contraseña,
        rol="Cliente"
    ):

        self.id = id
        self.nombre = nombre
        self.usuario = usuario
        self.contraseña = contraseña
        self.rol = rol