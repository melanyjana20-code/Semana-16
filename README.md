# Restaurante App

## Descripción

Restaurante App es una aplicación desarrollada en Python utilizando Tkinter y Programación Orientada a Objetos.

El proyecto permite gestionar usuarios y productos de un restaurante. Para la Semana 15 se incorporó la funcionalidad de Ventas, manteniendo las funcionalidades desarrolladas anteriormente.

## Funcionalidades

-   Inicio de sesión de usuarios.
    
-   Validación de usuario y contraseña.
    
-   Consulta de usuarios registrados.
    
-   Registro de productos.
    
-   Consulta de productos.
    
-   Actualización de productos.
    
-   Eliminación de productos.
    
-   Registro de ventas.
    
-   Selección de usuario mediante `Combobox`.
    
-   Selección de producto mediante `Combobox`.
    
-   Visualización de ventas mediante `Treeview`.
    
-   Persistencia de las ventas en un archivo JSON.
    
-   Uso de logo e íconos mediante la carpeta `assets`.
    

## Funcionalidad de Ventas

La funcionalidad de ventas permite relacionar un usuario con un producto y registrar la fecha en que se realiza la operación.

El proceso funciona de la siguiente manera:

```text
Seleccionar usuario
        ↓
Seleccionar producto
        ↓
Presionar "Registrar venta"
        ↓
command=
        ↓
Callback registrar_venta()
        ↓
RestauranteServicio
        ↓
ventas.json
        ↓
Actualizar Treeview

```

La operación es gestionada por `RestauranteServicio`, manteniendo la separación entre la interfaz gráfica y la lógica del programa.

## Persistencia

Las ventas se almacenan en:

```text
datos/ventas.json

```

Cada venta registra información del usuario, producto y fecha.

Ejemplo:

```json
[
    {
        "usuario": "Melany",
        "producto": "Hamburguesa",
        "fecha": "2026-09-27 16:30:00",
        "usuario_id": 1,
        "producto_id": 1
    }
]

```

## Eventos y callbacks

Para la interacción de la interfaz se utiliza el parámetro `command=` de Tkinter.

El botón de registro de ventas ejecuta el método:

```python
command=self.registrar_venta

```

El método `registrar_venta()` obtiene los datos seleccionados y solicita al servicio que registre la operación.

## Estructura del proyecto

```text
restaurante__app/
│
├── assets/
│   ├── logo.png
│   ├── usuarios.png
│   ├── productos.png
│   ├── ventas.png
│   └── salir.png
│
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
│
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
│
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
│
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
│
└── main.py

```

## Carpeta assets

La carpeta `assets` contiene los recursos gráficos utilizados por la aplicación.

Los archivos utilizados son:

-   `logo.png`: logotipo de la aplicación.
    
-   `usuarios.png`: ícono para usuarios.
    
-   `productos.png`: ícono para productos.
    
-   `ventas.png`: ícono para ventas.
    
-   `salir.png`: ícono para cerrar sesión.
    

## Tecnologías utilizadas

-   Python
    
-   Tkinter
    
-   ttk
    
-   JSON
    
-   Programación Orientada a Objetos
    

## Inicio de sesión

Para realizar las pruebas de la aplicación se pueden utilizar las credenciales registradas en `datos/usuarios.json`.

### Usuario administrador

```text
Usuario: admin
Contraseña: 1234

```

### Usuario mesero

```text
Usuario: mesero
Contraseña: 1235

```

## Ejecución del proyecto

Para ejecutar la aplicación se debe abrir una terminal dentro de la carpeta `restaurante__app` y utilizar:

```bash
python main.py

```

## Prueba de la funcionalidad de ventas

1.  Ejecutar `main.py`.
    
2.  Iniciar sesión.
    
3.  Ingresar a la opción **Ventas**.
    
4.  Seleccionar un usuario.
    
5.  Seleccionar un producto.
    
6.  Presionar **Registrar venta**.
    
7.  Verificar que la venta aparezca en el `Treeview`.
    
8.  Revisar el archivo `datos/ventas.json` para comprobar la persistencia.
    

## Conclusión

En esta semana se incorporó el módulo de ventas al proyecto del restaurante. La nueva funcionalidad permite relacionar usuarios y productos, registrar la fecha de la operación, guardar la información en un archivo JSON y mostrar las ventas en la interfaz gráfica.

También se incorporaron recursos gráficos en la carpeta `assets`, manteniendo una estructura organizada del proyecto.