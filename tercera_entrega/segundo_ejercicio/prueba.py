from inmuebles.apartamento_familiar import ApartamentoFamiliar
from inmuebles.apartaestudio import Apartaestudio

print("Datos apartamento familiar")
apto1 = ApartamentoFamiliar(103067, 120, "Avenida Santander 45-45", 3, 2, 200000)
apto1.calcular_precio_venta(ApartamentoFamiliar.valor_area)
apto1.imprimir()

print("\nDatos apartaestudio")
aptestudio1 = Apartaestudio(12354, 50, "Avenida Caracas 30-15", 1, 1)
aptestudio1.calcular_precio_venta(Apartaestudio.valor_area)
aptestudio1.imprimir()