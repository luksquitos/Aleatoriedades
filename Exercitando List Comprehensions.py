string = '0123456789012345678901234567890123456789012345678901234567890123456789'

lista = ['0' + fatiado for fatiado in string.split('0')]
lista2 = [string[i: i+10] for i in range(0, len(string), 10)]

print('.'.join(lista)[2:])
print('.'.join(lista2))