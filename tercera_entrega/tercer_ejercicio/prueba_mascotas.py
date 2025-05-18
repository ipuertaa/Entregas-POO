from tienda_mascotas.razas_perros import Schnauzer, PastorAleman
from tienda_mascotas.razas_gatos import Angora, Esfinge

print("\nMascotas en la tienda:\n")

perro1 = Schnauzer("Max", 4, "Gris", 8.5, False)
perro1.mostrar_info()
perro1.sonido()

print()
perro2 = PastorAleman("Rex", 6, "Negro y fuego", 35.0, True)
perro2.mostrar_info()
perro2.sonido()

print()
gato1 = Angora("Luna", 3, "Blanco", 70, 120)
gato1.mostrar_info()
gato1.sonido()

print()
gato2 = Esfinge("Cleopatra", 5, "Beige", 65, 100)
gato2.mostrar_info()
gato2.sonido()