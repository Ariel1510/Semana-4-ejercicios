class Dog():
    nombreP = ""
    razaP = ""
    edadP = 0
    sexo = ""
    peso = 0
    Tamanno = ""
    Discapacidad = True
    _Tipo = ""
    Estado = "No atendido"

    def __init__(self,):
        self._Tipo = "Perro"

    def tipo(self):
        return self._Tipo
    
    def StateCliente(self):
        Estado = "Atendido"
        return Estado
    
def PasarDatos(Dog, nameDog, razaDog, edadDog, sexoDog, pesoDog, tamannoDog, discapacidadDog):
    Dog.nombreP = nameDog
    Dog.razaP = razaDog
    Dog.edadP = edadDog
    Dog.sexo = sexoDog
    Dog.peso = pesoDog
    Dog.Tamanno = tamannoDog
    Dog.Discapacidad = discapacidadDog

def GetDatos(Dog):
    print("~~~~~ Ingrese los datos del perro ~~~~~")
    nameDog = input("Ingrese el nombre de la mascota: ")
    razaDog = input("Ingrese la raza del perro: ")
    edadDog = int(input("Ingrese la edad del perro(años): "))
    sexoDog = input("Sexo del perro (M/F): ")
    pesoDog = float(input("Ingrese el peso del perro(Kg): "))
    if pesoDog >= 10:
        tamannoDog = "Perro Grande"
    elif pesoDog < 10:
        tamannoDog = "Perro pequeño"

    discapacidadDog = input("¿El perro posee alguna discapacidad? (si/no): ")
    if discapacidadDog.lower() in ["sí", "si"]:
        discapacidadDog = True
    elif discapacidadDog.lower == "no":
        discapacidadDog = False
    PasarDatos(Dog, nameDog, razaDog, edadDog, sexoDog, pesoDog, tamannoDog, discapacidadDog)

def ShowDatos(Dog):
    print("~~~~~ DATOS DEL PACIENTE ~~~~~")
    print(f"Animal: {Dog.tipo()}")
    print(f"Nombre: {Dog.nombreP}")
    print(f"Raza: {Dog.razaP}")
    print(f"Edad: {Dog.edadP} años")
    print(f"Sexo: {Dog.sexo}")
    print(f"Peso: {Dog.peso} Kg")
    print(f"Tamaño: {Dog.Tamanno}")
    print(f"Posee discapacidad: {Dog.Discapacidad}")
    print(f"Estado del paciente: {Dog.StateCliente()}")

perro1 = Dog()
perro2 = Dog()

GetDatos(perro1)
GetDatos(perro2)

ShowDatos(perro1)
ShowDatos(perro2)