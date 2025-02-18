# Aethelred API

Esta API proporciona la funcionalidad para el juego de rol de mesa Aethelred. Permite a los jugadores gestionar personajes, tarjetas y partidas.

## Descripción general

La API está construida con Django REST Framework y sigue una arquitectura RESTful. Esto significa que utiliza métodos HTTP (GET, POST, PUT, DELETE) para realizar operaciones en los recursos (datos) del juego.

## Rutas

A continuación, se describen las rutas principales de la API:

### Autenticación

*   `POST /api/token/`: Obtiene un token de autenticación.
*   `POST /api/token/refresh/`: Refresca un token de autenticación.

### Usuarios

*   `GET /api/users/`: Lista todos los usuarios (solo para administradores).
*   `GET /api/users/{id}/`: Obtiene un usuario específico (solo para usuarios autenticados).
*   `POST /api/users/create/`: Crea un nuevo usuario.

### Jugadores

*   `GET /api/jugadores/`: Lista todos los jugadores.
*   `GET /api/jugadores/{id}/`: Obtiene un jugador específico.
*   `POST /api/jugadores/`: Crea un nuevo jugador.
*   `PUT /api/jugadores/{id}/`: Actualiza un jugador existente.
*   `DELETE /api/jugadores/{id}/`: Elimina un jugador.

### Tarjetas

*   `GET /api/tarjetas/`: Lista todas las tarjetas.
*   `GET /api/tarjetas/{id}/`: Obtiene una tarjeta específica.
*   `POST /api/tarjetas/`: Crea una nueva tarjeta.
*   `PUT /api/tarjetas/{id}/`: Actualiza una tarjeta existente.
*   `DELETE /api/tarjetas/{id}/`: Elimina una tarjeta.

### Inventario

*   `GET /api/inventarios/`: Lista todos los elementos del inventario.
*   `GET /api/inventarios/{id}/`: Obtiene un elemento del inventario específico.
*   `POST /api/inventarios/`: Crea un nuevo elemento en el inventario.
*   `PUT /api/inventarios/{id}/`: Actualiza un elemento del inventario existente.
*   `DELETE /api/inventarios/{id}/`: Elimina un elemento del inventario.

### Partidas

*   `GET /api/partidas/`: Lista todas las partidas.
*   `GET /api/partidas/{id}/`: Obtiene una partida específica.
*   `POST /api/partidas/`: Crea una nueva partida.
*   `PUT /api/partidas/{id}/`: Actualiza una partida existente.
*   `DELETE /api/partidas/{id}/`: Elimina una partida.

## Uso

Para utilizar la API, necesitarás obtener un token de autenticación. Esto se puede hacer enviando una solicitud POST a la ruta `/api/token/` con tus credenciales de usuario. Una vez que tengas el token, deberás incluirlo en la cabecera `Authorization` de todas las solicitudes a las rutas protegidas.


## Desarrollo

Para ejecutar la API localmente, necesitarás tener instalado Python y Django. Luego, sigue estos pasos:

1.  Clona el repositorio.
2.  Crea un entorno virtual.
3.  Instala las dependencias con `pip install -r requirements.txt`.
4.  Ejecuta el servidor de desarrollo con `python manage.py runserver`.

## Contribución

Si deseas contribuir a este proyecto, por favor, abre un "issue" o envía un "pull request" en el repositorio.

## Licencia

Este proyecto está bajo la licencia MIT.