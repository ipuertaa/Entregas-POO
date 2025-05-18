from .casa_urbana import CasaUrbana

class CasaIndependiente(CasaUrbana):
    valor_area = 3000000

    def __init__(self, identificador_inmobiliario, area, direccion, habitaciones, banos, pisos):
        super().__init__(identificador_inmobiliario, area, direccion, habitaciones, banos, pisos)

    def imprimir(self):
        super().imprimir()