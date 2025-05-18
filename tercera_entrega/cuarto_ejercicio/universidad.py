# A diferencia de Java, en python el constructor de la clase padre no se invoca automáticamente si el hijo define su propio método constructor. 
# Para lograr este comportamiento de invocar el constructor padre, debemos llamarlo explícitamente
# Para más detalle: https://blog.chuidiang.org/2022/08/07/comparacion-de-constructores-en-java-y-en-python/


class Persona:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getDireccion(self):
        return self.direccion

    def setDireccion(self, direccion):
        self.direccion = direccion



class Estudiante(Persona):
    def __init__(self, nombre, direccion, carrera, semestre):
        super().__init__(nombre, direccion)
        self.carrera = carrera
        self.semestre = semestre

    def getCarrera(self):
        return self.carrera

    def setCarrera(self, carrera):
        self.carrera = carrera

    def getSemestre(self):
        return self.semestre

    def setSemestre(self, semestre):
        self.semestre = semestre


class Profesor(Persona):
    def __init__(self, nombre, direccion, departamento, categoria):
        super().__init__(nombre, direccion)
        self.departamento = departamento
        self.categoria = categoria

    def getDepartamento(self):
        return self.departamento

    def setDepartamento(self, departamento):
        self.departamento = departamento

    def getCategoria(self):
        return self.categoria

    def setCategoria(self, categoria):
        self.categoria = categoria

# Prueba
print("\nEstudiante:")
estudiante = Estudiante("Ana Chaverra", "Avenida peru # 74-82", "Ingeniería", 5)
print(f"Nombre: {estudiante.getNombre()} \nDirección: {estudiante.getDireccion()} \nCarrera: {estudiante.getCarrera()} \nSemestre: {estudiante.getSemestre()}")


print("\nProfesor:")
profesor = Profesor("Luis Pedro", "Calle romero #45-67", "Matemáticas", "Titular")
print(f"Nombre: {profesor.getNombre()} \nDirección: {profesor.getDireccion()} \nDepartamento: {profesor.getDepartamento()} \nCategoría: {profesor.getCategoria()}")

