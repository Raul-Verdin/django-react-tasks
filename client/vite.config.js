import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  base: process.env.NODE_ENV === 'production' ? '/static/' : '/',
  define: {
    'process.env': {}, // 🧠 Previene errores con paquetes que usan process.env
  },
  server: {
    port: 5173, // Asegura que el frontend corre desde este puerto
  },
});
