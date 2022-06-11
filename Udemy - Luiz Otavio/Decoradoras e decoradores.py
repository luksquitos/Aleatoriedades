from pprint import pprint
from functools import reduce
from datetime import datetime


def master(func):
    def decorador(*args, **kwargs):
        # if not kwargs: #Isso está falando que se não tiver kwargs (BUG)
        if not kwargs['ler']:
            execute = func(*args, **kwargs)
            try:
                with open("registro.txt", "a") as registro:
                    registro.write(f"A funcao foi acessada as {datetime.now()} horas.\nCom o resultado {execute}\n")               
                return execute
            except FileNotFoundError:
                raise FileNotFoundError("\033[31m404 file not found")
        else:
            try:
                with open("registro.txt") as registro:
                    pprint(list(registro))
            except:
                   raise FileNotFoundError("\033[31m404 file not found")
    return decorador

@master
def soma_todos(*args, ler=False):
    """
    Essa função só vai servir pra ver quando ela será acessada e colocar o momento dentro de um bloco de notas.
    """
    return reduce(lambda acu, vals: acu+vals, args, 0)

var = soma_todos(11, 22, 33, 44, 55, 66, ler=False) # Não funciona se não especificarmos o valor de ler.



