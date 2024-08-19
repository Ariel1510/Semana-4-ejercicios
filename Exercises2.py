class cuaderno():
    __marcaC=""
    hojas=0
    tHoja=""
    colorC=""
    pastaC=""
    tamañoC=""
    precioC=0
    precioVentaC=0
    __multPrecioC=0
    def __init__(self,):
        self.__marcaC="HOJITAS"
        self.__multPrecioC=1.3
    
    def marca(self):
        return self.__marcaC
    
    def multPrecio(self):
        return self.__multPrecioC
    
class lapiz():
    __marcaL=""
    cantidad=0
    tamañoL=""
    tipo=""
    material=""
    precioL=0
    precioVentaL=0
    __multPrecioL=0
    
    def __init__(self,):
        self.__marcaL="RAYAS"
        self.__multPrecioL=1.3
    
    def marcaLp(self):
        return self.__marcaL
    
    def multPrecio(self):
        return self.__multPrecioL

#Funciones de los lápices  
def pasarDatosLp(lapiz,cantidadL,tamañoL,tipoL,materialL,precioL):
    lapiz.cantidad=cantidadL
    lapiz.tamañoL=tamañoL
    lapiz.tipo=tipoL
    lapiz.material=materialL
    lapiz.precioL=precioL
    lapiz.precioVentaL= lapiz.multPrecio()*precioL
    
def obtenerDatosLp(lapiz):
    print("~~~~~ INGRESE LOS DATOS ~~~~~")

    cantidadL=int(input("Cantidad de Lápices por paquete: "))
    tamañoL=input("Tamaño de los lápices: ")
    while True:
        tipoL=input("Tipo de lápices (Colores --> C / Grafito --> G):").upper()
        if tipoL=="C":
            tipoL="Colores"
            break
        elif tipoL=="G":
            tipoL="Grafito"
            break
        else:
            print("Valor incorrecto, ingrese C o G")
    materialL=input("Material de los lápices: ")
    precioL=float(input("Precio del producto: $"))
    pasarDatosLp(lapiz,cantidadL,tamañoL,tipoL,materialL,precioL)
    
def mostrarDatosLp(lapiz):
    print(f"~~~~~ Datos Lápices ~~~~~")
    print(f"Tipo: Lapices de {lapiz.tipo}")
    print(f"Marca: {lapiz.marcaLp()}")
    print(f"Cantidad: {lapiz.cantidad}")
    print(f"Tamaño: {lapiz.tamañoL}")
    print(f"Tipo: {lapiz.tipo}")
    print(f"Material: {lapiz.material}")
    print(f"Precio Venta: ${lapiz.precioVentaL}")
    print("~~~~~ ~~~~~ ~~~~~")
    
    
#Funciones de los cuadernos 
def pasarDatosC(cuaderno,numHojas,tipoHojasC,colorC,pastaC,tamañoC,precioCompra):
    cuaderno.hojas=numHojas
    cuaderno.tHoja=tipoHojasC
    cuaderno.colorC=colorC
    cuaderno.pastaC=pastaC
    cuaderno.tamañoC=tamañoC
    cuaderno.precioC=precioCompra
    cuaderno.precioVentaC= precioCompra*cuaderno.multPrecio()

def obtenerDatosC(cuaderno):
    print("~~~~~ INGRESE LOS DATOS ~~~~~")

    while True:
        numHojas=int(input("Número de Hojas (50 / 100) "))
        if numHojas==50:
            break
        elif numHojas==100:
            break
        else: 
            print("Error, número de hojas no válido")
    tipoHojasC= input("Tipo de Hoja (Rayado, Cuadriculado, Liso): ")
    colorC= input("Color del Cuaderno: ")
    pastaC= input("Tipo de pasta (Blanda/Dura): ")
    tamañoC= input("Tamaño del Cuaderno: ")
    precioCompra= float(input("Precio de Compra: $"))
    pasarDatosC(cuaderno,numHojas,tipoHojasC,colorC,pastaC,tamañoC,precioCompra)
    
def MostrarDatosC(cuaderno):
    print("~~~~~ Datos Cuadernos ~~~~~")
    print("Tipo: Cuaderno")
    print(f"Marca: {cuaderno.marca()}")
    print(f"Numero de Hoja: {cuaderno.hojas}")
    print(f"Tipo de Hojas: {cuaderno.tHoja}")
    print(f"Color :{cuaderno.colorC}")
    print(f"Tipo de Pasta: {cuaderno.pastaC}")
    print(f"Tamaño: {cuaderno.tamañoC}")
    print(f"Precio de Venta: ${cuaderno.precioVentaC}")
    print("~~~~~ ~~~~~ ~~~~~")

#--------------------Iniciar Programa:
print("-------------------------")
print("Bienvenido al sistema INVENTARIO")
print("-------------------------")

while True:
    print("Escoja una Opción")
    opt= input("1. Ingresar Cuadernos / 2. Ingresar Lapices ")

    match opt:
        case "1":
            cuaderno1=cuaderno()
            cuaderno2=cuaderno()
            obtenerDatosC(cuaderno1)
            obtenerDatosC(cuaderno2)
            MostrarDatosC(cuaderno1)
            MostrarDatosC(cuaderno2)
    
        case "2":
                lapices1=lapiz()
                lapices2=lapiz()
                obtenerDatosLp(lapices1)
                obtenerDatosLp(lapices2)
                mostrarDatosLp(lapices1)
                mostrarDatosLp(lapices2)
    
    opt= input("Desea continuar el programa? (S/N)").upper()
    if opt!="S":
        break