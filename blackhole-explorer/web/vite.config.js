import { defineConfig } from "vite";

export default defineConfig({
  server: {
    port: 5202,
    proxy: {
      "/api": {
        target: "http://localhost:5102",
        changeOrigin: true,
      },
    },
  },
});
