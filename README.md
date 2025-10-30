---#  API - Microservicio RESTful

Este proyecto es un microservicio construido con **Django 4.2+** y **Django REST Framework** , diseñado para funcionar en un entorno Dockerizado.

---

## Requisitos Previos

Necesitas tener instalado:
1.  **Git**
2.  **Docker** y **Docker Compose**
3.  **Python 3.8+** (para la instalación local)

## 🚀 Instalación y Ejecución

Puedes elegir entre una instalación local con entorno virtual o la ejecución inmediata con Docker.

### Opción 1: Ejecución con Docker (Recomendado)

1.  **Construir y Ejecutar Contenedores:**
    ```bash
    # En el directorio raíz (donde está docker-compose.yml)
    docker-compose up --build
    ```
    Esto construirá la imagen e iniciará el servidor.

2.  **Acceso a la API:**
    El servidor estará disponible en: [http://localhost:8000/api/productos/](http://localhost:8000/api/productos/)

### Opción 2: Instalación Local

1.  **Crear Entorno Virtual:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # o venv\Scripts\activate en Windows
    ```
2.  **Instalar Dependencias:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Iniciar Servidor:**
    ```bash
    python manage.py runserver
    ```
    Accede a la API en: [http://127.0.0.1:8000/api/productos/](http://127.0.0.1:8000/api/productos/)

---

## 💾 Gestión de Base de Datos y Migraciones

El proyecto utiliza **SQLite** por defecto.

### 1. Aplicar Migraciones

Una vez que el proyecto esté instalado/ejecutándose:

| Entorno | Comando |
| :--- | :--- |
| **Local** | `python manage.py migrate` |
| **Docker** | `docker exec wolf_api_web python manage.py migrate` |

### 2. Crear Superusuario (Opcional)

Para acceder al panel de administración de Django:

| Entorno | Comando |
| :--- | :--- |
| **Local** | `python manage.py createsuperuser` |
| **Docker** | `docker exec wolf_api_web python manage.py createsuperuser` |

---

## 🧪 Ejecutar Pruebas

El proyecto incluye pruebas básicas de *endpoints* (`productos/tests.py`).

| Entorno | Comando |
| :--- | :--- |
| **Local** | `python manage.py test productos` |
| **Docker** | `docker exec wolf_api_web python manage.py test productos` |

---

## 🌐 Documentación de Endpoints (API RESTful)

La API permite la gestión completa del modelo `Producto`.

**URL Base:** `/api/productos/`

| Método HTTP | Endpoint | Descripción | Requisito |
| :--- | :--- | :--- | :--- |
| **GET** | `/api/productos/` | Lista todos los productos disponibles. | Listar productos |
| **POST** | `/api/productos/` | Crea un nuevo producto. | Crear producto |
| **GET** | `/api/productos/{id}/` | Obtiene los detalles de un producto específico. | Obtener producto |
| **PUT** | `/api/productos/{id}/` | Reemplaza/Actualiza completamente un producto. | Actualizar producto |
| **DELETE** | `/api/productos/{id}/` | Elimina un producto específico. | Eliminar producto |

### Estructura del Objeto `Producto`

| Campo | Tipo | Requerido | Descripción |
| :--- | :--- | :--- | :--- |
| `id` | Integer | No (Autogenerado) | Clave primaria. |
| `nombre` | String (max 100) | Sí | Nombre del producto. |
| `descripcion` | Text | No | Descripción detallada (opcional). |
| `precio` | Decimal (10, 2) | Sí | Precio del producto. |
| `disponible` | Boolean | No (Default=True) | Indica si el producto está en stock. |
# API_with_Docker_Compose_Wolf
 Microservicio en Django REST Framework que permita la gestión de productos mediante  una API RESTful.
