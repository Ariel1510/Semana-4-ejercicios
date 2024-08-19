class Almacen:
    contador_indice = 0
    def __init__(self, tipo_dispositivo, modelo, color, procesador, pantalla, cámara, precio_compra):
        self.tipo_dispositivo = tipo_dispositivo
        self.modelo = modelo
        self.color = color
        self.procesador = procesador
        self.pantalla = pantalla
        self.cámara = cámara
        self.precio_compra = float(precio_compra)
        self.marca = "PHR"
        Almacen.contador_indice += 1
        self.indice = Almacen.contador_indice
        self.precio_venta = self.calcular_precio_venta()

    def calcular_precio_venta(self):
        return self.precio_compra * 1.7
    

    def mostrar_información(self):
        print(f"\n~~~~~~~~~~ INFORMACIÓN DEL DISPOSITIVO {self.indice} ~~~~~~~~~~")
        print(f"Tipo de dispositivo: {self.tipo_dispositivo}")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Color: {self.color}")
        print(f"Procesador: {self.procesador}")
        print(f"Tipo de pantalla: {self.pantalla}")
        print(f"Calidad de cámara: {self.cámara} megapixeles")
        print(f"Precio de compra: ${self.precio_compra:.2f}")
        print(f"Precio de venta: ${self.precio_venta:.2f}")

    
def ingresar_datos():
    num_dispositivos = int(input("¿Cuántos dispositivos desea ingresar?: "))
    dispositivos = []
    for i in range(num_dispositivos):
        
        print(f"~~~~~~~~~  INGRESE LOS DATOS DEL DISPOSITIVO N°{i+1}  ~~~~~~~~~~")
        tipo_dispositivo = input("Ingrese el tipo de dispositivo (Smartphone/tablet/laptop): ")
        modelo = input("Ingrese el modelo del dispositivo: ")
        color = input("Ingrese el color del dispositivo: ")
        procesador = input("Ingrese el procesador: ")
        pantalla = input("Ingrese el tipo de pantalla: ")
        cámara = input("Ingrese la calidad de la cámara (Megapixeles): ")
        precio = input("Ingrese el precio de compra del dispositivo: ")
        dispositivo = Almacen(tipo_dispositivo, modelo, color, procesador, pantalla, cámara, precio)
        dispositivos.append(dispositivo)
    return dispositivos

def mostrar_datos(dispositivos):
    for dispositivo in dispositivos:
        dispositivo.mostrar_información()

datos = ingresar_datos()
mostrar_datos(datos)