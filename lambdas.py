#!/usr/bin/env python3

def transforma_em_maiusculo(texto):
    return texto.upper()


def transforma_em_minusculo(texto):
    return texto.lower()


def divide_por_2(numero):
    return numero // 2


# e a nossa função principal
def faz_algo(valor, funcao):
    print(f"Aplicando a {funcao.__name__} em {valor}")
    return funcao(valor)


# print(faz_algo(13, divide_por_2))

names = ["Bruno", "Joao", "Bernardo", "Cintia", "Marcia", "Juca"]

# Desafio ordenar de acordo com a quantidade de i

print(sorted(names, key=lambda name: name.count("i")))

# Todos os nomes que começam com a letra B
print(list(filter(lambda name: name[0].lower() == "b", names)))

print(list(map(lambda name: "Hello " + name, names)))

# Calculadora

operacao = input("Operacao [sum, mul, div, sub]:")
n1 = float(input("n1:").strip())
n2 = float(input("n2:").strip())

operacoes = {
    "sum": lambda a, b: a + b,
    "sub": lambda a, b: a - b,
    "mul": lambda a, b: a * b,
    "div": lambda a, b: a / b,
}

resultado = operacoes[operacao](n1, n2)
print(f"O resultado é: {resultado}")
