from .mascota import Mascota

class Gato(Mascota):
    def __init__(self, nombre, edad, color, altura_salto, longitud_salto):
        super().__init__(nombre, edad, color)
        self.altura_salto = altura_salto
        self.longitud_salto = longitud_salto

    @staticmethod
    def sonido():
        print("Los gatos maúllan y ronronean")

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Altura de salto: {self.altura_salto} cm \nLongitud de salto: {self.longitud_salto} cm")
