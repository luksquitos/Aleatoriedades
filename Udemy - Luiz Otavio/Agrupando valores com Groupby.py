#Vídeo 79 | Luiz Otavio

from itertools import groupby

alunos = [
    {"nome": "Lucas", "nota": "A"},
    {"nome": "Júlio", "nota": "C"},
    {"nome": "Maria", "nota": "D"},
    {"nome": "Carlos", "nota": "F"},
    {"nome": "Miranda", "nota": "F"},
    {'nome':'luiz','nota':'A'},
    {'nome':'Nice','nota':'B'},
    {'nome':'Mario','nota':'A'},
    {'nome':'Joaquim','nota':'B'},
    {'nome':'Joana','nota':'C'},
    {'nome':'Maria','nota':'C'},
    {'nome':'Pedro','nota':'D'},
    {'nome':'José','nota':'A'},
    {'nome':'Marcela','nota':'D'}
]

alunos.sort(key=lambda dic: dic['nota'])
new = groupby(alunos, lambda dic: dic['nota'])
# new2 = list(groupby(alunos, lambda dic: dic['nota'])) # Tenta fazer assim. To com problema nesse

for nota, iterador_valores in new:
    print(f'Agrupamento {nota}')
    # print(len(list(iterador_valores))) #Se ambos estiverem mostrando, todo o iterador será consumido
    for dicionarios in iterador_valores:
        print(dicionarios)
    print('-' * 20)
