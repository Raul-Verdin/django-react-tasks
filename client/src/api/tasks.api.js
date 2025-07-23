import axios from "axios";

const URL = import.meta.env.VITE_BACKEND_URL || "http://localhost:8000";

console.log("✅ Backend URL:", URL);

const tasksApi = axios.create({
  baseURL: `${URL}/api/v1/tasks`,
  withCredentials: true, // 🔑 clave para enviar cookies
});

// ✅ Función para leer el CSRF token de la cookie
function getCSRFToken() {
  const match = document.cookie.match(/csrftoken=([\w-]+)/);
  const token = match ? match[1] : null;
  if (!token) {
    console.warn("⚠️ CSRF token no encontrado. ¿Ya llamaste a /api/csrf/?");
  }
  return token;
}

export const getAllTasks = () => tasksApi.get("/");

export const getTask = (id) => tasksApi.get(`/${id}/`);

export const createTask = (task) =>
  tasksApi.post("/", task, {
    headers: {
      "X-CSRFToken": getCSRFToken(),
    },
  });

export const updateTask = (id, task) =>
  tasksApi.put(`/${id}/`, task, {
    headers: {
      "X-CSRFToken": getCSRFToken(),
    },
  });

export const deleteTask = (id) =>
  tasksApi.delete(`/${id}/`, {
    headers: {
      "X-CSRFToken": getCSRFToken(),
    },
  });
