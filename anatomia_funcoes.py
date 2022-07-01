#!/usr/bin/env python3
"""
Este modulo serve apenas para anotação
"""
# 1. definiçào ou atribuição
# 2. assinatura - tudo que estiver () até o :
# 3. Documentacao / docstring
# 4. codigo
# 5. valor de retorno

# - Parametros
# Posicional - passados em ordem
# Nominal

def nome_da_funcao(a, b, c):
    """Esta função faz algo com a, b e c.

    Use esta função quando quiser a + b + c
    quando o parametro a tiver o valor 10
    vai acontecer x.
    
    >>> nome_da_funcao(1, 2, 3)
    6
    """
    resultado = a + b + c
    return resultado

# passagem de argumentos
valor = nome_da_funcao(1, 2, 3)

# Passagem de argumentos nomeados
valor = nome_da_funcao(a=1, b=2, c=3)
valor = nome_da_funcao(c=1, b=2, a=3)
valor = nome_da_funcao(b=1, a=2, c=3)

# Passagem de argumentos mista
valor = nome_da_funcao(1, c=2,b=3)

# funcao com muitos argumentos
valor = nome_da_funcao(
    a = 1,
    c = 2,
    b = 3,
)

print(valor)

######################

def outra_funcao(a, b, c):
    """Explica o que ela faz"""
    # tupla como valor de retorno
    return a * 2, b * 2, c * 2

valor1, valor2, valor3 = outra_funcao(1, 2, 3)
print(valor1)
print(valor2)
print(valor3)

valor1, *resto = outra_funcao(1, 2, 3)
print(valor1)
print(resto)

######################

# Passagem de Argumentos com desempacotamento

def soma(n1, n2):
    """Faz a soma de dois números."""
    return n1 + n2

# normal
print(soma(10, 20))

# Argumentos em sequencia
args = (20, 30) # tupla
# print(soma(args[0], args[1]))
# * vai desempacotar de forma posicional
print(soma(*args))

# argumentos dicionario / nomeados
args = {"n2": 90, "n1": 100}
# print(soma(n1=args["n1"], n2=args["n2"]))
print(soma(**args))

lista_de_valores_para_somar = [
    {"n2": 90, "n1": 100},
    {"n2": 90, "n1": 200},
    {"n2": 9, "n1": 650},
    (5, 10),
    [8, 13]
]

for item in lista_de_valores_para_somar:
    if isinstance(item, dict):
        print(soma(**item))
    else: 
        print(soma(*item))

##############################
