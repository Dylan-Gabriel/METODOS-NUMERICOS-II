import numpy as np

# Definición de la función F(x) para el sistema de ecuaciones 2x2
def F_system2(x):
    f1 = x[0]**2 + x[0]*x[1] - 10
    f2 = x[1] + 3*x[0]*x[1]**2 - 50
    return np.array([f1, f2])

# Función para resolver el sistema de ecuaciones utilizando el método de Broyden
def resolver_sistema(F, initial_guess, tolerance, max_iterations):
    x_k = initial_guess
    for k in range(max_iterations):
        Fk = F(x_k)
        Jk = np.zeros((len(x_k), len(x_k)))
        eps = 1e-5
        for i in range(len(x_k)):
            x_k[i] += eps
            Jk[:, i] = (F(x_k) - Fk) / eps
            x_k[i] -= eps

        dk = np.linalg.solve(Jk, -Fk)  # Dirección de búsqueda
        x_k1 = x_k + dk
        
        # Imprimir información en cada iteración
        print("\nIteración:", k+1)
        print("Aproximación:", x_k1)
        print("Matriz Jacobiana:")
        print(Jk)

        # Comprobación de convergencia
        if np.linalg.norm(x_k1 - x_k) < tolerance:
            print("\nConvergencia alcanzada con una tolerancia de", tolerance)
            print("\nRaíz del sistema encontrada:")
            print(x_k1)
            return

        x_k = x_k1

    # Si se alcanza el máximo de iteraciones sin convergencia
    print("\nNo se logró converger después de", max_iterations, "iteraciones.")

# Solicitar al usuario los valores iniciales, tolerancia y cantidad máxima de iteraciones
x_init = float(input("Ingrese el valor inicial para x: "))
y_init = float(input("Ingrese el valor inicial para y: "))
initial_guess = np.array([x_init, y_init])

tolerance = float(input("Ingrese la tolerancia deseada: "))
max_iterations = int(input("Ingrese la cantidad máxima de iteraciones: "))

# Resolver el sistema de ecuaciones
resolver_sistema(F_system2, initial_guess, tolerance, max_iterations)