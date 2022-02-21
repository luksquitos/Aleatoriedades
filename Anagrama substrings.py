# Duas palavras podem ser consideradas anagramas de si mesmas se as letras de uma palavra podem ser realocadas para formar a outra palavra. Dada uma string qualquer, desenvolva um algoritmo que encontre o número de pares de substrings que são anagramas.


palavra = input('Digite a palavra: ')
pares = dict()
gaveta = list()

for cont, index in enumerate(range(len(palavra)), 1):
    for resto in palavra[index + 1:]:
        if palavra[index] == resto:
            gaveta.append(index)
            gaveta.append(palavra.index(resto, index + 1))
            pares[f'Par {cont}'] = gaveta.copy()
            gaveta.clear()

contador_mostragem = len(pares.values())
cont = 1

for i1, i2 in (pares.values()):
    if contador_mostragem > 0:
        print(f'{cont}ºpar: {palavra[i1]}, {palavra[i2]}')
        contador_mostragem -= 1
        cont += 1
for i1, i2 in pares.values():
    print(f'{cont}ºpar: {palavra[i1: i2]}, {palavra[i2: i1: -1]} ')
    cont += 1
    
print(f'A quantidade de pares encontrados foram {cont - 1}')
    