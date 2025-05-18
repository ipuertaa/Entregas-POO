class Mascota:
    def __init__(self, nombre, edad, color):
        self.nombre = nombre
        self.edad = edad
        self.color = color

    def mostrar_info(self):
        print(f"Nombre: {self.nombre} \nEdad: {self.edad} \nColor: {self.color}")