# Gerador de senhas 

from random import choice, randint

random = (0, 1) # Serve apenas para ser chamado dentro do for.
caracteres = 'abcdefghijklmnopqrstuvwxyz1234567890!@#$%&*()'
password = ''


for vezes in range(randint(12, 24)):
    if choice(random) == 0:
        try:
            password += choice(caracteres.upper())
        except:
            password += choice(caracteres)
    else:
        password += choice(caracteres)

print(f'Senha gerada: {password}')

