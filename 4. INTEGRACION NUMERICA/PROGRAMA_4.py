import math

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
