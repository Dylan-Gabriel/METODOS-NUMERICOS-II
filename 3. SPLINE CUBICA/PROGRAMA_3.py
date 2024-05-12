print("\n\nDesarrolladores: \n\t -Albor Saucedo Dylan Gabriel. \n\t -Zavala Minor Leonardo. \n\t -Flores López Braulio Jesus. \n\t -Ramírez Maza Luis Alfredo.\n")

# Función para capturar los valores de x y f(x) para cada punto de la tabla
def capturar_tabla(num_puntos):
    tabla = []  # Inicializa una lista vacía llamada tabla
    for i in range(num_puntos):
        x = float(input(f"Ingrese el valor de x_{i}: "))  # Solicita al usuario el valor de x para el punto i
        fx = float(input(f"Ingrese el valor de f(x)_{i}: "))  # Solicita al usuario el valor de f(x) para el punto i
        tabla.append((x, fx))  # Agrega una tupla que contiene los valores de x y fx a la lista tabla
    return tabla  # Devuelve la lista tabla una vez que ha sido construida y completada con los pares de valores de x y f(x) ingresados por el usuario.

# Función para mostrar la tabla de valores
def mostrar_tabla(tabla):
    print("Tabla de valores:")  # Imprime el encabezado de la tabla
    print("x\t\tf(x)")  # Imprime las etiquetas de las columnas
    for x, fx in tabla:
        print(f"{x}\t\t{fx}")  # Imprime los valores de x y fx en formato de tabla

# Función para corregir puntos de la tabla
def corregir_tabla(tabla):
    while True:
        mostrar_tabla(tabla)  # Muestra la tabla actual
        respuesta = input("¿Desea corregir algún punto de la tabla? (si/no): ").lower()  # Pregunta al usuario si desea corregir algún punto
        if respuesta != 'si':
            break
        num_punto = int(input("Indique el número del punto que desea corregir (0 al número total de puntos x_i): "))  # Solicita al usuario el número del punto a corregir
        if num_punto < 0 or num_punto >= len(tabla):
            print("Número de punto inválido.")  # Verifica si el número de punto es válido
            continue
        nuevo_x = float(input(f"Ingrese el nuevo valor de x_{num_punto}: "))  # Solicita al usuario el nuevo valor de x
        nuevo_y = float(input(f"Ingrese el nuevo valor de f(x)_{num_punto}: "))  # Solicita al usuario el nuevo valor de f(x)
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

    print("Tabla de Spline Cúbico")  # Imprime el encabezado de la tabla
    print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format("i", "xi", "yi", "ci", "bi", "ai", "hi", "Diferencias Divididas"))  # Imprime las etiquetas de las columnas

    # Imprime los valores de la tabla en formato de tabla
    for i in range(n-1):
        # Imprime los valores de la tabla del spline cúbico en un formato tabular con un ancho fijo para cada columna.
        print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(i, round(x[i], 3), round(a[i], 3), round(b[i], 3), round(c[i], 3), round(d[i], 3), round(h[i], 3), round(diferencias_divididas[i], 3)))

# Función para mostrar los polinomios cúbicos
def mostrar_polinomios_cubicos(x, a, b, c, d):
    n = len(x)  # Obtiene el número de puntos en la tabla

    print("Polinomios Cúbicos:")  # Imprime el encabezado

    # Itera sobre los intervalos y muestra el polinomio cúbico correspondiente a cada intervalo
    for i in range(n - 1):
        intervalo = f"({x[i]}, {x[i+1]})"  # Define el intervalo
        polinomio = f"P_{i}(x) = {a[i]} + {b[i]}(x - {x[i]}) + {c[i]}(x - {x[i]})^2 + {d[i]}(x - {x[i]})^3"  # Define el polinomio
        print(f"Intervalo {intervalo}: {polinomio}")  # Muestra el polinomio para el intervalo correspondiente

# Función principal del programa
def main():
     while True:
        num_puntos = int(input("Ingrese el número de puntos en la tabla: "))  # Solicita al usuario el número de puntos en la tabla
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
        respuesta = input("¿Desea realizar otro ajuste con otra tabla de valores? (si/no): ").lower()
        if respuesta != 'si':
            break

# Verifica si este script es el programa principal que se está ejecutando
if __name__ == "__main__":
    main()  # Llama a la función principal del programa
