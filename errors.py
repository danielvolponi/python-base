#!/usr/bin/env python3
"""Errors

Programa que imprime na tela a posicao 1 da lista de nomes

"""
import os
import sys

# EAFP - Easy to Ask Forgiveness than permission
# (É mais fácil pedir perdão do que permissão)

try:
    raise RuntimeError("Ocorreu um erro")
except Exception as e:
    print(str(e)) 


try:
    names  = open("names.txt").readlines()
except FileNotFoundError as e:
    print(f"{str(e)}")
    sys.exit(1)
    # TODO: Usar retry
else: 
    print("Sucesso") # Somente se o try funcionar
finally:
    print("Execute isso sempre!") 


try:
    print(names[2])
except:
    print("[Error] Missing name in the list")
    sys.exit(1)
