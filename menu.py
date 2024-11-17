import subprocess

def menu():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Jugar trivia (Python - Entregable 1)")
        print("2. Procesar pedidos (Java - Entregable 2)")
        print("3. Realizar consultas en USQL (Python - Entregable 3)")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            print("\nEjecutando Trivia...")
            subprocess.run(["python", "Entregable1\main.py"]) 
        elif opcion == '2':
            print("\nProcesando Pedidos...") 
            subprocess.run(["java", "-jar", "TestApp.jar"])  
        elif opcion == '3':
            print("\nRealizando Consultas en USQL...")
            subprocess.run(["python", "Entregable3\API.py"])  
        elif opcion == '4':
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
