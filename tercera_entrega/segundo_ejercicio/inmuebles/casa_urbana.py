from .casa import Casa

class CasaUrbana(Casa):
    def __init__(self, identificador_inmobiliario, area, direccion, habitaciones, banos, pisos):
        super().__init__(identificador_inmobiliario, area, direccion, habitaciones, banos, pisos)

    def imprimir(self):
        super().imprimir()