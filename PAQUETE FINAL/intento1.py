import math
import os
import numpy as np

# Desarrolladores
def presentacion_desarrolladores():
    print("\nDesarrolladores:")
    print("\t-Albor Saucedo Dylan Gabriel.")
    print("\t-Flores Lopez Braulio Jesus.")
    print("\t-Ramírez Maza Luis Alfredo.")
    print("\t-Zavala Minor Leonardo.\n")

# Sistemas de ecuaciones no lineales (Broyden)
def broyden():
    # Código para el método de Broyden
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
        input("Presiona Enter para continuar...")

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
        print("\n Desarrollado por: ")
        print("\t-Albor Saucedo Dylan Gabriel.")
        print("\t-Flores Lopez Braulio Jesus.")
        print("\t-Ramírez Maza Luis Alfredo.")
        print("\t-Zavala Minor Leonardo.")

        while True:
            print("\nMenú de sistemas de ecuaciones:")
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
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Por favor, seleccione nuevamente.")

    if __name__ == "__main__":
        main()
    pass

# Interpolación y ajuste de curvas
def interpolacion_y_ajuste_de_curvas():
    while True:
        print("\n2. Interpolación y ajuste de curvas")
        print("\t2.1 Interpolación (Diferencias divididas)")
        print("\t2.2 Ajuste por mínimos cuadrados")

        opcion = input("\nIngrese su opción (2.1 o 2.2): ")

        if opcion == "2.1":
            interpolacion_diferencias_divididas()
        elif opcion == "2.2":
            ajuste_minimos_cuadrados()
        else:
            print("Opción no válida.")

        otra_vez = input("\n¿Desea realizar otra operación de interpolación o ajuste? (si/no): ").strip().lower()
        if otra_vez != 'si':
            break

# Interpolación (Diferencias divididas)
def interpolacion_diferencias_divididas():
    # Código para la interpolación usando diferencias divididas
    pass

# Ajuste por mínimos cuadrados
def ajuste_minimos_cuadrados():
    # Código para el ajuste por mínimos cuadrados
    pass

# Diferenciación e integración (datos equidistantes)
def diferenciacion_e_integracion():
    while True:
        print("\n3. Diferenciación e integración (datos equidistantes)")
        print("\t3.1 Diferenciación")
        print("\t3.2 Integración")

        opcion = input("\nIngrese su opción (3.1 o 3.2): ")

        if opcion == "3.1":
            diferenciacion()
        elif opcion == "3.2":
            integracion()
        else:
            print("Opción no válida.")

        otra_vez = input("\n¿Desea realizar otra operación de diferenciación o integración? (si/no): ").strip().lower()
        if otra_vez != 'si':
            break

# Diferenciación
def diferenciacion():
    # Código para diferenciación
    pass

# Integración
def integracion():
    # Código para integración
    pass

# Método de Broyden para sistemas de ecuaciones no lineales
def broyden():
    pass

def menu_principal():
    while True:
        print("\nMenú Principal")
        print("1. Sistemas de ecuaciones no lineales (Broyden)")
        print("2. Interpolación y ajuste de curvas")
        print("3. Diferenciación e integración (datos equidistantes)")
        print("4. Salir")

        opcion = input("\nIngrese su opción (1, 2, 3 o 4): ")

        if opcion == "1":
            broyden()
        elif opcion == "2":
            interpolacion_y_ajuste_de_curvas()
        elif opcion == "3":
            diferenciacion_e_integracion()
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    presentacion_desarrolladores()
    menu_principal()
