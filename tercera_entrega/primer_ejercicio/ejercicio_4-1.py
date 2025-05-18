## Solución Ejercicio 4.1 página 194

class Cuenta():
    def __init__(self, saldo, tasa_anual):
      self._saldo = float(saldo)
      self._numero_consignaciones = 0
      self._numero_retiros = 0
      self._tasa_anual = float(tasa_anual)
      self._comision_mensual = 0.0

    def consignar(self, cantidad):
      self._saldo += cantidad
      self._numero_consignaciones += 1

    def retirar(self, cantidad):
      if self._saldo >= cantidad:
          self._saldo -= cantidad
          self._numero_retiros += 1
      else:
          print("La cantidad a retirar excede el saldo actual.")

    def calcular_interes(self):
      tasa_mensual = self._tasa_anual / 12
      interes_mensual = self._saldo * tasa_mensual
      self._saldo += interes_mensual

    def extracto_mensual(self):
      self._saldo -= self._comision_mensual
      self.calcular_interes()

    def imprimir(self):
      print(f'''Saldo = ${self._saldo:.3f}
Comisión mensual = ${self._comision_mensual:.2f}
Número de transacciones = {self._numero_consignaciones + self._numero_retiros}''')

class CuentaAhorros(Cuenta):
    def __init__(self, saldo, tasa):
        super().__init__(saldo, tasa)
        # Verificar si la cuenta tiene mas de 10000 o no
        self._activa = saldo >= 10000

    def consignar(self, cantidad):
        if self._activa:
            super().consignar(cantidad)

    def retirar(self, cantidad):
        if self._activa:
            super().retirar(cantidad)

    def extracto_mensual(self):
        if self._numero_retiros > 4:
            self._comision_mensual += (self._numero_retiros - 4) * 1000
        super().extracto_mensual()
        #Verificar de nuevo si la cuenta está activa o no
        self._activa = self._saldo >= 10000

    def imprimir(self):
        print("\nCuenta de Ahorros:\n")
        super().imprimir()


class CuentaCorriente(Cuenta):
    def __init__(self, saldo, tasa):
        super().__init__(saldo, tasa)
        self._sobregiro = 0.0

    def retirar(self, cantidad):
        resultado = self._saldo - cantidad
        if resultado < 0:
            self._sobregiro -= resultado
            self._saldo = 0
        else:
            super().retirar(cantidad)

    def consignar(self, cantidad):
      residuo = self._sobregiro - cantidad
      if (self._sobregiro > 0):
        if residuo > 0:
          self._sobregiro = 0
          self._saldo = residuo
        else:
          self._sobregiro = residuo * (-1)
          self._saldo = 0
      else:
        super().consignar(cantidad)

    def extracto_mensual(self):
      super().extracto_mensual()


    def imprimir(self):
        print("\nCuenta Corriente:")
        print(f"Cargo mensual = ${self._comision_mensual:.2f}")
        print(f"Valor de sobregiro = ${self._sobregiro:.2f}\n")


# Programa de prueba

if __name__ == "__main__":
    saldo = float(input("Ingrese saldo inicial: $"))
    tasa = float(input("Ingrese tasa de interés (decimal, ej: 0.015): "))
    cuenta = CuentaAhorros(saldo, tasa)
    deposito = float(input("Ingresar cantidad a consignar: $"))
    cuenta.consignar(deposito)
    retiro = float(input("Ingresar cantidad a retirar: $"))
    cuenta.retirar(retiro)
    cuenta.extracto_mensual()
    cuenta.imprimir()