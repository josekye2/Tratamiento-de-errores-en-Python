class Contact:

    def __init__(self,nombre,telefono):
        self.nombre = nombre
        self.telefono = telefono

def mostrar_menu():
    print("Gestion de contactos")
    print("1. Agregar contacto")
    print("2. Mostrar contacto")
    print("3. Buscar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")

contactos = []

while True:
    mostrar_menu
    opcion = input("Elige una opción")
    if opcion == "5":
        print("Saliendo del programa")
        break

    if opcion == "1":
        nombre = input("Ingrese el nombre: ")
        telefono = input("Ingrese el telefono: ")
        contacto = Contact(nombre, telefono)
        contactos.append(Contact)
        print("Contacto agregado.")
    
    elif opcion == "2":
        for c in contactos:
            print(f"Nombre: {c.nombre}, Telefono: {c.telefono}")
    
    elif opcion == "3":
        nombre = input("Ingrese el nombre a buscar: ")
        encontrado = False
        for c in contactos:
            if c.nombre == nombre:
                print(f"Nombre: {c.nombre}, Telefono: {c.telefono}")
                encontrado == True
                break
            if not encontrado:
                print("Contacto no encontrado.")
    
    elif opcion == "4":
        nombre = input("Ingrese el nombre a eliminar: ")
        for c in contactos:
            if c.nombre == nombre:
                contactos.remove(c)
                print("Contacto eliminado.")
                break
        
    else: 
        print("Opcion no válida. Intente denuevo.")