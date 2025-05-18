from .mascota import Mascota

class Perro(Mascota):
    def __init__(self, nombre, edad, color, peso, muerde):
        super().__init__(nombre, edad, color)
        self.peso = peso
        self.muerde = muerde

    @staticmethod
    def sonido():
        print("Los perros ladran")

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Peso: {self.peso} kg \n¿Muerde?: {self.muerde}")