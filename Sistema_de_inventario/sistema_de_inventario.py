class Producto:

    def __init__(self,nombre,cantidad,precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

def mostrar_menu():
    print("Sistema de inventario")
    print("1. Agregar producto")
    print("2. Mostrar producto")
    print("3. Buscar producto")
    print("4. Actualizar cantidad")
    print("5. Eliminar producto")
    print("6. Salir")

inventario = []

while True:
    mostrar_menu
    opcion = input("Elige una opción: ")
    if opcion == "6":
        print("Saliendo del programa")
        break

    if opcion == "1":
        nombre = input("Ingrese el nombre del producto: ")
        try:
            cantidad = int(input("ingrese la cantidad"))
            precio = float(input("Ingrese el precio"))
            producto = Producto(nombre, cantidad, precio)
            inventario.append(producto)
            print("Producto agregado")
        except ValueError:
            print("Error: Entrada no válida")
    
    elif opcion == "2":
        for p in inventario:
            print(f"Nombre:{p.nombre}, Cantidad:{p.cantidad}, Precio:{p.precio}")
    
    elif opcion == "3":
        nombre = input("Ingrese el nombre del producto a buscar: ")
        encontrado = False
        for p in inventario:
            if p.nombre == nombre:
                print(f"Nombre:{p.nombre}, Cantidad:{p.cantidad}, Precio:{p.precio}")
                encontrado = True
                break
            if not encontrado:
                print("Producto no encontrado")
    
    elif opcion == "4":
        nombre = input("Ingrese el nombre del producto a actualizar: ")
        try:
            nueva_cantidad = int(input("Ingrese la nueva cantidad"))
            for p in inventario:
                if p.nombre == nombre:
                    p.cantidad == nueva_cantidad
                    print("Cantidad actualizada")
                    break
        except ValueError:
            print("Error: Entrada no encontrada")

    elif opcion == "5":
        nombre = input("Ingrese el nombre del producto a eliminar: ")
        for p in inventario:
            if p.nombre == nombre:
                inventario.remove(p)
                print("Producto eliminado.")
                break
        
    else: 
        print("Opcion no válida")