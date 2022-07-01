#!/usr/bin/env python3
# aqui começa o escopo global
nome = "Global"
numero = 1
flag = True

def funcao():
    # Aqui começa o escopo local 
    nome = "Local"

    def funcao_interna(): # inner function
        # closure
        # aqui comeca o escopo local da funcao interna
        nome = "Interna"
        # print("Escopo local da função interna: ", locals())
        # print("=" * 30)
        print(nome)
        return nome
    # print("Escopo local da função: ", locals())
    # print("=" * 30)
    funcao_interna()
    print(nome)
    return nome
    # aqui termina o escopo local

# print("Escopo global do programa", globals())

# print("-" * 30)
funcao()
print(nome)

# aqui termina o escopo global
