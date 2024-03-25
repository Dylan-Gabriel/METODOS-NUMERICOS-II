import numpy as np

# Datos de años y casos de VIH
años = np.array([2016, 2018, 2019, 2020, 2022])
casos = np.array([14.026, 17.486, 17.424, 10.327, 7.934])

def lagrange_interpolation(x, y, x_interpolate):
    n = len(x)
    if n != 3:
        raise ValueError("Este método solo funciona para un polinomio de grado 2.")
    
    result = 0.0
    for i in range(n):
        term = y[i]
        for j in range(n):
            if j != i:
                term *= (x_interpolate - x[j])/ (x[i] - x[j])
        result += term
    return result

# Estimar el número de casos para los años 2017 y 2021 con un polinomio de grado 2
casos_2017_grado2 = lagrange_interpolation(años[0:3], casos[0:3], 2017)
casos_2021_grado2 = lagrange_interpolation(años[2:4], casos[2:4], 2021)

# Imprimir resultados
print("Estimación de casos de VIH para 2017 (polinomio de grado 2):", casos_2017_grado2)
print("Estimación de casos de VIH para 2021 (polinomio de grado 2):", casos_2021_grado2)
