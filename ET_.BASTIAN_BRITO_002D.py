productos = {"modelo":   
["marca", "pantalla", "RAM", "disco", "GB de DD", "procesador", "video"]}
 
productos = {
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'], 
    '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'], 
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'], 
    'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'], 
    'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'], 
    '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'], 
    '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'], 
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'], 
}

stock = {
    '8475HD': [387990,10],
    '2175HD': [327990,4], 
    'JjfFHD': [424990,1],
    'fgdxFHD': [664990,21],
    '123FHD': [290890,32], 
    '342FHD': [444990,7],
    'GF75HD': [749990,2], 
    'UWU131HD': [349990,1], 
    'FS1230HD': [249990,0],
}
### opcion 1
def stock_marca(marca):
    for marca in productos:
        pas = marca[0]
        if pas in stock:
            cantidad += stock[pas][1]
        else:
            print("La marca no existe")

### Opcion 2
def búsqueda_precio(p_min,p_max):
    for i in stock:
        stock[modelo]
        if i in stock[modelo[i][1]]:
            print(i)
        
        
### opcion 3
def actualizar_precio(modelo, p):
    while True:
        if modelo in stock:
            stock[modelo][0] = p    
            return True
        else:
            return False
        
while True:
    print("""*** MENU PRINCIPAL ***
    1. Stock marca.
    2. Búsqueda por precio.
    3. Actualizar precio.
    4. Salir.""")
    opc = input("Ingrese opción: ")
    match opc:
        case "1":
            marca = input("Ingrese marca a consultar: ")
            stock_marca(marca)
            cantidad = stock_marca(marca)
            print(f"El stock es: {cantidad}")
        case "2":
            p_min = input("Ingrese precio mínimo: ")
            p_max = input("Ingrese precio máximo:")
            búsqueda_precio(p_min,p_max)
        
        case "3":
            try:
                modelo = input("Ingrese modelo a actualizar:")
                p = int(input("Ingrese precio nuevo:"))
                verificacion = actualizar_precio(modelo,p)
                if verificacion == True:
                    print("Precio actualizado!!")
                else:
                    print("El modelo no existe!!")
            except Exception:
                print("Ingrese Datos correctos")
        
        case "4":
            print("Programa finalizado.")
            break
        case _:
            print("Debe seleccionar una opción válida!!")