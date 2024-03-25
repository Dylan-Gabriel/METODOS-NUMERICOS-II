import numpy as np

def leer_tabla():
    while True:
        try:
            num_puntos = int(input("Ingrese el número de puntos en la tabla: "))
            break
        except ValueError:
            print("Por favor, ingrese un número válido.")

    tabla = []
    for i in range(num_puntos):
        punto = input(f"Ingrese el punto {i+1} en el formato xi yi separado por espacio: ").split()
        tabla.append((float(punto[0]), float(punto[1])))

    print("\nTabla de valores ingresada:")
    print("xi\t\tyi")
    for xi, yi in tabla:
        print(f"{xi}\t\t{yi}")

    return sorted(tabla, key=lambda x: x[0])  # Ordenar la tabla por xi

def verificar_datos(tabla):
    while True:
        respuesta = input("¿Los datos son correctos? (Sí/No): ").lower()
        if respuesta == 'no':
            fila_corregir = int(input("Ingrese el número de fila a corregir: ")) - 1
            nuevo_valor = input("Ingrese el nuevo valor en el formato xi yi separado por espacio: ").split()
            tabla[fila_corregir] = (float(nuevo_valor[0]), float(nuevo_valor[1]))
            print("\nTabla de valores corregida:")
            print("xi\t\tyi")
            for xi, yi in tabla:
                print(f"{xi}\t\t{yi}")
        elif respuesta == 'sí' or respuesta == 'si':
            return tabla
        else:
            print("Por favor, responda 'Sí' o 'No'.")

def leer_punto_interpolacion(tabla):
    while True:
        punto_interpolacion = float(input("Ingrese el punto a interpolar: "))
        if tabla[0][0] <= punto_interpolacion <= tabla[-1][0]:
            return punto_interpolacion
        else:
            print("El punto a interpolar debe estar dentro del rango de la tabla.")

def leer_grado_polinomio(tabla):
    while True:
        grado = int(input("Ingrese el grado del polinomio: "))
        if grado <= len(tabla) - 1:
            return grado
        else:
            print("No hay suficientes puntos en la tabla para el grado del polinomio especificado.")

def diferencias_divididas(tabla):
    n = len(tabla)
    matriz_diferencias = np.zeros((n, n+1))

    for i in range(n):
        matriz_diferencias[i, 0] = tabla[i][0]
        matriz_diferencias[i, 1] = tabla[i][1]

    for j in range(2, n+1):
        for i in range(n-j+1):
            matriz_diferencias[i, j] = (matriz_diferencias[i+1, j-1] - matriz_diferencias[i, j-1]) / (matriz_diferencias[i+j-1, 0] - matriz_diferencias[i, 0])

    return matriz_diferencias

def evaluar_polinomio(tabla, matriz_diferencias, punto_interpolacion):
    n = len(tabla)
    resultado = matriz_diferencias[0, 1]  # Primer término del polinomio
    x = np.array([fila[0] for fila in tabla])  # Valores xi de la tabla
    for i in range(1, n):
        termino = matriz_diferencias[0, i+1]
        for j in range(i):
            termino *= (punto_interpolacion - x[j])
        resultado += termino
    return resultado



def mostrar_tabla_diferencias(matriz_diferencias):
    print("\nTabla de diferencias divididas:")
    n = len(matriz_diferencias)
    for i in range(n):
        for j in range(n+1):
            print(f"{matriz_diferencias[i, j]:.4f}", end="\t")
        print()

def main():
    print("Interpolación Polinomial")

    while True:
        tabla = leer_tabla()
        tabla = verificar_datos(tabla)
        punto_interpolacion = leer_punto_interpolacion(tabla)
        grado = leer_grado_polinomio(tabla)

        matriz_diferencias = diferencias_divididas(tabla)
        mostrar_tabla_diferencias(matriz_diferencias)

        resultado = evaluar_polinomio(tabla, matriz_diferencias, punto_interpolacion)
        print(f"\nEl resultado de la interpolación en el punto {punto_interpolacion} es: {resultado: .5f}")

        continuar = input("¿Desea interpolar otro punto con la misma tabla? (Sí/No): ").lower()
        if continuar != 'sí' and continuar != 'si':
            cambiar_tabla = input("¿Desea cambiar la tabla? (Sí/No): ").lower()
            if cambiar_tabla == 'sí' or cambiar_tabla == 'si':
                continue
            else:
                break

if __name__ == "__main__":
    main()
