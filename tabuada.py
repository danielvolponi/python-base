#!/usr/bin/env python3
"""Imprime a tabuada do 1 ao 10

---Tabuada do 1---

    1 x 1 = 1
    2 x 1 = 2
    3 x 1 = 3
...
##################
---Tabuada do 2---

    2 x 1 = 2
    2 x 2 = 4
...
-------
"""
__version__ = "0.1.1"
__author__ = "Daniel"

template_base = """
---Tabuada do 2---

    {operacao}


##################
"""


#base = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros = list(range(1, 11))

# Iterables (percorriveis)

# Para cada numero em numeros
for numero in numeros:
    for outro_numero in numeros:
        n1 = numero
        n2 = outro_numero
        resultado = n1 * n2
        operacao = f"{n1} x {n2} = {resultado}"
        print(
            template_base.format(
                operacao=operacao
            )
        )
