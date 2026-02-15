import math

def posicion_falsa(f, a, b, eps, M):

    if f(a) * f(b) >= 0:
        print("Error: f(a) y f(b) no tienen signos opuestos")
        return

    print("\nMétodo de la Posición Falsa\n")
    print("{:<3} {:<10} {:<10} {:<12} {:<12} {:<12} {:<12}".format(
        "n", "a_n", "b_n", "f(a_n)", "f(b_n)", "x_n", "f(x_n)"
    ))
    print("-" * 85)

    # Iteración 0
    x_prev = (a * f(b) - b * f(a)) / (f(b) - f(a))
    print("{:<3} {:<10.6f} {:<10.6f} {:<12.6f} {:<12.6f} {:<12.6f} {:<12.6f}".format(
        0, a, b, f(a), f(b), x_prev, f(x_prev)
    ))

    if f(x_prev) * f(a) < 0:
        a_n, b_n = a, x_prev
    else:
        a_n, b_n = x_prev, b

    # Iteraciones
    for n in range(1, M + 1):
        x_n = (a_n * f(b_n) - b_n * f(a_n)) / (f(b_n) - f(a_n))
        error = abs((x_n - x_prev) / x_n)

        print("{:<3} {:<10.6f} {:<10.6f} {:<12.6f} {:<12.6f} {:<12.6f} {:<12.6f}".format(
            n, a_n, b_n, f(a_n), f(b_n), x_n, f(x_n)
        ))

        if error <= eps:
            print("\nÉXITO: se obtuvo una aproximación de la raíz")
            print(f"Raíz aproximada: {x_n}")
            print(f"Iteraciones: {n}")
            return

        if f(x_n) * f(a_n) < 0:
            b_n = x_n
        else:
            a_n = x_n

        x_prev = x_n

    print("\nFRACASO: no se alcanzó la precisión deseada")


# ================= PROGRAMA PRINCIPAL =================

print("MÉTODO DE LA POSICIÓN FALSA\n")

funcion = input("Ingrese la función f(x): ")
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
eps = float(input("Ingrese la tolerancia ε: "))
M = int(input("Ingrese el número máximo de iteraciones: "))

def f(x):
    return eval(funcion, {"x": x, "math": math})

posicion_falsa(f, a, b, eps, M)