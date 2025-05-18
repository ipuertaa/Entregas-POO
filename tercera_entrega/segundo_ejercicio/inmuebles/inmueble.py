
class Inmueble:
    def __init__(self, identificador_inmobiliario, area, direccion):
        self.identificador_inmobiliario = identificador_inmobiliario
        self.area = area
        self.direccion = direccion
        self.precio_venta = 0.0

    def calcular_precio_venta(self, valor_area):
        self.precio_venta = self.area * valor_area
        return self.precio_venta

    def imprimir(self):
        print(f"Identificador inmobiliario: {self.identificador_inmobiliario}")
        print(f"Área: {self.area} m²")
        print(f"Dirección: {self.direccion}")
        print(f"Precio de venta: ${self.precio_venta:.2f}")