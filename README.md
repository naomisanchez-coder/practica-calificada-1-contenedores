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

# Caso 2: Consulta ONPE - Contenedorización y Optimización con Docker

Este proyecto forma parte de la **Práctica Calificada 1: Contenedores**. En este caso de estudio se aborda el proceso completo de contenedorización, optimización y construcción multietapa (*Multi-stage Build*) de una aplicación en Python dedicada a la consulta de información de la ONPE.

---

## 📋 Descripción del Proyecto

El objetivo principal es llevar una aplicación en Python desde su empaquetado inicial hasta una versión altamente optimizada en producción, comparando el peso de las imágenes y la eficiencia en la construcción mediante el uso de diferentes estrategias de Docker.

Se trabajaron tres versiones distintas de la imagen Docker:
1. **Versión Base (`v1.0`)**: Basada en una imagen oficial de Python en versión *slim* (`python:3.10-slim`).
2. **Versión Optimizada (`v1.1-alpine`)**: Basada en Alpine Linux (`python:3.10-alpine`), instalando las dependencias necesarias a nivel del sistema operativo.
3. **Versión Multietapa (`v1.2-alpine`)**: Construcción en varias etapas (*Multi-stage build*) para separar el entorno de compilación del entorno de ejecución final.

---

## 🛠️ Estructura del Proyecto

```text
caso2-consulta-onpe/
├── Dockerfile              # Configuración base (python:3.10-slim)
├── Dockerfile.optimizado   # Configuración optimizada basada en Alpine Linux
├── Dockerfile.multistage   # Configuración multietapa (Multi-stage Build)
├── requirements.txt        # Dependencias de Python requeridas
├── app.py                  # Código fuente de la aplicación
└── README.md               # Documentación general del proyecto