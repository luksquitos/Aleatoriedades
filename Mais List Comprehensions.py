from random import randint

carrinho = ( # Gerador
    (f'Produto_{n}', randint(100, 1000))
    for n in range(1, 10)
)

preços = sum([valor for nome, valor in carrinho])

print(preços)