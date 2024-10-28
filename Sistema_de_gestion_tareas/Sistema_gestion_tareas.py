class Tarea:
    def __init__(self, titulo, descripcion, estado="pendiente"):
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = estado

    def mostrar_info(self):
        print(f"Título: {self.titulo}, Descripción: {self.descripcion}, Estado: {self.estado}")

def mostrar_menu():
    print("Sistema de gestión de tareas")
    print("1. Agregar tarea")
    print("2. Mostrar todas las tareas")
    print("3. Buscar tarea por título")
    print("4. Actualizar estado de tarea")
    print("5. Eliminar tarea")
    print("6. Salir")

tareas = []

while True:
    mostrar_menu()
    opcion = input("Elige una opción: ")
    
    if opcion == "6":
        print("Saliendo del programa")
        break

    elif opcion == "1":
        titulo = input("Ingrese el título de la tarea: ")
        descripcion = input("Ingrese la descripción de la tarea: ")
        tarea = Tarea(titulo, descripcion)
        tareas.append(tarea)
        print("Tarea agregada.")

    elif opcion == "2":
        if tareas:
            for tarea in tareas:
                tarea.mostrar_info()
        else:
            print("No hay tareas en la lista.")
    
    elif opcion == "3":
        titulo = input("Ingrese el título de la tarea a buscar: ")
        encontrada = False
        for tarea in tareas:
            if tarea.titulo.lower() == titulo.lower():
                tarea.mostrar_info()
                encontrada = True
                break
        if not encontrada:
            print("Tarea no encontrada.")
    
    elif opcion == "4":
        titulo = input("Ingrese el título de la tarea a actualizar: ")
        actualizada = False
        for tarea in tareas:
            if tarea.titulo.lower() == titulo.lower():
                tarea.estado = "completada"
                print("Estado de la tarea actualizado a 'completada'.")
                actualizada = True
                break
        if not actualizada:
            print("Tarea no encontrada.")

    elif opcion == "5":
        titulo = input("Ingrese el título de la tarea a eliminar: ")
        eliminada = False
        for i, tarea in enumerate(tareas):
            if tarea.titulo.lower() == titulo.lower():
                del tareas[i]
                print("Tarea eliminada.")
                eliminada = True
                break
            if not eliminada:
                print("Tarea no encontrada")

    else:
        print("Opción no válida. Inténtalo de nuevo.")