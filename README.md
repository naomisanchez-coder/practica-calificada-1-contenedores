# Práctica Calificada 1: Dockerización de Aplicaciones Web y Web Scraping

Este repositorio contiene la solución completa de la Práctica Calificada 1, demostrando el uso de **Docker**, optimización de imágenes mediante construcciones multi-stage, desarrollo en Python y documentación de evidencias.

---

## Caso 1: Descargador de Videos Multi-Plataforma (Flask + yt-dlp)

Aplicación web desarrollada en Python con Flask que permite la descarga de videos desde redes sociales (YouTube, TikTok, Instagram, Facebook, LinkedIn) utilizando la librería `yt-dlp`.

### Estrategia de Dockerización y Optimización

Se desarrollaron tres variantes de `Dockerfile` para comparar la reducción de peso y eficiencia de las imágenes:

1. **`Dockerfile` (Estándar):** Basado en `python:3.10-slim`.
2. **`Dockerfile.optimizado` (Alpine):** Basado en `python:3.10-alpine`.
3. **`Dockerfile.multistage` (Multi-stage Build):** Separa la etapa de compilación de dependencias de la etapa final de ejecución sobre Alpine Linux.

---

### Instrucciones de Construcción y Ejecución

#### 1. Navegar a la carpeta del Caso 1
```bash
cd caso1-video-downloader