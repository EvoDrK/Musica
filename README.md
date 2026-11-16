# MusicaPy - Gestor y Descargador de Audio con POO

Aplicación de escritorio desarrollada en Python con interfaz gráfica moderna, diseñada bajo el paradigma de **Programación Orientada a Objetos (POO)** para la gestión y descarga de contenido de audio autorizado desde plataformas multimedia.

---

## 1. Descripción del Problema
La necesidad de gestionar archivos de audio locales requiere herramientas de software desacopladas, modulares y fáciles de usar. Este proyecto resuelve la tarea mediante una interfaz limpia y una arquitectura orientada a objetos que separa la lógica de red, los modelos de datos y la vista gráfica.

## 2. Objetivos
* Aplicar los pilares fundamentales de la POO (Encapsulamiento, Herencia, Polimorfismo y Abstracción).
* Integrar una interfaz gráfica moderna utilizando `CustomTkinter`.
* Evitar el bloqueo de la interfaz mediante programación concurrente (`threading`).

## 3. Funcionalidades Principales
1. **Ingreso y validación de enlaces:** Permite capturar la URL multimedia de origen.
2. **Selección de ruta de destino:** Permite elegir dinámicamente la carpeta del sistema donde se almacenará el archivo MP3 resultante.
3. **Conversión y descarga en segundo plano:** Extrae el flujo de audio con `yt-dlp` notificando el progreso en tiempo real sin congelar la ventana.

## 4. Tecnologías Utilizadas
* **Lenguaje:** Python 3.10+
* **Interfaz Gráfica:** CustomTkinter
* **Extracción Multimedia:** yt-dlp
* **Concurrencia:** Threading (Python Standard Library)

## 5. Instalación
1. Clona el repositorio en tu computador.
2. Instala las dependencias ejecutando en la terminal:
   ```bash
   pip install -r requirements.txt