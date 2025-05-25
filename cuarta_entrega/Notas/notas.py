import math

class Notas():
    """
    Esta clase denominada Notas define una lista de notas numéricas de
    tipo float.
    """
    def __init__(self):
        """
        Constructor de la clase Notas, instancia una lista vacía para las notas.
        Las notas se asignarán posteriormente usando la interfaz gráfica
        """
        self.listaNotas = []

    def set_notas(self, notas_list):
        """
        Método para asignar las notas a la lista.
        - Se verifica que hayan 5 notas
        - Se verifica que todos y cada uno de los elementos n en la lista de notas sea un número entero o decimal
        (esto para evitar que se ingresen caracteres no numericos)

        """
        if len(notas_list) == 5 and all(isinstance(n, (int, float)) for n in notas_list):
            self.listaNotas = [float(n) for n in notas_list]
        else:
            raise ValueError("Se deben ingresar exactamente 5 notas numéricas.")

    def calcular_promedio(self):
        # Método que calcula el promedio de notas.
        
        if not self.listaNotas:
            return 0.0
        return sum(self.listaNotas) / len(self.listaNotas)

    def calcular_desviacion(self):
    
        # Método que calcula la desviación estándar de la lista de notas.

        if not self.listaNotas:
            return 0.0
        prom = self.calcular_promedio()
        suma = sum([(x - prom) ** 2 for x in self.listaNotas])
        return math.sqrt(suma / len(self.listaNotas))

    def calcular_menor(self):
        # Método que calcula el valor menor de la lista de notas.
        
        if not self.listaNotas:
            return 0.0
        return min(self.listaNotas)

    def calcular_mayor(self):
        
        # Método que calcula el valor mayor de la lista de notas.
        if not self.listaNotas:
            return 0.0
        return max(self.listaNotas)