import os
import yt_dlp
from servicios.descargador_base import DescargadorContenido

class DescargadorAudio(DescargadorContenido):
    """Especialización para descargar y convertir contenido multimedia a audio (MP3)."""

    def __init__(self, ruta_destino: str, calidad_kbps: str = "192"):
        super().__init__(ruta_destino)
        self.__calidad_kbps = calidad_kbps  # Encapsulamiento estricto

    @property
    def calidad_kbps(self) -> str:
        return self.__calidad_kbps

    def descargar(self, url: str, callback_progreso=None) -> bool:
        """Implementación concreta del método abstracto (Polimorfismo)."""
        def hook_progreso(d):
            if d['status'] == 'downloading' and callback_progreso:
                porcentaje = d.get('_percent_str', '0%').strip()
                callback_progreso(porcentaje)

        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(self.ruta_destino, '%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': self.__calidad_kbps,
            }],
            'progress_hooks': [hook_progreso],
            'noplaylist': True
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            return True
        except Exception as e:
            print(f"Error en la descarga: {e}")
            return False