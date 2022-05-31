#Dentro os alunos da sala, será escolhido de forma aleatória um aluno diáriamente para apagar o quadro. Depois que passar a vez do aluno, ele não irá apagar o quadro até que todos tenham apagado.

from random import choice

def escolher_aluno():
    alunos = [
        "Carlos Alberto",
        "Julia Martins",
        "Carlinha Mariana",
        "Marcos Ricardo",
        "Lucia Vordex",
        "Valdemort Ronaldo",
        "Paulo Eduardo",
        "Bruna Surfistinha",
    ]
    dia = 1
    while alunos:
        escolhido = choice(alunos)
        alunos.remove(escolhido)
        yield f'{dia}º dia: {escolhido}'
        dia += 1
    
escolhido = escolher_aluno()

print(next(escolhido))
print(next(escolhido))
print(next(escolhido))
print(next(escolhido))
print(next(escolhido))
print(next(escolhido))
print(next(escolhido))
print(next(escolhido))
  