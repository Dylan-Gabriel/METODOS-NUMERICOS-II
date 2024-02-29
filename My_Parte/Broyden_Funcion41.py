import numpy as np

# Definición de la función F(x)
def F(x):
    f1 = x[0]**2 - 4*x[0] + x[1]**2
    f2 = x[0]**2 - x[0] - 12*x[1] + 1
    f3 = 3*x[0]**2 - 12*x[0] + x[1]**2 - 3*x[2]**2 + 8
    return np.array([f1, f2, f3])

# Función para mostrar el sistema de ecuaciones
def mostrar_sistema():
    print("Sistema de ecuaciones:")
    print("f1(x, y, z) = x^2 - 4x + y^2 = 0")
    print("f2(x, y, z) = x^2 - x - 12y + 1 = 0")
    print("f3(x, y, z) = 3x^2 - 12x + y^2 - 3z^2 + 8 = 0")

# Función para resolver el sistema de ecuaciones utilizando el método de Broyden
def resolver_sistema():
    initial_guess = np.array([0, 0, 0])  # Valores iniciales

    print("\nIngrese los valores iniciales para x, y, z:")
    x = float(input("x: "))
    y = float(input("y: "))
    z = float(input("z: "))
    initial_guess = np.array([x, y, z])

    tolerance = float(input("Ingrese la tolerancia deseada: "))

    max_iterations = int(input("Ingrese la cantidad máxima de iteraciones: "))

    # Resolución del sistema de ecuaciones utilizando el método de Broyden
    x_k = initial_guess
    for k in range(max_iterations):
        Fk = F(x_k)
        Jk = np.array([[2 * x_k[0] - 4, 2 * x_k[1], 0],
                       [2 * x_k[0] - 1, -12, 0],
                       [6 * x_k[0] - 12, 2 * x_k[1], -6 * x_k[2]]])  # Jacobiana de F en x_k
        dk = np.linalg.solve(Jk, -Fk)  # Dirección de búsqueda
        x_k1 = x_k + dk
        
        # Imprimir información en forma de tabla
        print("\nIteración:", k+1)
        print("Aproximación:", x_k1)
        print("Matriz Jacobiana:")
        print(Jk)

        # Comprobación de convergencia
        if np.linalg.norm(x_k1 - x_k) < tolerance:
            print("\nConvergencia alcanzada con una tolerancia de", tolerance)
            print("\nRaíz del sistema encontrada:")
            print("x =", x_k1[0])
            print("y =", x_k1[1])
            print("z =", x_k1[2])
            return

        x_k = x_k1

    # Si se alcanza el máximo de iteraciones sin convergencia
    print("\nNo se logró converger después de", max_iterations, "iteraciones.")

# Función principal
def main():
    print("Desarrollado por: Nombre1, Nombre2, Nombre3")

    while True:
        print("\nMenú de opciones:")
        print("1. Mostrar sistema de ecuaciones")
        print("2. Resolver sistema de ecuaciones utilizando el método de Broyden")
        print("3. Salir")

        option = input("Seleccione una opción: ")

        if option == '1':
            mostrar_sistema()
        elif option == '2':
            resolver_sistema()
        elif option == '3':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione nuevamente.")

if __name__ == "__main__":
    main()
