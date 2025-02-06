def mostrar_menu():
    print("Calculadora Básica")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Suma Avanzada")
    print("6. Salir")

def ejecutar_calculadora():
    import sumar, restar, multiplicacion, dividir, suma_avanzada
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "6":
            print("Saliendo...")
            break

        if opcion in ["1", "2", "3", "4"]:
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            
            if opcion == "1":
                print("Resultado:", sumar.sumar(a, b))
            elif opcion == "2":
                print("Resultado:", restar.restar(a, b))
            elif opcion == "3":
                print("Resultado:", multiplicacion.multiplicar(a, b))
            elif opcion == "4":
                print("Resultado:", dividir.dividir(a, b))
        elif opcion == "5":
            numeros = list(map(float, input("Ingrese los números separados por espacio: ").split()))
            print("Resultado:", suma_avanzada.suma_avanzada(*numeros))
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    ejecutar_calculadora()