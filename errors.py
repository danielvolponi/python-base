#!/usr/bin/env python3
"""Errors

Programa que imprime na tela a posicao 1 da lista de nomes

"""
import os
import sys
import time
import logging

log = logging.Logger("errors")

# EAFP - Easy to Ask Forgiveness than permission
# (É mais fácil pedir perdão do que permissão)

def try_to_open_a_file(filepath, retry=1) -> list: 
    """Tries to open a file, if error, retries n times """
    for attempt in range(1, retry + 1):
        try:
            return  open(filepath).readlines()
        except FileNotFoundError as e:
            log.error("ERRO: %s", e) 
            time.sleep(1)
        else: 
            print("Sucesso") # Somente se o try funcionar
        finally:
            print("Execute isso sempre!")
    return []     

for line in try_to_open_a_file("names.txt", retry=5):
    print(line)
