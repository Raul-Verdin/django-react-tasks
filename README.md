🗂️ Estructura del Proyecto
El proyecto está compuesto por un frontend en React y un backend en Django REST Framework, 
comunicándose a través de una API REST protegida por CSRF.

🔧 1. BACKEND – Django
📁 Ubicación del módulo de tareas: apps/tasks/

📄 apps/tasks/models.py
Modelo Task con campos:
    title: CharField
    description: TextField
    done: BooleanField

📄 apps/tasks/serializers.py
Serializador para convertir Task ↔ JSON.

📄 apps/tasks/views.py
Vista basada en viewsets.ModelViewSet, expone endpoints:
    GET /api/v1/tasks/
    POST /api/v1/tasks/
    GET /api/v1/tasks/<id>/
    PUT /api/v1/tasks/<id>/
    DELETE /api/v1/tasks/<id>/

📄 apps/tasks/urls.py
    from django.urls import include, path
    from rest_framework import routers
    from .views import TaskView

    router = routers.DefaultRouter()
    router.register(r"tasks", TaskView, basename="tasks")

    urlpatterns = [
        path("", include(router.urls)),
    ]

📄 project/urls.py (probable ubicación)
    from django.urls import path, include
    from .views import csrf  # o desde apps.tasks.views

    urlpatterns = [
        path("api/v1/", include("apps.tasks.urls")),
        path("api/csrf/", csrf, name="csrf"),
    ]

🌐 API ENDPOINTS
Método      Endpoint                Descripción
GET	        /api/v1/tasks/	        Listar tareas
POST	    /api/v1/tasks/	        Crear nueva tarea
GET	        /api/v1/tasks/<id>/	    Ver tarea por ID
PUT	        /api/v1/tasks/<id>/	    Editar tarea existente
DELETE	    /api/v1/tasks/<id>/	    Eliminar tarea por ID
GET	        /api/csrf/	            Obtener token CSRF

💻 2. FRONTEND – React + Vite
📄 src/api/tasks.api.js
    Encapsula llamadas a la API usando axios, incluyendo CSRF en cabecera.
    Ejemplo de función:
        export const getTask = (id) => tasksApi.get(`/${id}`);

📄 src/pages/TaskFormPage.jsx
    Permite crear o editar tareas.
    Si hay un params.id, obtiene la tarea vía getTask(id) y usa setValue(...) de react-hook-form para prellenar el formulario.

📄 src/pages/TasksList.jsx (asumido)
    Lista todas las tareas usando getAllTasks.

🛠️ Mejoras que puedes aplicar a futuro

✅ Validación más avanzada (longitud mínima, etc.)
✅ Agregar campo created_at, updated_at en el modelo
✅ Paginación en la API para tareas
🔐 Agregar autenticación de usuario (JWT o session + login)
📦 Test unitarios y e2e (Django & React)
📈 PWA o modo offline
📡 WebSockets para tareas en tiempo real
🌍 Despliegue (Render, Vercel + Railway, etc.)
🧪 Linter + prettier + Husky hooks en React
📚 Documentación OpenAPI (Swagger o ReDoc)

Para clonar en otro equipo:
    git clone https://github.com/Raul-Verdin/django-react-tasks.git
    cd django-react-tasks

💡 Para subir nuevos cambios a GitHub:
    git add .
    git commit -m "Mensaje breve del cambio"
    git push

