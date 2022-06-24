#!/usr/bin/env python3
"""Exemplos de Funções"""

"""
f(x) = 5 * (x / 2)
f(10) == 25
"""

# [S]olid - Single Responsability
def f(x): # assinatura
    result = 5 * (x / 2)
    return result

def double(x):
    return x * 2

valor = f(10)    

print(f(10))
print(f(10) == 25)


####

# Procedimentos / Procedures
def print_in_upper(text):
    """Procedure with no explicit return"""
    print(text.upper())
    # implicit return None

print_in_upper("Daniel")

####

def heron(a, b, c):
    # Calcula a area de um triangulo
    perimeter = a + b + c
    s = perimeter / 2
    area = (s * (s - a) * (s - b) * (s - c)) 
    return area ** 0.5

def heron2(params):
    return heron(*params)



triangulos = [
    (3, 4, 5),
    (5, 12, 13),
    (8, 5, 17),
    (12, 35, 37),
    (3, 4, 5),
    (5, 12, 13),
    (8, 5, 17),
    (12, 35, 37)
]

# print(list((map(heron2, triangulos))))


for t in triangulos:
     area = heron2(t)
     print(f"A área do triangulo é: {area}")


###

def nome_da_funcao():
    print("Hello funcao")
    return 1

result = nome_da_funcao()
print(result)
