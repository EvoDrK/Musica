class PistaAudio:
    """Representa una pista de audio con atributos encapsulados y validaciones."""

    def __init__(self, titulo: str, artista: str, duracion: int, url: str):
        self.__titulo = titulo
        self.__artista = artista
        self.__duracion = duracion  # en segundos
        self.__url = url

    @property
    def titulo(self) -> str:
        return self.__titulo

    @property
    def artista(self) -> str:
        return self.__artista

    @property
    def duracion(self) -> str:
        minutos = self.__duracion // 60
        segundos = self.__duracion % 60
        return f"{minutos:02d}:{segundos:02d}"

    @property
    def url(self) -> str:
        return self.__url