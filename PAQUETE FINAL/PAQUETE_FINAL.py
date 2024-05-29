import numpy as np
import os
import math

# Función para mostrar la portada
def mostrar_portada():
    print("\n\n\n Bienvenido al Paquete Final de Metodos Numericos II.")
    print("\n Desarrollado por:")
    print("\t -Albor Saucedo Dylan Gabriel. \n\t -Flores Lopez Braulio Jesus. \n\t -Ramírez Maza Luis Alfredo. \n\t -Zavala Minor Leonardo.")  # Coloca aquí el nombre del desarrollador principal

# Función para mostrar el menú principal
def mostrar_menu():
    print("\n Menú Principal:")
    print("\t1. Sistemas de ecuaciones no lineales (Broyden).")
    print("\t2. Interpolación y ajuste de curvas.")
    print("\t3. Diferenciación e integración (datos equidistantes).")
    print("\t4. Salir")

# Función para la opción 1
def opcion1():
    print("\n\tHas seleccionado el tema de Sistemas de ecuaciones no lineales (Broyden).\n\n")
    # Aquí puedes colocar el código para la opción 1

    # Definición de las funciones de los sistemas de ecuaciones
    def sistema_1(x):
        f1 = x[0]**2 + x[0]*x[1] - 10
        f2 = x[1] + 3*x[0]*x[1]**2 - 50
        return np.array([f1, f2])

    def sistema_2(x):
        f1 = x[0]**2 + x[1]**2 - 9
        f2 = -np.exp(x[0]) - 2*x[1] - 3
        return np.array([f1, f2])

    def sistema_3(x):
        x, y, z = x
        f1 = 2*x**2 - 4*x + y**2 + 3*z**2 + 6*z + 2
        f2 = x**2 + y**2 - 2*y + 2*z**2 - 5
        f3 = 3*x**2 - 12*x + y**2 - 3*z**2 + 8
        return np.array([f1, f2, f3])

    def sistema_4(x):
        x, y, z = x
        f1 = x**2 - 4*x + y**2
        f2 = x**2 - x - 12*y + 1
        f3 = 3*x**2 - 12*x + y**2 - 3*z**2 + 8
        return np.array([f1, f2, f3])

    # Función para mostrar los sistemas de ecuaciones
    def mostrar_sistemas():
        print("Sistema de ecuaciones 1:")
        print("f1(x, y) = x^2 + xy - 10 = 0")
        print("f2(x, y) = y + 3xy^2 - 50 = 0")

        print("\nSistema de ecuaciones 2:")
        print("f1(x, y) = x^2 + y^2 - 9 = 0")
        print("f2(x, y) = -e^x - 2y - 3 = 0")

        print("\nSistema de ecuaciones 3:")
        print("f1(x, y, z) = 2x^2 - 4x + y^2 + 3z^2 + 6z + 2 = 0")
        print("f2(x, y, z) = x^2 + y^2 - 2y + 2z^2 - 5 = 0")
        print("f3(x, y, z) = 3x^2 - 12x + y^2 - 3z^2 + 8 = 0")

        print("\nSistema de ecuaciones 4:")
        print("f1(x, y, z) = x^2 - 4x + y^2 = 0")
        print("f2(x, y, z) = x^2 - x - 12y + 1 = 0")
        print("f3(x, y, z) = 3x^2 - 12x + y^2 - 3z^2 + 8 = 0")
    
        # Esperar a que el usuario presione Enter antes de continuar
        input("\n\tPresiona Enter para continuar...")

    # Función para resolver los sistemas de ecuaciones utilizando el método de Broyden
    def resolver_sistema(sistema_func):
        valor_inicial = np.array([0, 0, 0]) if sistema_func in [sistema_3, sistema_4] else np.array([0, 0])  # Valores iniciales

        print("\nIngrese los valores iniciales:")
        if sistema_func in [sistema_3, sistema_4]:
            x = float(input("x: "))
            y = float(input("y: "))
            z = float(input("z: "))
            valor_inicial = np.array([x, y, z])
        else:
            x = float(input("x: "))
            y = float(input("y: "))
            valor_inicial = np.array([x, y])

        tolerancia = float(input("Ingrese la tolerancia deseada: "))
        iteraciones_max = int(input("Ingrese la cantidad máxima de iteraciones: "))

        # Resolución del sistema de ecuaciones utilizando el método de Broyden
        x_k = valor_inicial
        for k in range(iteraciones_max):
            Fk = sistema_func(x_k)
            Jk = np.zeros((len(x_k), len(x_k)))
            h = 1e-6
            for i in range(len(x_k)):
                x_k_h = x_k.copy()
                x_k_h[i] += h
                Jk[:, i] = (sistema_func(x_k_h) - Fk) / h

            dk = np.linalg.solve(Jk, -Fk)  # Dirección de búsqueda
            x_k1 = x_k + dk

            # Imprimir información de la iteración
            print("\nIteración:", k + 1)
            print("Aproximación:", x_k1)
            print("Matriz Jacobiana:")
            print(Jk)

            # Comprobación de convergencia
            if np.linalg.norm(x_k1 - x_k) < tolerancia:
                print("\nConvergencia alcanzada con una tolerancia de", tolerancia)
                print("\nRaíz del sistema encontrada:", x_k1)
            # Esperar a que el usuario presione Enter antes de continuar
                input("Presiona Enter para continuar...")           
                return
            
            x_k = x_k1
        # Si se alcanza el máximo de iteraciones sin convergencia
        print("\nNo se logró converger después de", iteraciones_max, "iteraciones.")
        
        # Esperar a que el usuario presione Enter antes de continuar
        input("\nPresiona Enter para continuar...")

    # Función principal
    def main():

        while True:
            print(" Menú de sistemas de ecuaciones:")
            print("\t1. Mostrar sistemas de ecuaciones.")
            print("\t2. Resolver sistema de ecuaciones 1.")
            print("\t3. Resolver sistema de ecuaciones 2.")
            print("\t4. Resolver sistema de ecuaciones 3.")
            print("\t5. Resolver sistema de ecuaciones 4.")
            print("\t6. Salir.\n")

            option = input("Seleccione una opción: ")

            if option == '1':
                mostrar_sistemas()
            elif option == '2':
                resolver_sistema(sistema_1)
            elif option == '3':
                resolver_sistema(sistema_2)
            elif option == '4':
                resolver_sistema(sistema_3)
            elif option == '5':
                resolver_sistema(sistema_4)
            elif option == '6':
                print("\n\tSaliendo al menú...\n\n")
                break
            else:
                print("Opción no válida. Por favor, seleccione nuevamente.")

    if __name__ == "__main__":
        main()

# Función para la opción 2
def opcion2():
    print("\n\n\tHas seleccionado el tema de Interpolación y ajuste de curvas.\n\n")
    # Aquí puedes colocar el código para la opción 2
    while True:
        print(" Submenú:\n")
        print("\t 2.1 Interpolación.")
        print("\t 2.2 Ajuste de curvas.")
        print("\t 3 Volver al Menú Principal.")
        opcion = input("\n\t\tSelecciona una opción: ")
        
        if opcion == "2.1":
            print("\n\n\tHas seleccionado el tema de Interpolación.\n\n")
            # Código para la Opción A
            def leer_tabla():
                # Función para leer la tabla de valores xi, yi
                while True:
                    try:
                        num_puntos = int(input("\n\tIngrese el número de puntos en la tabla: "))  # Solicitar al usuario el número de puntos
                        break
                    except ValueError:
                        print("\n\tPor favor, ingrese un número válido.\n\t")  # Manejar excepción si se ingresa un valor no válido

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
                print("\n INTERPOLACIÓN POLINOMIAL.")
                print("\n Seleccione una opción:")
                print("\t1. Iniciar programa.")
                print("\t2. Salir.")

            def pausa():
                # Función para pausar la ejecución hasta que el usuario presione Enter
                input("\n\tPresione Enter para continuar...\n\n")

            def main():
                # Función principal del programa
                mostrar_portada()  # Mostrar la portada al inicio del programa
                opcion = input("\n\tIngrese su opción: ")

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
                            print("\n\t\t¡Hasta luego!\n\n")
                        else:
                            print("\n\t\tOpción no válida. Por favor, seleccione una opción válida.\n\n")

            if __name__ == "__main__":
                main()  # Ejecutar la función principal del programa
        elif opcion == "2.2":
            print("\n\tHas seleccionado el tema de Ajuste de curvas\n\n")
            # Código para la Opción B

            # Función para capturar los valores de x y f(x) para cada punto de la tabla
            def capturar_tabla(num_puntos):
                tabla = []  # Inicializa una lista vacía llamada tabla
                for i in range(num_puntos):
                    x = float(input(f" Ingrese el valor de x_{i}: "))  # Solicita al usuario el valor de x para el punto i
                    fx = float(input(f" Ingrese el valor de f(x)_{i}: "))  # Solicita al usuario el valor de f(x) para el punto i
                    tabla.append((x, fx))  # Agrega una tupla que contiene los valores de x y fx a la lista tabla
                return tabla  # Devuelve la lista tabla una vez que ha sido construida y completada con los pares de valores de x y f(x) ingresados por el usuario.

            # Función para mostrar la tabla de valores
            def mostrar_tabla(tabla):
                print(" Tabla de valores:")  # Imprime el encabezado de la tabla
                print(" x\t\tf(x)")  # Imprime las etiquetas de las columnas
                for x, fx in tabla:
                    print(f"{x}\t\t{fx}")  # Imprime los valores de x y fx en formato de tabla

            # Función para corregir puntos de la tabla
            def corregir_tabla(tabla):
                while True:
                    mostrar_tabla(tabla)  # Muestra la tabla actual
                    respuesta = input(" ¿Desea corregir algún punto de la tabla? (si/no): ").lower()  # Pregunta al usuario si desea corregir algún punto
                    if respuesta != 'si':
                        break
                    num_punto = int(input(" Indique el número del punto que desea corregir (0 al número total de puntos x_i): "))  # Solicita al usuario el número del punto a corregir
                    if num_punto < 0 or num_punto >= len(tabla):
                        print(" Número de punto inválido.")  # Verifica si el número de punto es válido
                        continue
                    nuevo_x = float(input(f" Ingrese el nuevo valor de x_{num_punto}: "))  # Solicita al usuario el nuevo valor de x
                    nuevo_y = float(input(f" Ingrese el nuevo valor de f(x)_{num_punto}: "))  # Solicita al usuario el nuevo valor de f(x)
                    tabla[num_punto] = (nuevo_x, nuevo_y)  # Actualiza el valor de la tabla en la posición num_punto con los nuevos valores de x y fx

            # Función para calcular las diferencias divididas
            def calculo_diferencias_divididas(xi, yi):
                n = len(xi)  # Obtiene el número de puntos en la tabla
                F = [[0] * n for _ in range(n)]  # Crea una matriz de ceros de tamaño nxn para almacenar las diferencias divididas
                # Inicializa la primera columna de la matriz F con los valores de yi
                for i in range(n):
                    F[i][0] = yi[i] 
                # Calcula las diferencias divididas utilizando el método de Newton
                for j in range(1, n):
                    for i in range(n - j):
                        F[i][j] = (F[i+1][j-1] - F[i][j-1]) / (xi[i+j] - xi[i])
                return F[0]  # Devuelve la primera fila de la matriz F, que contiene los coeficientes de Newton

            # Función para calcular los coeficientes del spline cúbico
            def spline_cubico(x, y):
                n = len(x)  # Obtiene el número de puntos en la tabla
                a = y.copy()  # Copia la lista de valores de y
                b = [0] * (n-1)  # Crea una lista de coeficientes b de longitud n-1 llena de ceros
                d = [0] * (n-1)  # Crea una lista de coeficientes d de longitud n-1 llena de ceros
                h = [x[i+1] - x[i] for i in range(n-1)]  # Calcula las diferencias entre los valores de x adyacentes
                alfa = [0] * (n-1)  # Crea una lista de valores alfa de longitud n-1 llena de ceros

                # Calcula los valores de alfa para i desde 1 hasta n-2.
                for i in range(1, n-1):
                    alfa[i] = (3/h[i])*(a[i+1]-a[i]) - (3/h[i-1])*(a[i]-a[i-1])  # Calcula los valores de alfa

                l = [0] * n  # Crea una lista de valores de l de longitud n llena de ceros
                miu = [0] * n  # Crea una lista de valores de miu de longitud n llena de ceros
                z = [0] * n  # Crea una lista de valores de z de longitud n llena de ceros
                l[0] = 1  # Asigna 1 al primer elemento de la lista l

                # Itera sobre los índices i desde 1 hasta n-2.
                for i in range(1, n-1):
                    # Calcula el valor de l para el índice i.
                    l[i]= 2*(x[i+1] - x[i-1]) - h[i-1]*miu[i-1]
                    # Calcula el valor de miu para el índice i.
                    miu[i] = h[i]/l[i]
                    # Calcula el valor de z para el índice i.
                    z[i] = (alfa[i] - h[i-1]*z[i-1])/l[i]

                l[n-1] = 1  # Asigna 1 al último elemento de la lista l
                z[n-1] = 0  # Asigna 0 al último elemento de la lista z
                c = [0] * n  # Crea una lista de coeficientes c de longitud n llena de ceros
                b = [0] * (n-1)  # Crea una lista de coeficientes b de longitud n-1 llena de ceros
                d = [0] * (n-1)  # Crea una lista de coeficientes d de longitud n-1 llena de ceros

                # Calcula los coeficientes c, b y d.
                for j in range(n-2, -1, -1):
                    # Calcula el valor de c para el índice j.
                    c[j] = z[j] - miu[j]*c[j+1]
                    # Calcula el valor de b para el índice j.
                    b[j] = (a[j+1] - a[j])/h[j] - h[j]*(c[j+1] + 2*c[j])/3
                    # Calcula el valor de d para el índice j.
                    d[j] = (c[j+1] - c[j])/(3*h[j])

                return a, b, c, d, h  # Devuelve los coeficientes a, b, c, d y las diferencias h entre los valores de x

            # Función para mostrar la tabla del spline cúbico
            def tabla_spline_cubico(x, y, a, b, c, d, h, diferencias_divididas):
                n = len(x)  # Obtiene el número de puntos en la tabla

                print(" \n\t\tTabla de Spline Cúbico\n")  # Imprime el encabezado de la tabla
                print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format("i", "xi", "yi", "ci", "bi", "ai", "hi", "Diferencias Divididas"))  # Imprime las etiquetas de las columnas

                # Imprime los valores de la tabla en formato de tabla
                for i in range(n-1):
                    # Imprime los valores de la tabla del spline cúbico en un formato tabular con un ancho fijo para cada columna.
                    print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(i, round(x[i], 3), round(a[i], 3), round(b[i], 3), round(c[i], 3), round(d[i], 3), round(h[i], 3), round(diferencias_divididas[i], 3)))

            # Función para mostrar los polinomios cúbicos
            def mostrar_polinomios_cubicos(x, a, b, c, d):
                n = len(x)  # Obtiene el número de puntos en la tabla

                print(" Polinomios Cúbicos:")  # Imprime el encabezado

                # Itera sobre los intervalos y muestra el polinomio cúbico correspondiente a cada intervalo
                for i in range(n - 1):
                    intervalo = f"({x[i]}, {x[i+1]})"  # Define el intervalo
                    polinomio = f"P_{i}(x) = {a[i]} + {b[i]}(x - {x[i]}) + {c[i]}(x - {x[i]})^2 + {d[i]}(x - {x[i]})^3"  # Define el polinomio
                    print(f" Intervalo {intervalo}: {polinomio}")  # Muestra el polinomio para el intervalo correspondiente

            # Función principal del programa
            def main():
                while True:
                    num_puntos = int(input(" Ingrese el número de puntos en la tabla: "))  # Solicita al usuario el número de puntos en la tabla
                    tabla = capturar_tabla(num_puntos)  # Captura la tabla de valores
                    corregir_tabla(tabla)  # Permite al usuario corregir la tabla si es necesario
                    
                    x = [p[0] for p in tabla]  # Extrae los valores de x de la tabla
                    y = [p[1] for p in tabla]  # Extrae los valores de y de la tabla
                    
                    a, b, c, d, h = spline_cubico(x, y)  # Calcula los coeficientes del spline cúbico
                    diferencias_divididas = calculo_diferencias_divididas(x, y)  # Calcula las diferencias divididas
                    tabla_spline_cubico(x, y, a, b, c, d, h, diferencias_divididas)  # Muestra la tabla del spline cúbico
                    
                    # Llama a la función para mostrar los polinomios cúbicos
                    mostrar_polinomios_cubicos(x, a, b, c, d)
                    
                    # Pregunta al usuario si desea agregar más datos o salir
                    respuesta = input(" ¿Desea realizar otro ajuste con otra tabla de valores? (si/no): ").lower()
                    if respuesta != 'si':
                        break

            # Verifica si este script es el programa principal que se está ejecutando
            if __name__ == "__main__":
                main()  # Llama a la función principal del programa
        elif opcion == "3":
            break
        else:
            print("\n\t\tOpción no válida. Por favor, intenta de nuevo.\n\n")

# Función para la opción 3
def opcion3():
    print("Has seleccionado la Opción 3")
    # Aquí puedes colocar el código para la opción 3

    # Primera función
    def f1(x):
        return (x**4 * math.sqrt(3 + 2 * x**2)) / 3

    # Segunda función
    def f2(x):
        return x**5 / ((x**2 + 4)**(1/5))

    def regla_simpson(f, a, b, n):
        if n % 2 == 1:
            n += 1  # Incrementamos n para que sea par
        h = (b - a) / n
        integral = f(a) + f(b)

        for i in range(1, n, 2):
            integral += 4 * f(a + i * h)
        for i in range(2, n-1, 2):
            integral += 2 * f(a + i * h)

        integral *= h / 3
        return integral

    def regla_trapecio(f, a, b, h):
        return (h / 2) * (f(a) + f(b))

    def integrate(f, a, b, n):
        if n % 2 == 0:
            return regla_simpson(f, a, b, n)
        else:
            h = (b - a) / n
            integral_simpson = regla_simpson(f, a, b - h, n - 1)
            integral_trapezoid = regla_trapecio(f, b - h, b, h)
            return integral_simpson + integral_trapezoid

    def main():
        while True:
            print("\n DESARROLLADORES: \n\t -Albor Saucedo Dylan Gabriel. \n\t -Flores Lopez Jesus Braulio. \n\t -Ramírez Maza Luis Alfredo. \n\t -Zavala Minor Leonardo")
            print("\n Seleccione la función a integrar:")
            print("\n\t1. f(x) = (x^4 * sqrt(3 + 2 * x^2)) / 3")
            print("\t2. f(x) = x^5 / ((x^2 + 4)^(1/5))\n")
            seleccion = int(input(" Ingrese 1 o 2: "))

            if seleccion == 1:
                f = f1
            elif seleccion == 2:
                f = f2
            else:
                print("Selección no válida.")
                continue

            a = float(input("\n\tIngrese el valor del limite inferior: "))
            b = float(input("\tIngrese el valor del limite superior: "))
            n = int(input("\tIngrese el número de subintervalos n: "))

            resultado = integrate(f, a, b, n)
            print("\n\tEl valor aproximado de la integral es:", resultado)

            otra_vez = input("\n¿Quiere volver a integrar en otro intervalo o con otra n? (si/no): ").strip().lower()
            if otra_vez != 'si':
                break

    if __name__ == "__main__":
        main()

# Programa principal
mostrar_portada()  # Llama a la función mostrar_portada() al principio del programa

while True:
    mostrar_menu()  # Llama a la función mostrar_menu() dentro del bucle principal
    seleccion = input("\n Selecciona una opción: ")

    if seleccion == "1":
        opcion1()  # Llama a la función opcion1() si el usuario selecciona la opción 1
    elif seleccion == "2":
        opcion2()  # Llama a la función opcion2() si el usuario selecciona la opción 2
    elif seleccion == "3":
        opcion3()  # Llama a la función opcion3() si el usuario selecciona la opción 3
    elif seleccion == "4":
        print("\n\tGracias por usar el programa. ¡Hasta luego!\n\n")
        break  # Sale del bucle si el usuario selecciona la opción 4
    else:
        print("\n\tOpción no válida. Por favor, intenta de nuevo.\n\n")

