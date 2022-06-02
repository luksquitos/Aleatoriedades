# Aula 83, 84, 85 | Luiz Otavio

def conversor(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:
        try:
            valor = float(valor)
            return valor
        except ValueError:
            return valor

while True:
    entrada = conversor(input("digite um número para ser somado: "))
    if isinstance(entrada, str):
        raise ValueError("\033[31mFoi digitado uma string") # O programa será encerrado aqui.
    print(round(entrada * 1.54, 3))

            