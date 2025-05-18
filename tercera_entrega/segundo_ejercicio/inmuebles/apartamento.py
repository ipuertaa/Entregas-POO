from .inmueble_vivienda import InmuebleVivienda

class Apartamento(InmuebleVivienda):
    def __init__(self, identificador_inmobiliario, area, direccion, habitaciones, banos):
        super().__init__(identificador_inmobiliario, area, direccion, habitaciones, banos)

    def imprimir(self):
        super().imprimir()
