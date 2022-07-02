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


print(faz_algo(13, divide_por_2))
