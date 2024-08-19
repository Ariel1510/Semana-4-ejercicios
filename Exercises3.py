class auto():
    origen = ""
    __capacidad = 0
    __ruedas = 0
    marca = ""
    modelo = ""
    edicion = ""
    categoria = ""
    color = ""
    transmision = ""
    tipoFrenos = ""
    bolsasDeAire = 0
    seguro = 0
    precioCompra = 0
    precioVenta = 0
    __multiplicadorVenta = 0
    
    def __init__(self,):
        self.__capacidad=5
        self.__ruedas=4
        self.__multiplicadorVenta=1.4
    
    def capacidad(self):
        return self.__capacidad
        
    def ruedas(self):
        return self.__ruedas
    
    def multiplicadorVenta(self):
        return self.__multiplicadorVenta

def pasarDatos(auto,paisOrigen,marcaAut,modeloAut,edicionAut,categoriaAut, colorAut,transmisionAut,
               frenosAut,bolsasAireAut,seguroDelAut,precioDelAut):
    
    auto.marca=marcaAut
    auto.origen=paisOrigen
    auto.modelo=modeloAut
    auto.categoria=categoriaAut
    auto.edicion=edicionAut
    auto.color=colorAut
    auto.transmision=transmisionAut
    auto.tipoFrenos=frenosAut
    auto.bolsasDeAire=bolsasAireAut
    auto.seguro=seguroDelAut
    auto.precioCompra=precioDelAut
    auto.precioVenta=auto.multiplicadorVenta()*auto.precioCompra
    
def obtenerDatos(auto):
    print("********* Ingresar Datos *************")
    while True:
        paisOrigen =  input("Origen (L: Local/ I:Importado): ").lower()
        if paisOrigen =="l":
            paisOrigen ="Local"
            break
        elif paisOrigen =="i":
            paisOrigen = "Importado"
            break
        else:
            print("Respuesta inválida, ingrese L o I")    
    marcaAut = input("Marca: ")
    modeloAut = input("Modelo: ")
    categoriaAut =input("Categoría del Vehículo (Camineta, Pick up, sedán, etc): ")
    edicionAut = input(f"Edición del Modelo {modeloAut}: " )
    colorAut = input("Color: ")
    transmisionAut = input("Transmisión del Vehículo: ")
    frenosAut = input("Tipo de frenos: ")
    bolsasAireAut = input("Número de Bolsas de Aire: ")
    while True:
            seguroDelAut = (input("Estado del seguro (1:Activo / 0:Inactivo): "))
            if seguroDelAut == "1":
                seguroDelAut = True
                break
            elif seguroDelAut == "0":
                seguroDelAut = False
                break
            else:
                print("Opción inválida, ingrese 1 o 0")
                
    precioDelAut = float(input("Ingrese el precio de compra: $"))
    
    pasarDatos(auto,paisOrigen,marcaAut,modeloAut,edicionAut,categoriaAut, colorAut,transmisionAut,
               frenosAut,bolsasAireAut,seguroDelAut,precioDelAut)

def mostrarDatos(vehiculo):
    print("~~~~~~~~~~  DATOS DEL AUTOMOVIL  ~~~~~~~~~~")
    print(f"- Origen: {vehiculo.origen}")
    print(f"- Marca: {vehiculo.marca}")
    print(f"- Modelo: {vehiculo.modelo}")
    print(f"- Categoría: {vehiculo.categoria}")
    print(f"- Capacidad: {vehiculo.capacidad()} pasajeros")
    print(f"- Numero de Ruedas: {vehiculo.ruedas()}")
    print(f"- Transmisión: {vehiculo.transmision}")
    print(f"- Edicion: {vehiculo.edicion}")
    print(f"- Color: {vehiculo.color}")
    print(f"- Tipo de frenos: {vehiculo.tipoFrenos}")
    print(f"- Bolsas de aire: {vehiculo.bolsasDeAire}")
    print(f"- Estado del Seguro: {vehiculo.seguro}")
    print(f"- Precio al Público: ${vehiculo.precioVenta}")
    print("""
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░▒▒▓████████▓▓▓▒░░░░
░░░░░░░░▒▓█████████████████▓░░
░░▒▒▓▓███████████████████████▒
▒████████████████████████████▓
████▓▓█▓▓██████████████▓██▓███
███▓█████▓████████████▓████▓▓▒
░░░░▓███▒░░░░░░░░░░░░░░▓██▓░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
""")
    

carro1=auto()
obtenerDatos(carro1)
mostrarDatos(carro1)