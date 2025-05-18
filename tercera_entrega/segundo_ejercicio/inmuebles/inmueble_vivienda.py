from .inmueble import Inmueble

class InmuebleVivienda(Inmueble):
    def __init__(self, identificador_inmobiliario, area, direccion, habitaciones, banos):
        super().__init__(identificador_inmobiliario, area, direccion)
        self.habitaciones = habitaciones
        self.banos = banos

    def imprimir(self):
        super().imprimir()
        print(f"Habitaciones: {self.habitaciones}")
        print(f"Baños: {self.banos}")