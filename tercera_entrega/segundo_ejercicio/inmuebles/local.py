from .inmueble import Inmueble
from enum import Enum

class TipoLocal(Enum):
    INTERNO = "Interno"
    CALLE = "Calle"

class Local(Inmueble):
    def __init__(self, identificador_inmobiliario, area, direccion, tipo_local: TipoLocal):
        super().__init__(identificador_inmobiliario, area, direccion)
        if not isinstance(tipo_local, TipoLocal):
            raise ValueError("tipo_local debe ser una instancia de TipoLocal")
        else:
            self.tipo_local = tipo_local

    def imprimir(self):
        super().imprimir()
        print(f"Tipo de local: {self.tipo_local.value}")
