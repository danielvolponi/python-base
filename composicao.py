#!/usr/bin/env python3
"""
Buscar todos os nomes que comecam com a letra B"""

names = [
    "Bruno",
    "Joao", 
    "Bernardo",
    "Barbara",
    "Brian",
]

# TODO: Usar lambdas
def starts_with_b(text):
    return text[0].lower() == "b"
    # return text.lower().startswith("b")

print(*list(filter(starts_with_b, names)))

# for name in names:
    # if name.lower().startswith("b"):
        # print(name)
