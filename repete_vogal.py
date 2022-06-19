#!/usr/bin/env python3
"""
Faça um programa que pede ao usuário que digite uma ou mais palavras e imprime cada uma das palavras com suas vogais duplicadas.

ex:

python repete_vogal.py
'Digite uma palavra (ou enter para sair):' Python
'Digite uma palavra (ou enter para sair):' Bruno
'Digite uma palavra (ou enter para sair):' <enter>
Pythoon
Bruunoo
"""

words = []

while True:
    word = input("Digite uma palavra (ou enter para sair): ").strip()
    if not word:
        break

    final_word = ""
    vogais = "aeiouãéêóíá"

    for letter in word:
        # TODO: remover acentuação usando funcao
        if letter.lower() in vogais:
            final_word += letter * 2
        else:
            final_word += letter
        # if ternario alternativo
        # final_word += letter * 2 if letter.lower() in vogais else letter
        
    words.append(final_word)

print(*words, sep = "\n")

