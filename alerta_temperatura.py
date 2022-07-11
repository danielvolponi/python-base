#!/usr/bin/env python3
"""
Alarme de temperatura
Faça um script que pergunta ao usuário qual a temperatura atual e o indice de
umidade do ar sendo que caso será exibida uma mensagem de alerta dependendo das
condições:
temp maior 45: "ALERTA!!! 🥵 Perigo calor extremo"
temp maior que 30 e temp vezes 3 for maior ou igual a umidade:
    "ALERTA!!! 🥵♒ Perigo de calor úmido"
temp entre 10 e 30: "😀 Normal"
temp entre 0 e 10: "🥶 Frio"
temp <0: "ALERTA!!! ⛄ Frio Extremo."
ex:
python3 alerta.py
temperatura: 30
umidade: 90
...
"ALERTA!!! 🥵♒ Perigo de calor úmido"
"""
import sys
import os
import logging
from logging import handlers
from typing import Dict

log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger("alerta", log_level)
fmt = logging.Formatter(
    '%(asctime)s  %(name)s  %(levelname)s '
    'l:%(lineno)d f:%(filename)s: %(message)s'
)
ch = logging.StreamHandler()  # Console/terminal/stderr
ch.setLevel(log_level)
ch.setFormatter(fmt)
log.addHandler(ch)

# TODO: Mover para módulo de utilidades

def is_completely_filled(dict_of_inputs: Dict) -> bool:
    """Return a boolean telling if a dict is a completly filled."""
    info_size = len(dict_of_inputs)
    filled_size = len(
        [value for value in dict_of_inputs.values() if value is not None]
        )
    return info_size == filled_size
    

def read_inputs_for_dict(dict_of_info):
    """Read information for a dict from a user input."""
    for key in dict_of_info.keys():
            if dict_of_info[key] is not None:
                continue
                
            try:
                dict_of_info[key] = float(input(f"Qual a {key}? ").strip())
            except ValueError:
                log.error(f"{key.capitalize()} inválida")
                break # para o for
                
# Programa Principal

info = {
    "temperatura": None,
    "umidade": None
}

while not is_completely_filled(info):
    read_inputs_for_dict(info)
    
temp, umidade = info.values()



if temp >= 45:
    print("ALERTA!!! 🥵 Perigo calor extremo")
elif temp * 3 >= umidade and temp > 30:
    print("ALERTA!!! 🥵♒ Perigo de calor úmido")
elif temp >= 10 and temp <= 30:
    print("😀 Normal")
elif temp >= 0 and temp <= 10:
    print("🥶 Frio")
elif temp < 0:
    print("ALERTA!!! ⛄ Frio Extremo.")
