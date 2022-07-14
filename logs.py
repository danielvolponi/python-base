#!/usr/bin/env python3
import os
import logging
from logging import handlers

# BOILERPLATE
# TODO: mover para um módulo de utilidades
# TODO: usar lib (loguru)
log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger("logs.py", log_level)
# ch = logging.StreamHandler() # Console/terminal/stdeer
# ch.setLevel(log_level)
fh = handlers.RotatingFileHandler(
    "meulog.log", 
    maxBytes=10**6, # 10 **6 (1mb)
    backupCount= 10
)
fh.setLevel(log_level)
fmt = logging.Formatter(
    '%(asctime)s  %(name)s  %(levelname)s '
    'l:%(lineno)d f:%(filename)s: %(message)s'
)
# ch.setFormatter(fmt)
# log.addHandler(ch)
fh.setFormatter(fmt)
log.addHandler(fh)

"""
# Mensanges de log com exemplo
# logging # root logger
log.debug("Mensagem pro dev, qe, sysadmin")
log.info("Mensagem geral para usuários")
log.warning("Aviso que não causa erro")
log.error("Erro que afeta uma única execução")
log.critical("Erro geral ex banco de dados sumiu")
"""

try:
    1 / 0
except ZeroDivisionError as e:
    log.error("Deu erro %s", str(e))
