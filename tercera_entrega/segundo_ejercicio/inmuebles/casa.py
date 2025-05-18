from .inmueble_vivienda import InmuebleVivienda

class Casa(InmuebleVivienda):
    def __init__(self, identificador_inmobiliario, area, direccion, habitaciones, banos, pisos):
        super().__init__(identificador_inmobiliario, area, direccion, habitaciones, banos)
        self.pisos = pisos

    def imprimir(self):
        super().imprimir()
        print(f"Número de pisos: {self.pisos}")