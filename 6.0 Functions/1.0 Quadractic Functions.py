from typing import Any


def Quad(a, b, c):
    D = (b**2) - (4 * a * c)

    if D < 0:

        return "The solution is complex"

    else:
        x1 = (-b + (D ** (1/2)))/(2 * a)

        x2 = (-b - (D ** (1/2)))/(2 * a)

        x_1 = round(x1, 1)

        x_2 = round(x2, 1)

        return x_1, x_2


x = Quad(-4, 2, -1)
print(x)