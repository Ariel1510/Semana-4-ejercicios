#Mi ejercicio consistirá en el siguiente caso, una pupuseria local se ha vuelto muy reconocida y ha adquirido mucha más clientela 
#en los últimos meses, por lo cual para agilizar la atención al cliente requieren de un sistema que les de las cuentas de los clientes
#en base a lo que ellos han pedido, en este ejercicio solo usaré la opción de las pupusas pero claro que se puede integrar cosas como
#la bebida o algún postre.

class pupusa():
    saborPupusa = ""
    cantidad = ""
    masa = ""
    salsa = ""
    repollo = ""
    precioVenta = 0
    multiplicador = 0


def pasarDatos(pupusa, saborPp, cantidadPp, masaPp, salsaPp, repolloPp, multipPp):
    pupusa.saborPupusa = saborPp
    pupusa.cantidad = cantidadPp
    pupusa.masa = masaPp
    pupusa.salsa = salsaPp
    pupusa.repollo = repolloPp
    pupusa.multiplicador = multipPp
    pupusa.precioVenta = multipPp * cantidadPp

def getDatos(pupusa):
    print("~~~~~~~~~~  INGRESE LA ORDEN  ~~~~~~~~~~")
    
    saborPp = input("Ingrese el sabor de la pupusa: ")
    masaPp = input("Ingrese el tipo de masa(maiz/arroz): ")
    cantidadPp = int(input("Ingrese la cantidad de pupusas: "))
    if saborPp == "Loca":
        multipPp = 1.25
    else:
        multipPp = 0.75

    salsaPp = input("Ingrese la salsa que acompañe la orden:")    
    repolloPp = input("Ingrese el tipo de repollo: ") 

    pasarDatos(pupusa, saborPp, cantidadPp, masaPp, salsaPp, repolloPp, multipPp)   

def showDatos(pupusa):
    print("~~~~~~~~~~  ORDEN DE PUPUSAS  ~~~~~~~~~~")
    print(f"Sabor de la/las pupusas: {pupusa.saborPupusa}\n"
          f"Tipo de masa: {pupusa.masa}\n"
          f"Cantidad: {pupusa.cantidad}\n"
          f"salsa de las pupusas: {pupusa.salsa}\n"
          f"Repollo de las pupusas: {pupusa.repollo}\n"
          f"COSTO TOTAL: {pupusa.precioVenta}")
    
#ARRANCAR EL PROGRAMA
print("-------------------------")
print("Bienvenido al sistema PUPUSERIA")
print("-------------------------")

while True:
    print("Escoja una Opción")
    opt= input("1. Entrar al sistema / 2. Cerrar el programa ")

    match opt:
        case "1":
            orden1 = pupusa()
            getDatos(orden1)
            showDatos(orden1)
    
        case "2":
                break
    
    opt= input("Desea continuar el programa? (S/N)").upper()
    if opt!="S":
        break