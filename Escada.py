# Escreva um algoritmo que mostre na tela uma escada de tamanho n utilizando o caractere * e espaços. A base e altura da escada devem ser iguais ao valor de n. A última linha não deve conter nenhum espaço.

num_desejado = input('Digite um número: ')

while not num_desejado.isnumeric():
    num_desejado = input('Digite um número válido: ')
num_desejado = int(num_desejado)
    
acumulador = ''

for regressivo in range(num_desejado, 0, -1):
    acumulador += '*'
    print(f'{" " * regressivo} {acumulador}')
    