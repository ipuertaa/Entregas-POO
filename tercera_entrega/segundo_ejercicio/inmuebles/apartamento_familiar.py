from .apartamento import Apartamento

class ApartamentoFamiliar(Apartamento):
    valor_area = 2000000

    def __init__(self, identificador_inmobiliario, area, direccion, habitaciones, banos, valor_administracion):
        super().__init__(identificador_inmobiliario, area, direccion, habitaciones, banos)
        self.valor_administracion = valor_administracion

    def imprimir(self):
        super().imprimir()
        print(f"Valor de la administración: ${self.valor_administracion}")