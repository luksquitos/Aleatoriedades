# Gerador de senhas

from random import choice, randint


caracteres = 'abcdefghijklmnopqrstuvwxyz1234567890!@#$%&*()'
password = ''


for vezes in range(randint(12, 24)):
    random = randint(0, 1) # Serve apenas para gerar um valor aleatório
    if random:
        password += choice(caracteres.upper())
    else:
        password += choice(caracteres)

print(f'Senha gerada: {password}')

