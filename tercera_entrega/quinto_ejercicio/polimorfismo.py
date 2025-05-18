class Profesor:
    def imprimir(self):
        print("Es un profesor.")

class ProfesorTitular(Profesor):
    def imprimir(self):
        print("Es un profesor titular.")


#Prueba
profesor1: Profesor = ProfesorTitular()
profesor1.imprimir() 