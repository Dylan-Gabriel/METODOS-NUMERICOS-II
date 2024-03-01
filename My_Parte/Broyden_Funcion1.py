import numpy as np

# Definición de la nueva función F(x)
def nueva_F(x):
    f1 = x[0]**2 + x[0]*x[1] - 10
    f2 = x[1] + 3*x[0]*x[1]**2 - 50
    return np.array([f1, f2])

# Función para mostrar el sistema de ecuaciones
def mostrar_nuevo_sistema():
    print("Sistema de ecuaciones:")
    print("f1(x, y) = x^2 + xy - 10 = 0")
    print("f2(x, y) = y + 3xy^2 - 50 = 0")

# Función para resolver el sistema de ecuaciones utilizando el método de Broyden
def resolver_nuevo_sistema():
    initial_guess = np.array([0, 0])  # Valores iniciales

    print("\nIngrese los valores iniciales para x, y:")
    x = float(input("x: "))
    y = float(input("y: "))
    initial_guess = np.array([x, y])

    tolerance = float(input("Ingrese la tolerancia deseada: "))

    max_iterations = int(input("Ingrese la cantidad máxima de iteraciones: "))

    # Resolución del sistema de ecuaciones utilizando el método de Broyden
    x_k = initial_guess
    for k in range(max_iterations):
        Fk = nueva_F(x_k)
        Jk = np.array([[2 * x_k[0] + x_k[1], x_k[0]],
                       [3 * x_k[1]**2, 1 + 6 * x_k[0] * x_k[1]]])  # Jacobiana de F en x_k
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
            return

        x_k = x_k1

    # Si se alcanza el máximo de iteraciones sin convergencia
    print("\nNo se logró converger después de", max_iterations, "iteraciones.")

# Función principal
def main():
    print("Desarrollado por: Nombre1, Nombre2, Nombre3")

    while True:
        print("\nMenú de opciones:")
        print("1. Mostrar sistema de ecuaciones (2x2)")
        print("2. Resolver sistema de ecuaciones (2x2) utilizando el método de Broyden")
        print("3. Salir")

        option = input("Seleccione una opción: ")

        if option == '1':
            mostrar_nuevo_sistema()
        elif option == '2':
            resolver_nuevo_sistema()
        elif option == '3':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione nuevamente.")

if __name__ == "__main__":
    main()
