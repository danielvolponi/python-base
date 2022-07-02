#!/usr/bin/env python3

def soma(a, b):
    return a + b

soma(1,3)
soma(1, b=3)

def hello(nome, sobrenome="Sabugosa"):
    print(f"Hello {nome}, {sobrenome}")

hello("Bruno", "Rocha")
hello("Bruno", sobrenome="Rocha")
hello(sobrenome="Rocha", nome="Bruno")
hello( nome="Bruno")

def funcao(*args, timeout=10, **kwargs):
    for item in args:
        print(args)

    print(f"timeout: {timeout}")
    print(kwargs)

funcao(
    "Bruno",
     1,
     True,
     [],
     nome="João", 
     cidade="Viana", 
     teclado = True,
     timeout=90
 )
