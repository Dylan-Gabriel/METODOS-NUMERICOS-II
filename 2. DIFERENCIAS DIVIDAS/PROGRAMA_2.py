import numpy as np  # Importar la biblioteca numpy para cálculos numéricos
import os  # Importar el módulo os para utilizar la función pause

def leer_tabla():
    # Función para leer la tabla de valores xi, yi
    while True:
        try:
            num_puntos = int(input("Ingrese el número de puntos en la tabla: "))  # Solicitar al usuario el número de puntos
            break
        except ValueError:
            print("Por favor, ingrese un número válido.")  # Manejar excepción si se ingresa un valor no válido

    tabla = []
    for i in range(num_puntos):
        punto = input(f"Ingrese el punto {i+1} en el formato xi yi separado por espacio: ").split()  # Solicitar los puntos xi, yi
        tabla.append((float(punto[0]), float(punto[1])))  # Convertir a flotante y agregar a la tabla

    print("\nTabla de valores ingresada:")  # Imprimir la tabla ingresada por el usuario
    print("xi\t\tyi")
    for xi, yi in tabla:
        print(f"{xi}\t\t{yi}")

    return sorted(tabla, key=lambda x: x[0])  # Ordenar la tabla por xi

def verificar_datos(tabla):
    # Función para verificar si los datos son correctos
    while True:
        respuesta = input("¿Los datos son correctos? (Sí/No): ").lower()  # Solicitar confirmación al usuario
        if respuesta == 'no':
            fila_corregir = int(input("Ingrese el número de fila a corregir: ")) - 1  # Si los datos no son correctos, solicitar al usuario la fila a corregir
            nuevo_valor = input("Ingrese el nuevo valor en el formato xi yi separado por espacio: ").split()  # Solicitar el nuevo valor
            tabla[fila_corregir] = (float(nuevo_valor[0]), float(nuevo_valor[1]))  # Actualizar la tabla con el nuevo valor ingresado
            print("\nTabla de valores corregida:")  # Imprimir la tabla corregida
            print("xi\t\tyi")
            for xi, yi in tabla:
                print(f"{xi}\t\t{yi}")
        elif respuesta == 'sí' or respuesta == 'si':  # Si los datos son correctos, retornar la tabla
            return tabla
        else:
            print("Por favor, responda 'Sí' o 'No'.")  # Manejar entrada inválida

def leer_punto_interpolacion(tabla):
    # Función para leer el punto a interpolar
    while True:
        punto_interpolacion = float(input("Ingrese el punto a interpolar: "))  # Solicitar al usuario el punto a interpolar
        if tabla[0][0] <= punto_interpolacion <= tabla[-1][0]:  # Verificar que el punto esté dentro del rango de la tabla
            return punto_interpolacion
        else:
            print("El punto a interpolar debe estar dentro del rango de la tabla.")  # Manejar caso donde el punto está fuera del rango

def leer_grado_polinomio():
    # Función para leer el grado del polinomio
    while True:
        try:
            grado = int(input("Ingrese el grado del polinomio: "))  # Solicitar al usuario el grado del polinomio
            if grado >= 0:
                return grado  # Retornar el grado si es un número entero no negativo
            else:
                print("El grado del polinomio debe ser un número entero no negativo.")  # Manejar entrada inválida
        except ValueError:
            print("Por favor, ingrese un número entero válido.")  # Manejar excepción si se ingresa un valor no válido

def diferencias_divididas(tabla):
    # Función para calcular las diferencias divididas
    n = len(tabla)
    matriz_diferencias = np.zeros((n, n+1))  # Inicializar la matriz de diferencias divididas

    for i in range(n):
        matriz_diferencias[i, 0] = tabla[i][0]  # Llenar la primera columna con los valores xi de la tabla
        matriz_diferencias[i, 1] = tabla[i][1]  # Llenar la segunda columna con los valores yi de la tabla

    for j in range(2, n+1):
        for i in range(n-j+1):
            # Calcular las diferencias divididas utilizando la fórmula de Newton-Gregory
            matriz_diferencias[i, j] = (matriz_diferencias[i+1, j-1] - matriz_diferencias[i, j-1]) / (matriz_diferencias[i+j-1, 0] - matriz_diferencias[i, 0])

    return matriz_diferencias  # Retornar la matriz de diferencias divididas

def evaluar_polinomio(tabla, matriz_diferencias, punto_interpolacion, grado):
    # Función para evaluar el polinomio interpolante en el punto dado
    n = grado + 1
    resultado = 0
    for i in range(n):
        termino = matriz_diferencias[0, i+1]
        for j in range(i):
            termino *= (punto_interpolacion - tabla[j][0])
        resultado += termino
    return round(resultado, 5)  # Redondear el resultado a 5 decimales

def mostrar_tabla_diferencias(matriz_diferencias):
    # Función para mostrar la tabla de diferencias divididas
    print("\nTabla de diferencias divididas:")
    n = len(matriz_diferencias)
    for i in range(n):
        for j in range(n+1):
            print(f"{matriz_diferencias[i, j]:.4f}", end="\t")
        print()

def mostrar_portada():
    # Función para mostrar la portada con los nombres del equipo
        # Función para mostrar la portada con los nombres del equipo
    print("\nINTERPOLACIÓN POLINOMIAL")
    print("\n Desarrollado por: ")
    print("\t-Albor Saucedo Dylan Gabriel.")
    print("\t-Flores Lopez Braulio Jesus.")
    print("\t-Ramírez Maza Luis Alfredo.")
    print("\t-Zavala Minor Leonardo.\n")
    print("Seleccione una opción:")
    print("\t1. Iniciar programa")
    print("\t2. Salir")

def pausa():
    # Función para pausar la ejecución hasta que el usuario presione Enter
    input("Presione Enter para continuar...")

def main():
    # Función principal del programa
    mostrar_portada()  # Mostrar la portada al inicio del programa
    opcion = input("Ingrese su opción: ")

    if opcion == "1":
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar la pantalla
        mostrar_portada()  # Mostrar la portada nuevamente

        print("\nInterpolación Polinomial Por Diferencias Divididas.\n")
        
        while True:
            tabla = leer_tabla()  # Leer la tabla de valores xi, yi
            tabla = verificar_datos(tabla)  # Verificar si los datos son correctos
            punto_interpolacion = leer_punto_interpolacion(tabla)  # Leer el punto a interpolar
            grado = leer_grado_polinomio()  # Leer el grado del polinomio

            matriz_diferencias = diferencias_divididas(tabla)  # Calcular las diferencias divididas
            mostrar_tabla_diferencias(matriz_diferencias)  # Mostrar la tabla de diferencias divididas

            resultado = evaluar_polinomio(tabla, matriz_diferencias, punto_interpolacion, grado)  # Evaluar el polinomio interpolante
            print(f"\nEl resultado de la interpolación en el punto {punto_interpolacion} es: {resultado:.5f}")  # Mostrar el resultado

            pausa()  # Pausar la ejecución para que el usuario pueda ver los resultados

            continuar = input("¿Desea interpolar otro punto con la misma tabla? (Sí/No): ").lower()  # Preguntar al usuario si desea continuar
            if continuar != 'sí' and continuar != 'si':
                cambiar_tabla = input("¿Desea cambiar la tabla? (Sí/No): ").lower()  # Preguntar al usuario si desea cambiar la tabla
                if cambiar_tabla == 'sí' or cambiar_tabla == 'si':
                    continue  # Volver a solicitar la tabla
                else:
                    break  # Salir del programa si el usuario no desea continuar
    elif opcion == "2":
        print("¡Hasta luego!")
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()  # Ejecutar la función principal del programa
