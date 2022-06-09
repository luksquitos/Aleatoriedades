# Vídeo 75 | Luiz Otavio Miranda

lista_a, lista_b = [1, 2, 3, 4, 5, 6], [1, 2, 5, 4, 11]
lista_soma = [x + y for x, y in zip(lista_a, lista_b)]

print(lista_soma)


#---- 2ª Maneira ----

# lista_menor = lista_a if len(lista_a) < len(lista_b) else lista_b
# lista_soma = []

# for index in range(len(lista_menor)):
#     lista_soma.append(lista_a[index] + lista_b[index])
# print(lista_soma)