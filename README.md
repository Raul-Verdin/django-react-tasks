# ✅ Aplicación de Gestión de Tareas – Fullstack con React + Django REST
El proyecto está compuesto por un frontend en React y un backend en Django REST Framework, comunicándose a través de una API REST protegida por CSRF.

## 📁 Estructura General del Repositorio

├── config/ (o nombre del proyecto Django)
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py               ← Configuración global: CORS, CSRF, apps
│   ├── urls.py                   ← Incluye rutas del API y CSRF
│   └── wsgi.py

├── apps/
│   └── tasks/
│       ├── models.py             ← Modelo Task (title, description, done)
│       ├── serializers.py        ← Serializador para Task
│       ├── views.py              ← CRUD + endpoint `/api/csrf/`
│       ├── urls.py               ← Router DRF para `/api/v1/tasks/`
│       └── migrations/

├── client/ (o frontend/)
│   ├── src/
│   │   ├── api/
│   │   │   ├── tasks.api.js      ← Axios, CSRF headers y rutas API
│   │   │   └── csrf.js (opcional)← Petición directa a `/api/csrf/`
│   │   ├── components/
│   │   │   ├── Navigation.jsx    ← Navegación principal
│   │   │   ├── TaskCard.jsx      ← Tarjeta individual de tarea
│   │   │   └── TasksList.jsx     ← Lista de tareas
│   │   ├── pages/
│   │   │   ├── TaskFormPage.jsx  ← Formulario de crear/editar tarea
│   │   │   └── TasksPage.jsx     ← Página principal
│   │   ├── App.jsx               ← Rutas y lógica inicial (CSRF)
│   │   └── main.jsx              ← Punto de entrada React
│   ├── .env                      ← `VITE_BACKEND_URL=http://localhost:8000`
│   └── vite.config.js

├── requirements/                ← Requisitos separados por entorno
│   ├── base.txt                  ← Paquetes comunes: Django, DRF, etc.
│   ├── dev.txt                   ← Herramientas de desarrollo (yapf, ipython, etc.)
│   └── prod.txt                  ← Producción: gunicorn, whitenoise, etc.

├── manage.py                    ← Script de Django
├── db.sqlite3                   ← Base de datos local
├── staticfiles/                 ← Archivos para producción (build)
└── README.md                    ← Documentación general

### 📌 INSTRUCCIONES PARA CORRER Y PROBAR EL PROYECTO

🔁 Clonar el repositorio

git clone https://github.com/Raul-Verdin/django-react-tasks.git
cd django-react-tasks

🐍 Configurar el entorno virtual (solo backend)

1. Crear el entorno virtual en la raiz del proyecto
python -m venv venv

2. Activar el entorno virtual
PowerShell (Windows):
    .\venv\Scripts\Activate.ps1

Si ves un error de permisos, ejecuta esto una sola vez:
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned

3. 📦 Instalar dependencias del backend
🔧 Puedes elegir entre 3 archivos de requirements:

Archivo	  Uso	                      Comando
base.txt	Requisitos base	          pip install -r requirements/base.txt
dev.txt	  Desarrollo local	        pip install -r requirements/dev.txt
prod.txt	Producción / despliegue	  pip install -r requirements/prod.txt

🐍 INSTRUCCIONES PARA CORRER

1. 🚀 Iniciar el backend (Django)
--------------------------------
Desde la raíz del backend (donde está `manage.py`):

> python manage.py migrate
> python manage.py runserver

Esto iniciará el backend en: http://localhost:8000


2. 💻 Iniciar el frontend (React + Vite)
----------------------------------------
Desde la carpeta `client/` según tu estructura:

> npm install
> npm run dev

Esto lanza el frontend en: http://localhost:5173


3. 🔧 Variables de entorno necesarias
-------------------------------------
Archivo: client/.env o frontend/.env

Contenido:
VITE_BACKEND_URL=http://localhost:8000


⚠️ Problemas comunes

❌ Error 403 Forbidden:
  - Asegúrate de que tu frontend usa `withCredentials: true` en axios
  - Verifica que el backend tenga configurado correctamente:
    - `CORS_ALLOWED_ORIGINS`
    - `CSRF_TRUSTED_ORIGINS`
  - Visita directamente `/api/csrf/` en el navegador para ver si se genera la cookie

❌ Error 404 con tareas nuevas:
  - A veces las tareas creadas no aparecen por problemas de redirección o de base de datos
  - Revisa `http://localhost:8000/api/v1/tasks/` para ver todas las tareas
  - Verifica que estés accediendo a un ID existente

❌ URL malformada `/undefined/api/v1/tasks/`:
  - Asegúrate de haber definido `VITE_BACKEND_URL` correctamente en `.env`
  - Reinicia el servidor con `npm run dev`


#### 📝 Informacion 

---

🌐 Rutas disponibles

🎯 FRONTEND (React + Vite):
- http://localhost:5173/                     → Redirige a /tasks
- http://localhost:5173/tasks               → Lista todas las tareas
- http://localhost:5173/tasks-create        → Formulario para crear tarea
- http://localhost:5173/tasks/:id           → Editar tarea existente

📡 BACKEND (Django API):
- http://localhost:8000/api/v1/tasks/         → `GET` (listar), `POST` (crear)
- http://localhost:8000/api/v1/tasks/<id>/    → `GET`, `PUT`, `DELETE`
- http://localhost:8000/api/csrf/             → ✅ Devuelve y establece la cookie CSRF

🧪 DOCUMENTACIÓN API:
(opcional si instalaste drf-yasg o similar)
- http://localhost:8000/api/docs/     → Swagger
- http://localhost:8000/api/redoc/    → Redoc


✅ Seguridad CSRF (implementada)
- Se hace una llamada inicial a `/api/csrf/` en el `App.jsx`
- El token CSRF se guarda como cookie `csrftoken`
- Cada petición `POST`, `PUT`, `DELETE` incluye el header `X-CSRFToken`
  (ver `tasks.api.js`)

---

🌱 Trabajo con Ramas
Este proyecto está organizado en una sola rama principal:

Rama	    Descripción
main	    Versión integrada de backend + frontend

---

✅ GUARDAR CAMBIOS en GitHub

1. 🧭 Asegúrate de estar en la raíz del proyecto

2. 📦 Verifica los archivos modificados
git status

3. ➕ Agrega todos los cambios
git add .

4. 📝 Haz el commit
git commit -m "Que cambios hiciste"

5. 🚀 Sube tus cambios a GitHub
git push origin main

---

🛠️ Mejoras que se pueden aplicar a futuro

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

---