# Restaurante App - Semana 16

## Nombre del estudiante

**Melany Jaña**

## Descripción

Restaurante App es una aplicación de escritorio desarrollada en Python utilizando Programación Orientada a Objetos (POO) y la biblioteca Tkinter para la construcción de la interfaz gráfica.

El proyecto corresponde a la evolución del sistema desarrollado en semanas anteriores. Para la Semana 16 se incorporó la gestión básica de usuarios, incluyendo roles, registro, consulta, actualización y eliminación de usuarios mediante un formulario y un Treeview.

La aplicación mantiene las funcionalidades desarrolladas anteriormente, como el inicio de sesión, la gestión de productos y el registro de ventas.

## Objetivo

El objetivo de la Semana 16 es implementar la gestión de usuarios dentro de la aplicación Restaurante App, incorporando el atributo `rol` al modelo `Usuario` y permitiendo administrar los usuarios mediante una interfaz gráfica.

También se utilizan eventos de Tkinter para mejorar la interacción con el usuario, manteniendo la lógica de validación, las operaciones y la persistencia dentro de `RestauranteServicio`.

## Funcionalidades del sistema

- Inicio de sesión mediante usuario y contraseña.
- Validación de usuarios.
- Gestión de usuarios.
- Registro de usuarios.
- Consulta de usuarios.
- Actualización de usuarios.
- Eliminación de usuarios.
- Asignación de roles.
- Control de acceso según el rol.
- Gestión de productos.
- Registro de ventas.
- Control de stock.
- Persistencia de usuarios.
- Persistencia de productos.
- Persistencia de ventas.
- Uso de archivos JSON.
- Interfaz gráfica desarrollada con Tkinter.
- Uso de logo e íconos desde la carpeta `assets`.

## Roles de usuario

### Administrador

El Administrador tiene acceso a la gestión de usuarios y puede realizar las operaciones administrativas disponibles en el sistema.

### Empleado

El Empleado puede utilizar las funciones correspondientes a la operación del restaurante, como productos y ventas, de acuerdo con los permisos establecidos.

### Cliente

El Cliente representa un usuario registrado dentro del sistema.

## Gestión de usuarios

La gestión de usuarios permite realizar las operaciones básicas de un CRUD:

- Registrar usuarios.
- Consultar usuarios.
- Actualizar usuarios.
- Eliminar usuarios.

Los usuarios se presentan mediante un `Treeview`, desde donde se puede seleccionar un registro para cargar sus datos en el formulario.

La información del usuario incluye:

- ID.
- Nombre.
- Usuario.
- Contraseña.
- Rol.

El rol se selecciona mediante un `Combobox` con las opciones:

- Administrador.
- Empleado.
- Cliente.

## Eventos utilizados

En la Semana 16 se utilizan diferentes mecanismos de eventos de Tkinter para mejorar la interacción con la interfaz.

### `<<TreeviewSelect>>`

Se utiliza para detectar cuando el usuario selecciona un registro dentro del Treeview y cargar sus datos en el formulario.

### `bind()`

Permite asociar eventos de la interfaz con funciones o callbacks.

### `<Return>`

Permite utilizar la tecla Enter para ejecutar una acción del formulario.

### `<Escape>`

Permite limpiar el formulario y la selección realizada.

### `<<ComboboxSelected>>`

Permite detectar el cambio de selección en el ComboBox de roles.

### `command=`

Los botones principales utilizan `command=` para ejecutar las funciones correspondientes.

## Flujo de gestión de usuarios

```text
Inicio de la aplicación
        ↓
LoginView
        ↓
Validación mediante RestauranteServicio
        ↓
MainView
        ↓
Administrador accede a "Usuarios"
        ↓
Formulario + Treeview
        ↓
Selecciona una fila
        ↓
<<TreeviewSelect>>
        ↓
bind() → callback(event)
        ↓
Obtiene el identificador del usuario
        ↓
RestauranteServicio busca el usuario
        ↓
Carga los datos en el formulario
        ↓
Actualizar / Eliminar / Limpiar
        ↓
Persistencia en usuarios.json
        ↓
Actualización del Treeview
```

La interfaz se encarga de recibir las acciones del usuario y actualizar la vista, mientras que las validaciones, operaciones y persistencia son realizadas por `RestauranteServicio`.

## Persistencia de datos

La aplicación utiliza archivos JSON para almacenar la información y conservarla cuando el programa se cierra.

Los archivos utilizados son:

```text
datos/
├── usuarios.json
├── productos.json
└── ventas.json
```

### usuarios.json

Contiene la información de los usuarios registrados y su respectivo rol.

### productos.json

Contiene la información de los productos disponibles y su stock.

### ventas.json

Contiene la información de las ventas registradas.

Para la lectura y escritura de información se utiliza `ArchivoServicio`, que trabaja con `json.load()` y `json.dump()`.

## Gestión de productos

El sistema mantiene la gestión de productos desarrollada en semanas anteriores.

Permite:

- Consultar productos.
- Registrar productos.
- Actualizar productos.
- Eliminar productos.
- Consultar el stock disponible.

La información de los productos se mantiene en `productos.json`.

## Gestión de ventas

La aplicación también mantiene el módulo de ventas.

El registro de una venta relaciona un usuario con un producto.

Al realizar una venta correctamente:

1. Se verifica que el producto exista.
2. Se verifica que exista stock disponible.
3. Se identifica al usuario.
4. Se registra la venta.
5. Se disminuye el stock.
6. Se guarda la información actualizada.

Las ventas se almacenan en `datos/ventas.json`.

## Estructura del proyecto

```text
Repositorio GitHub
│
├── restaurante__app/
│   │
│   ├── datos/
│   │   ├── productos.json
│   │   ├── usuarios.json
│   │   └── ventas.json
│   │
│   ├── modelos/
│   │   ├── __init__.py
│   │   ├── producto.py
│   │   └── usuario.py
│   │
│   ├── servicios/
│   │   ├── __init__.py
│   │   ├── archivo_servicio.py
│   │   └── restaurante_servicio.py
│   │
│   ├── ui/
│   │   ├── __init__.py
│   │   ├── login_view.py
│   │   └── main_view.py
│   │
│   ├── assets/
│   │   └── imágenes, logo e íconos
│   │
│   └── main.py
│
└── README.md
```

## Responsabilidad de los componentes

### Modelos

La carpeta `modelos` contiene las clases que representan las entidades utilizadas por el sistema.

Entre ellas se encuentran:

- `Producto`
- `Usuario`

La clase `Usuario` contiene información como ID, nombre, usuario, contraseña y rol.

### Servicios

La carpeta `servicios` contiene las clases encargadas de las operaciones y la persistencia.

#### ArchivoServicio

Se encarga de leer y guardar información en archivos JSON mediante `json.load()` y `json.dump()`.

#### RestauranteServicio

Se encarga de las operaciones del sistema relacionadas con:

- Usuarios.
- Productos.
- Ventas.
- Validaciones.
- Persistencia.

De esta manera, la interfaz no contiene directamente toda la lógica del negocio.

### UI

La carpeta `ui` contiene las interfaces gráficas.

#### LoginView

Se encarga de mostrar la pantalla de inicio de sesión y validar las credenciales mediante `RestauranteServicio`.

#### MainView

Se encarga de mostrar la ventana principal y las diferentes secciones del sistema:

- Productos.
- Usuarios.
- Ventas.
- Cerrar sesión.

## Assets

La carpeta `assets` contiene los recursos visuales utilizados por la aplicación.

Se utilizan imágenes, logo e íconos para mejorar la presentación de la interfaz gráfica.

```text
assets/
```

Los recursos visuales son cargados desde la aplicación para mantener una interfaz clara y coherente.

## Manejo de validaciones

Las validaciones principales se realizan dentro de `RestauranteServicio`.

Entre las validaciones implementadas se encuentran:

- Verificación de credenciales.
- Verificación de existencia de usuarios.
- Verificación de IDs duplicados.
- Verificación de nombres de usuario duplicados.
- Validación del rol.
- Verificación de existencia de productos.
- Verificación del stock disponible.
- Validación de datos ingresados.

También se evita eliminar accidentalmente el usuario que se encuentra actualmente conectado.

## Manejo de excepciones

El sistema utiliza manejo de excepciones para controlar posibles errores durante la lectura y escritura de archivos y durante la validación de datos.

De esta manera se evita que un error detenga inesperadamente la aplicación.

## Ejecución del proyecto

Para ejecutar el proyecto se debe ingresar a la carpeta:

```text
restaurante__app
```

Luego se ejecuta el archivo:

```text
main.py
```

Desde la terminal se puede utilizar:

```bash
python main.py
```

También se puede ejecutar directamente desde Visual Studio Code.

## Flujo general de la aplicación

```text
Inicio
  ↓
LoginView
  ↓
Ingreso de usuario y contraseña
  ↓
RestauranteServicio valida las credenciales
  ↓
MainView
  ↓
┌─────────────────────────────┐
│ Productos                   │
│ Usuarios                    │
│ Ventas                      │
│ Cerrar sesión               │
└─────────────────────────────┘
  ↓
Operaciones del sistema
  ↓
Persistencia en archivos JSON
```

## Comprobación mínima de funcionamiento

Para comprobar el funcionamiento del sistema se realizaron las siguientes pruebas:

1. Ejecutar `main.py` y comprobar que la aplicación inicia correctamente.
2. Verificar que se muestre primero la pantalla de inicio de sesión.
3. Comprobar el ingreso de usuario y contraseña.
4. Verificar que los campos vacíos generen una respuesta visual.
5. Comprobar que las credenciales incorrectas sean rechazadas.
6. Ingresar con credenciales válidas.
7. Verificar que el Administrador pueda acceder a la sección Usuarios.
8. Registrar un nuevo usuario.
9. Comprobar que el usuario aparezca en el Treeview.
10. Seleccionar una fila del Treeview.
11. Verificar que `<<TreeviewSelect>>` cargue los datos en el formulario.
12. Modificar los datos de un usuario.
13. Comprobar que la opción Actualizar conserve los cambios.
14. Seleccionar un usuario y comprobar la opción Eliminar.
15. Verificar la confirmación antes de eliminar un usuario.
16. Comprobar que el usuario Administrador actualmente conectado no pueda eliminarse accidentalmente.
17. Verificar que la tecla Enter ejecute el registro mediante `<Return>`.
18. Verificar que la tecla Escape permita limpiar el formulario.
19. Comprobar que el ComboBox de rol responda mediante `<<ComboboxSelected>>`.
20. Verificar que los usuarios se guarden correctamente en `usuarios.json`.
21. Cerrar y volver a ejecutar la aplicación.
22. Comprobar que los usuarios se recuperen correctamente desde `usuarios.json`.
23. Verificar que Productos continúe funcionando.
24. Verificar que Ventas continúe funcionando.
25. Comprobar que el stock se actualice después de una venta válida.
26. Verificar que las ventas se almacenen en `ventas.json`.

## Tecnologías utilizadas

- Python
- Tkinter
- Programación Orientada a Objetos (POO)
- JSON
- Visual Studio Code
- Git
- GitHub

## Conclusión

La Semana 16 permitió continuar con la evolución del proyecto Restaurante App mediante la incorporación de la gestión de usuarios y roles.

Se implementaron operaciones de registro, consulta, actualización y eliminación de usuarios mediante una interfaz gráfica con Treeview y formulario. También se incorporaron eventos de Tkinter como `bind()`, `<<TreeviewSelect>>`, `<Return>`, `<Escape>` y `<<ComboboxSelected>>`.

El proyecto mantiene la separación entre modelos, servicios, interfaz y datos, permitiendo que las validaciones y la persistencia sean gestionadas por `RestauranteServicio`.

Además, se conservaron las funcionalidades desarrolladas en semanas anteriores, como el inicio de sesión, la gestión de productos y el registro de ventas.

