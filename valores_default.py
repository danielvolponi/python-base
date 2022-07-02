#!/usr/bin/env python3
import time

def imprime_nome(nome, sobrenome="Sabugosa"):
    # escopo local {nome: ..., sobrenome: ..}
    print(f"Seu nome é {nome} {sobrenome}")


imprime_nome("Daniel", "Volponi")
imprime_nome("Linus", "Torvalds")
imprime_nome("Linus")


def conecta(host, timeout=10):
    print(f"Conectando com o {host}")
    for i in range(0, timeout + 1):
        time.sleep(1)
        print("." * i)
    print("Erro ao conectar")

conecta("localhost")
