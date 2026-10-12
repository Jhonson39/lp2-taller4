# Taller 4: Adopta una Mascota

Proyecto sencillo para practicar una aplicación web usando Docker Compose. Está pensado para una persona que está empezando y trabaja desde Visual Studio Code.

## ¿Qué hace?
Muestra mascotas que buscan hogar. Puedes ver la lista, filtrar por tipo de animal y consultar los detalles de cada mascota.

## Los 4 contenedores
- **reverse-proxy:** Nginx. Es la única parte que publica el puerto 80.
- **frontend:** página web sencilla con HTML, CSS y JavaScript.
- **api:** API hecha con FastAPI.
- **database:** PostgreSQL 15, donde se guardan los datos.

## Relación entre las tablas
Una **categoría** puede tener muchas **mascotas**. Por ejemplo, la categoría "Perros" puede tener a Luna y Max. Cada mascota pertenece a una categoría.

## Requisitos
- Docker Desktop instalado y abierto.
- Visual Studio Code.
- Extensión de Docker en VS Code (opcional, pero útil).

## Pasos para ejecutar en Windows y VS Code

1. Descarga y descomprime el ZIP.
2. Abre Visual Studio Code.
3. Ve a **Archivo > Abrir carpeta** y selecciona `taller4_adopta_mascotas`.
4. En VS Code, abre **Terminal > Nueva terminal**.
5. Copia el archivo de ejemplo de variables de entorno:

   ```powershell
   Copy-Item .env.example .env
   ```

6. Construye y levanta los contenedores:

   ```powershell
   docker compose up -d --build
   ```

7. Carga los datos de ejemplo una sola vez:

   ```powershell
   docker compose exec api python -m app.seed
   ```

8. Abre estas direcciones en el navegador:
   - Página web: http://localhost
   - Documentación de la API: http://localhost/api/docs

## ¿Cómo comprobar que funciona?
- En la página web deben aparecer mascotas.
- Puedes elegir una categoría para filtrar la lista.
- Pulsa **Ver detalles** para consultar la información de una mascota.
- En `/api/docs` puedes probar los endpoints de la API.

## Endpoints principales
- `GET /mascotas` — muestra todas las mascotas.
- `GET /mascotas/{id}` — muestra una mascota por su ID.
- `GET /mascotas?categoria_id=1` — filtra las mascotas por categoría.
- `GET /categorias` — muestra las categorías.

## Comandos útiles
Apagar los contenedores:

```powershell
docker compose down
```

Volver a construir si haces cambios:

```powershell
docker compose up -d --build
```

