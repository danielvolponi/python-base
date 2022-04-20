#!/usr/bin/env python3
"""Calculadora infix.

Funcionamento: 

[operacao] [n1] [n2]

Operações:
sum -> +
sub -> -
mul -> *
div -> /

Uso:
$ infixcalc.py sum 5 2
7

$ infixcalc.py mul 10 5
50

$ infixcalc.py 
operação: sum
n1: 5
n2: 4
9
"""
__version__ = "0.1.0"
__author__ = "Daniel Volponi"
__license__ = "Unlicense"

import sys

arguments = {
    "operation": None,
    "n1": None,
    "n2": None
}


if len(sys.argv[1:]) == 3:
    arguments["operation"] = sys.argv[1]
    arguments["n1"] = sys.argv[2]
    arguments["n2"] = sys.argv[3]
else: 
    arguments["operation"] = input("Operação: ")
    arguments["n1"] = input("n1: ")
    arguments["n2"] = input("n2: ")

operation = arguments["operation"]
n1 = float(arguments["n1"])
n2 = float(arguments["n2"])

calc = {
    "sum": n1 + n2,
    "difference": n1 - n2,
    "product": n1 * n2,
    "quotient": n1 / n2,
}

print(calc[operation])
