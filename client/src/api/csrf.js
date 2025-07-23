import axios from "axios";

export const getCSRFToken = async () => {
  try {
    await axios.get(`${import.meta.env.VITE_BACKEND_URL}/api/csrf/`, {
      withCredentials: true,
    });
    console.log("✅ CSRF token recibido");
  } catch (error) {
    console.error("❌ Error al obtener CSRF token", error);
  }
};
