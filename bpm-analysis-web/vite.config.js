import { defineConfig } from 'vite';

export default defineConfig({
  server: {
    host: true,
    port: 3000
  },
  build: {
    rollupOptions: {
      external: [],
      output: {
        manualChunks: {
          'plotly': ['plotly.js-dist']
        }
      }
    }
  },
  optimizeDeps: {
    include: ['plotly.js-dist']
  }
});