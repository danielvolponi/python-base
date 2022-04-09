#!/usr/bin/bin/env python3
"""Exibe relatório de crianças por atividade

Imprimir a lista de crianças agrupadas por sala
que frequentam cada uma das atividades.
"""
__version__ = "0.1.2"

# Dados
salas = {
    "sala1": ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"],
    "sala2": ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]        
}

# Salas de atividades extra

aulas_extras = {
    "ingles": ["Erik", "Maia", "Joana", "Carlos", "Antonio"],
    "musica": ["Erik", "Carlos", "Maria"],
    "danca": ["Gustavo", "Sofia", "Joana", "Antonio"] 
}

atividades = {
    "Inglês": aulas_extras["ingles"],
    "Música": aulas_extras["musica"],
    "Dança": aulas_extras["danca"]
}

# Listar alunos em cada atividade por sala

for nome_atividade, atividade in atividades.items():

    print(f"Alunos da atividade {nome_atividade}\n")
    print("-" * 50)
    
    # sala1 que tem a interseção com a atividade
    atividade_sala1 = set(salas["sala1"]) & set(atividade)
    atividade_sala2 = set(salas["sala2"]) & set(atividade)
    
    print("Sala1 ", atividade_sala1)
    print("Sala2 ", atividade_sala2)
    print()
    print("#" * 40)
