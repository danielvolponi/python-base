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



info = {
    "temperatura": None,
    "umidade": None
}

keys = info.keys()

for key in keys:
    try:
        info[key] = float(input(f"Qual a {key}? ").strip())
    except ValueError:
        log.error(f"{key.capitalize()} inválida")
        sys.exit(1)

temp = info["temperatura"]
umidade = info["umidade"]



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
