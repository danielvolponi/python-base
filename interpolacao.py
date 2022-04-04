#!/usr/bin/env python3

email_tmpl = """
Olá, %(nome)s 
 
Tem interesse em comprar %(produto)s?
Este produto é ótimo para resolver
%(texto)s
  
Clique agora em %(links)s
  
Apenas %(quantidade)d disponiveis!

Preço promocional %(preco).2f

"""

clientes = ["Maria", "Joao", "Bruno"]

for cliente in clientes:
    print(email_tmpl % ({
        "nome": cliente,
        "produto": "caneta", 
        "texto": "Escrever muito bem", 
        "links": "canetaslegais.com", 
        "quantidade": 1, 
        "preco": 50.0}))
