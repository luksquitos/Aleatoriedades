#Vídeo 93 | Luiz Otavio

from pprint import pprint


def menu():
    print(f"{cores[2]}1: Adicionar Tarefa")
    print("2: Listar Tarefas")
    print("3: Desfazer")
    print("4: Refazer")
    print(f"0: Sair{cores[0]}")

cores = (
    '\033[m',
    '\033[31m',
    '\033[33m',
    '\033[32m',
)

tarefas = list()
cache = list()

while True:
    menu()
    try:
        op = int(input("Digite um valor: "))
    except ValueError:
        print("Digite um valor inteiro\n")
        continue
    match op:
        case 1:
            task = input("Tarefa: ")
            tarefas.append(task)
            print(f'{cores[3]}Tarefa {task} adicionada {cores[0]}\n')
        case 2:
            print(tarefas)
        case 3:
            cache.append(tarefas[-1])
            tarefas.pop(-1)
        case 4:
            tarefas.append(cache[-1])
            cache.pop(-1)
        case 0:
            break
        case default:
            raise "Option not found"
        
            