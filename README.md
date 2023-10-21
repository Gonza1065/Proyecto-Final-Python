# Tienda Virtual - README

## Descripción

Este proyecto es una tienda virtual desarrollada con Django, diseñada para vender gorras, remeras y pantalones. Los usuarios pueden explorar productos, publicar sus propias prendas y gestionar su perfil.

## Características

- **Catálogo de Productos:** Los usuarios pueden explorar y comprar gorras, remeras y pantalones desde la página de inicio.

- **Publicar Prenda:** Los usuarios pueden publicar sus propias prendas completando un formulario con detalles como nombre, descripción e imagen.

- **Mis Prendas Publicadas:** Los usuarios pueden ver una lista de todas las prendas que han publicado, y tienen la opción de actualizar o eliminar sus productos.

- **Autenticación:** Los usuarios deben registrarse o iniciar sesión para acceder a las funcionalidades de la tienda. Se incluye la opción de cerrar sesión.

- **Acerca de Mí:** La página incluye información personal del creador del sitio, incluyendo detalles sobre su vida, estudios y gustos personales, junto con una foto.

## Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/Gonza1065/Final-Python.git
```

2. Crea un entorno virtual (se recomienda utilizar `virtualenv`)

```bash
python -m venv venv
```

3. Activa el entorno virtual

- Windows:

```bash
venv\Scripts\activate
```

- macOS y Linux:

```bash
source venv/bin/activate
```

4. Instala las dependencias

```bash
pip install -r requirements.txt
```

5. Ejecuta las migraciones

```bash
python manage.py migrate
```

6. Inicia el servidor de desarrollo

```bash
python manage.py runserver
```

## Uso

- Navega por las diferentes secciones de la tienda: Gorras, Remeras, Pantalones.
- Para publicar una prenda, haz clic en "Publicar prenda" en el menú de navegación, completa el formulario y presiona "Crear producto". Tu prenda se publicará instantáneamente.
- En "Mis prendas publicadas", puedes ver y gestionar las prendas que has publicado. Puedes actualizar o eliminar tus productos.
- Para acceder a todas las funcionalidades, regístrate o inicia sesión. Puedes cerrar sesión en cualquier momento haciendo clic en "Logout" en el menú de navegación.
- Visita la sección "Acerca de Mí" para obtener más información sobre el creador del sitio.

## Contribuciones

1. Fork del repositorio en GitHub.
2. Crea una nueva rama para tus cambios.
3. Realiza tus cambios y realiza un pull request en el repositorio original.

## Funcionamiento de la página (video)

https://www.youtube.com/watch?v=4tpqqCbeMLU&t=4s
