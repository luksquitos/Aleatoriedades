# Aulas 80, 81, 82 | Luiz Otávio

from functools import reduce

produtos = [
    {"nome": "p1", "preco": 43.12},
    {"nome": "p2", "preco": 12.40},
    {"nome": "p3", "preco": 9.90},
    {"nome": "p4", "preco": 13.50},
    {"nome": "p5", "preco": 1999.99},    
    {"nome": "p6", "preco": 0.90},
    {"nome": "p7", "preco": 4.90},
]

def aumento_preco(dic):
    dic['preco'] = round(dic['preco'] * 1.15, 2) # Aumento de 15%
    return dic

produtos_arrumados = map(aumento_preco, produtos)
carrinho = filter(lambda dic: dic['preco'] > 10, produtos_arrumados)
soma_carrinho = reduce(
    lambda soma, dic: soma + dic['preco'], carrinho, 0
)

print(soma_carrinho)

