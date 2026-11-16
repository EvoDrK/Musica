from abc import ABC, abstractmethod

class DescargadorContenido(ABC):
    """Clase abstracta que define el contrato obligatorio para cualquier descargador."""
    
    def __init__(self, ruta_destino: str):
        self._ruta_destino = ruta_destino  # Atributo protegido

    @property
    def ruta_destino(self) -> str:
        return self._ruta_destino

    @ruta_destino.setter
    def ruta_destino(self, nueva_ruta: str):
        if not nueva_ruta:
            raise ValueError("La ruta de destino no puede estar vacía.")
        self._ruta_destino = nueva_ruta

    @abstractmethod
    def descargar(self, url: str, callback_progreso=None) -> bool:
        """Método abstracto que implementarán las clases derivadas (Polimorfismo)."""
        pass