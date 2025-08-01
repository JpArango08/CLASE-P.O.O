class Calificaciones:
    def __init__(self, Nombre, edad, M1, M2, M3):
        self.Nombre=Nombre
        self.edad=edad
        self.M1=M1
        self.M2=M2
        self.M3=M3
    def Datos(self):
        print("Nombre:", self.Nombre)
        print("Edad:", self.edad)
        print("Nota 1:", M1)
        print("Nota 2:", M2)
        print("Nota 3:", M3)
    def Prom(self):
        prom=(self.M1 + self.M2 + self.M3)/3
        return prom

listaEstudiante= [ ] 
while True:
    print("1. Agregar Estudiante")
    print("2. Mostrar información de Estudiantes")
    print("3. Mostrar promedio")
    print("0. Salir")
    opcion=int(input())
    if opcion==1:
        print("Ingrese el nombre del estudiante:")
        Nombre=input()
        print("Ingrese la edad del estudiante:")
        edad=int(input())
        print("Ingrese la nota 1 del estudiante:")
        M1=float(input())
        print("Ingrese la nota 2 del estudiante:")
        M2=float(input())
        print("Ingrese la nota 3 del estudiante:")
        M3=float(input())
        estudiante=Calificaciones(Nombre,edad,M1,M2,M3)
        listaEstudiante.append(estudiante)
    if opcion==2:
        numEstudiantes=len(listaEstudiante)
        for estudiante in listaEstudiante:
            print("El nombre del estudiante es:", estudiante.Nombre)
            print("El promedio del estudiante es:", estudiante.Prom())
    elif opcion==0:
        break
    else:
        print("Opción incorrecta")
