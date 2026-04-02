   # Lista de tareas
tareas = ["acomodar","lavar","ir al gmy","cocinar","limpiar"]

def mostrar_tareas():
    if len(tareas) == 0:
        print("No hay tareas.")
    else:
        print("\nTareas:")
        for i, tarea in enumerate(tareas, 1):
            print(f"{i}. {tarea}")

def agregar_tarea():
    tarea = input("Escribe la tarea: ")
    tareas.append(tarea)
    print("Tarea agregada.")

def eliminar_tarea():
    mostrar_tareas()
    num = int(input("Número de tarea a eliminar: "))
    if 1 <= num <= len(tareas):
        tareas.pop(num - 1)
        print("Tarea eliminada.")
    else:
        print("Número inválido.")

while True:
    print("\n--- MENÚ ---")
    print("1. Ver tareas")
    print("2. Agregar tarea")
    print("3. Eliminar tarea")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        mostrar_tareas()
    elif opcion == "2":
        agregar_tarea()
    elif opcion == "3":
        eliminar_tarea()
    elif opcion == "4":
        print("Adiós")
        break
    else:
        print("Opción inválida")
