# Débora se inscreveu em uma rede social para se manter em contato com seus amigos. A página de cadastro exigia o preenchimento dos campos de nome e senha, porém a senha precisa ser forte. O site considera uma senha forte quando ela satisfaz os seguintes critérios:
# Possui no mínimo 6 caracteres.
# Contém no mínimo 1 digito.
# Contém no mínimo 1 letra em minúsculo.
# Contém no mínimo 1 letra em maiúsculo.
# Contém no mínimo 1 caractere especial. Os caracteres especiais são: !@#$%^&*()-+
# Débora digitou uma string aleatória no campo de senha, porém ela não tem certeza se é uma senha forte. Para ajudar Débora, construa um algoritmo que informe qual é o número mínimo de caracteres que devem ser adicionados para uma string qualquer ser considerada segura.

def menu():
    print(f'{cores[1]}{"Bem vindo ao validador de senha":.^50}{cores[0]}')
    print('A senha deve: \n')
    print(f'{cores[3]}• Possuir no mínimo 6 caracteres.')
    print('• Conter no mínimo 1 digito.')
    print('• Conter no mínimo 1 Letra minúscula')
    print(f'• Conter no mínimo 1 Caractere especial. Os caracteres especiais são: !@#$%^&*()-+{cores[0]}')
    


def validador_senha(senha: str):
    caracteres_especiais = '! @ # $ % ^ & * ( ) - +'.split()
    especiais = maiusculas = minusculas = digito = False

    if not len(senha) > 5:
        print(f'{cores[2]}A senha deve conter 6 caracteres.{cores[0]}')

    for letra in senha:
        if letra.isupper():
            maiusculas = True
        elif letra.islower():
            minusculas = True
        elif letra.isnumeric():
            digito = True
        elif letra in caracteres_especiais:
            especiais = True
        
    if not maiusculas:
        print(f'{cores[2]}Você precisa digitar ao menos 1 letra maiúscula.{cores[0]}')
    if not minusculas:
        print(f'{cores[2]}Você precisa digitar ao menos 1 letra minúscula.{cores[0]}')
    if not digito:
        print(f'{cores[2]}Você precisa digitar ao menos 1 número.{cores[0]}')
    if not especiais:
        print(f'{cores[2]}Você precisa digitar ao menos 1 caractere especial.{cores[0]}')

    if maiusculas and minusculas and digito and especiais:
        return False
    else:
        return True


cores = (
    '\033[m',    # Padrão
    '\033[7;33m',#Título
    '\033[31m',  # Vermelho
    '\033[33m',  # Amarelo
    '\033[32m'   # Verde
)

menu()

while True:
    senha = input('Digite uma senha: ')
    if not validador_senha(senha):
        print(f'\n{cores[4]}A senha cadastrada foi:{cores[0]} {senha}')
        break
    print()
