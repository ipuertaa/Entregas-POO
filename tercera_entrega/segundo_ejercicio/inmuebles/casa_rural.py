from .casa import Casa

class CasaRural(Casa):
    valor_area = 1500000

    def __init__(self, identificador_inmobiliario, area, direccion, habitaciones, banos, pisos, distancia_cabecera, altitud):
        super().__init__(identificador_inmobiliario, area, direccion, habitaciones, banos, pisos)
        self.distancia_cabecera = distancia_cabecera
        self.altitud = altitud

    def imprimir(self):
        super().imprimir()
        print(f"Distancia a cabecera municipal: {self.distancia_cabecera} km")
        print(f"Altitud sobre el nivel del mar: {self.altitud} msnm")