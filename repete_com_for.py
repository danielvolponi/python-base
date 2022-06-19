#!/usr/bin/env python3

original = [1, 2, 3]

# For loops / laço for
dobrada = []
for n in original:
    dobrada.append(n * 2)

print(dobrada)

# Abordagem Funcional
# List comprehension
dobrada = [n * 2 for n in original]
print(dobrada)

# Dict Comprehension
dados = {
    line.split(":")[0]: line.split(":")[1].strip()
    for line in open("post.txt") 
    if ":" in line
}
print(dados)
