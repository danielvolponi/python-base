#!/usr/bin/env python3
"""Errors

Programa que imprime na tela a posicao 1 da lista de nomes

"""
import os
import sys

if os.path.exists("names.txt"):
    names  = open("names.txt").readlines()
else:
    print("[Error] File names.txt not found.")
    sys.exit(1)

# LBYL - Look Before you leap
if len(names) >=3:
    print(names[2])
else:
    print("[Error] Missing name in the list")
    sys.exit(1)
