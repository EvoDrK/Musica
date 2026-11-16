import customtkinter as ctk
import threading
from tkinter import filedialog, messagebox
from servicios.descargador_audio import DescargadorAudio

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class VentanaPrincipal(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("MusicaPy - Descargador de Audio con POO")
        self.geometry("650x450")
        self.resizable(False, False)

        # Carpeta por defecto inicial
        self.__ruta_descarga = filedialog.askdirectory(title="Selecciona la carpeta de destino") or "."

        self._crear_componentes()

    def _crear_componentes(self):
        # Título principal
        self.lbl_titulo = ctk.CTkLabel(self, text="Gestor y Descargador de Música (POO)", font=("Arial", 20, "bold"))
        self.lbl_titulo.pack(pady=20)

        # Campo de Entrada de URL
        self.lbl_url = ctk.CTkLabel(self, text="Enlace de YouTube autorizado:")
        self.lbl_url.pack(anchor="w", padx=50)
        
        self.txt_url = ctk.CTkEntry(self, width=540, placeholder_text="https://www.youtube.com/watch?v=...")
        self.txt_url.pack(padx=50, pady=5)

        # Botón para cambiar carpeta de destino
        self.btn_carpeta = ctk.CTkButton(self, text="Cambiar Carpeta de Destino", command=self._seleccionar_carpeta)
        self.btn_carpeta.pack(pady=10)

        # Botón de Descarga
        self.btn_descargar = ctk.CTkButton(self, text="Descargar MP3", fg_color="green", hover_color="darkgreen", command=self._iniciar_descarga_hilo)
        self.btn_descargar.pack(pady=15)

        # Estado y Retroalimentación
        self.lbl_estado = ctk.CTkLabel(self, text="Estado: Listo para iniciar", text_color="gray")
        self.lbl_estado.pack(pady=5)

        self.progress = ctk.CTkProgressBar(self, width=540)
        self.progress.set(0)
        self.progress.pack(pady=10)

    def _seleccionar_carpeta(self):
        carpeta = filedialog.askdirectory()
        if carpeta:
            self.__ruta_descarga = carpeta
            messagebox.showinfo("Carpeta Actualizada", f"Destino cambiado a:\n{carpeta}")

    def _iniciar_descarga_hilo(self):
        url = self.txt_url.get().strip()
        if not url:
            messagebox.showwarning("Advertencia", "Por favor ingresa un enlace web válido.")
            return

        # Desactivar controles durante el proceso
        self.btn_descargar.configure(state="disabled")
        self.lbl_estado.configure(text="Estado: Procesando descarga en segundo plano...")
        
        # Ejecutar en hilo independiente (Threading) para evitar congelar la interfaz gráfica
        hilo = threading.Thread(target=self._ejecutar_descarga, args=(url,))
        hilo.daemon = True
        hilo.start()

    def _ejecutar_descarga(self, url):
        descargador = DescargadorAudio(self.__ruta_descarga)
        
        def actualizar_progreso(porcentaje_str):
            self.lbl_estado.configure(text=f"Descargando: {porcentaje_str}")

        exito = descargador.descargar(url, callback_progreso=actualizar_progreso)

        if exito:
            self.lbl_estado.configure(text="Estado: ¡Descarga completada con éxito!")
            messagebox.showinfo("Éxito", "El archivo de audio se ha descargado y convertido a MP3 correctamente.")
        else:
            self.lbl_estado.configure(text="Estado: Error en la descarga.")
            messagebox.showerror("Error", "No se pudo completar la operación. Verifica la URL o tu conexión.")

        self.btn_descargar.configure(state="normal")
        self.progress.set(0)