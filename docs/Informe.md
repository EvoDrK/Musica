# Informe Técnico — Proyecto MusicaPy

## 1. Análisis del problema
Se identificó la necesidad de automatizar la obtención de pistas de audio mediante un software modular. El sistema está dirigido a usuarios que buscan una herramienta de escritorio ligera, intuitiva y robusta para gestionar archivos multimedia de uso propio o autorizado.

## 2. Diseño inicial
Se planificó una arquitectura basada en capas para garantizar alta cohesión y bajo acoplamiento:
* **Modelos:** Representación de entidades puras (`PistaAudio`).
* **Servicios:** Clases encargadas de la lógica abstracta y concreta de descarga (`DescargadorContenido`, `DescargadorAudio`).
* **Interfaz:** Gestión visual de eventos y retroalimentación con el usuario (`VentanaPrincipal`).

## 3. Arquitectura
El flujo de comunicación opera de forma unidireccional: la interfaz gráfica captura los eventos del usuario, invoca los servicios especializados de descarga y estos actualizan el estado visual utilizando hilos independientes (`threading`).

## 4. Aplicación de Programación Orientada a Objetos (POO)

| Concepto | Clase o método | Archivo | Explicación |
| :--- | :--- | :--- | :--- |
| **Clases y objetos** | `PistaAudio` | `modelos/pista_audio.py` | Modela las propiedades y metadatos fundamentales de una canción. |
| **Encapsulamiento** | `__calidad_kbps` / `@property` | `servicios/descargador_audio.py` | Protege los atributos internos de configuración frente a modificaciones externas indebidas. |
| **Herencia** | `DescargadorAudio` | `servicios/descargador_audio.py` | Hereda los atributos y métodos comunes de la clase base `DescargadorContenido`. |
| **Polimorfismo** | `descargar()` | `servicios/descargador_audio.py` | Sobrescribe el método abstracto de la superclase para implementar la lógica específica de audio. |
| **Abstracción** | `DescargadorContenido` | `servicios/descargador_base.py` | Establece un contrato estricto mediante el módulo `ABC` y `@abstractmethod`. |
| **Relaciones** | `VentanaPrincipal` -> `DescargadorAudio` | `interfaz/ventana_principal.py` | Relación de asociación y colaboración para activar las operaciones en segundo plano. |

## 5. Construcción de la interfaz
Se seleccionó **CustomTkinter** debido a su estética moderna adaptada al sistema operativo. Se implementaron botones interactivos, campos de texto dinámicos y cuadros de diálogo nativos (`filedialog` y `messagebox`) conectados mediante funciones callback asíncronas.

## 6. Proceso de desarrollo
1. Definición de la idea y alcance funcional.
2. Diseño del diagrama de clases conceptual y jerarquía de herencia.
3. Implementación de los servicios de negocio con `yt-dlp`.
4. Desarrollo de la interfaz gráfica y acoplamiento mediante hilos.
5. Pruebas unitarias de integración y depuración de excepciones.

## 7. Pruebas de funcionamiento

| Prueba | Acción realizada | Resultado esperado | Resultado obtenido |
| :--- | :--- | :--- | :--- |
| **Prueba 1** | Ingresar una URL vacía y hacer clic en descargar. | Mostrar advertencia de enlace inválido sin bloquear la app. | Exitoso (Muestra advertencia modal). |
| **Prueba 2** | Cambiar la carpeta de destino mediante el selector. | Actualizar la ruta interna de almacenamiento correctamente. | Exitoso (Ruta modificada sin errores). |
| **Prueba 3** | Iniciar descarga con enlace válido y conexión activa. | Descargar el contenido, convertirlo a MP3 y notificar éxito. | Exitoso (Archivo guardado en disco). |

## 8. Problemas y soluciones
* **Problema 1:** Congelamiento de la ventana gráfica durante la descarga de archivos pesados.
  * *Solución:* Se implementó el módulo `threading` para aislar la ejecución de `yt-dlp` en un hilo secundario independiente del hilo principal de renderizado de la interfaz.
* **Problema 2:** Dependencia de códecs externos para la conversión de audio.
  * *Solución:* Se documentó formalmente la necesidad de instalar **FFmpeg** en el entorno local del sistema operativo para permitir la post-conversión automática a formato MP3.

## 9. Conclusiones
El desarrollo del proyecto permitió afianzar los conceptos teóricos de la POO en Python. La estructuración modular facilitó la ampliación de funcionalidades y demostró que una correcta separación de responsabilidades da como resultado un software robusto, mantenible y profesional.