#!/usr/bin/env python3
"""Bloco de notas

$ notes.py new "Minha nota"
tag: tech
text: Anotacao geral sobre carreira de tecnologia

$ notes.py read tech
...
...
"""
__version__ = "0.1.0"

import os
import sys

cmds = ("read", "new", "list-tags")
path = os.curdir
filepath = os.path.join(path, "notes.txt")

arguments = sys.argv[1:]

if not arguments:
    print("Invalid usage")
    print(f"You must specify subcommand {cmds}")
    sys.exit(1)


if arguments[0] not in cmds:
    print(f"Invalid comand {argument[0]}")

if arguments[0] == "read":
    # leitura das notas
    for line in open(filepath):
        title, tag, text = line.split("\t")
        if tag.lower() == arguments[1].lower():
            print(f"title: {title}")
            print(f"text: {text}")
            print("-" * 30)
            print()
    
if arguments[0] == "new":
    try:
        title = arguments[1]
    except IndexError as e:
        print(f"[ERROR] {str(e)}")
        print("You must specify a title like `notes.py new Note`")
        sys.exit(1)
    
    text = [
        f"{title}",
        input("tag: ").strip(),
        input("text:\n").strip(),
    ]
    # \t - txt
    with open(filepath, "a") as file_:
        file_.write("\t".join(text) + "\n")


if arguments[0] == "list-tags":
    # lista todas as tags
    tags = []
    for line in open(filepath):
        title, tag, text = line.split("\t")
        tags.append(tag)

    tags = set(tags)
    print(tags)
