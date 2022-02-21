class Estudante:
    def __init__(self, nome, idade, nota) -> None:
        self.nome = nome
        self.idade = idade 
        self.nota = nota # 0 - 100
        
    
class Curso:
    def __init__(self, nome_curso, max_alunos) -> None:
        self.nome = nome_curso
        self.max = max_alunos
        self.alunos = []

    def cadastro(self, aluno):
        if len(self.alunos) < self.max:
            self.alunos.append(aluno)
            return True  # Aluno cadastrado
        return print('Aluno não cadastrado')
    
    def mostra_alunos(self):
        for aluno in self.alunos:
            print(end=f'{aluno.nome}...{aluno.idade}...{aluno.nota}\n')
    
    def media_alunos(self):
        soma = 0
        for aluno in self.alunos:
            soma += aluno.nota
        return soma / len(self.alunos)
    

aluno1 = Estudante('Lucas', 23, 65)
aluno2 = Estudante('Carla', 33, 87)
aluno3 = Estudante('José', 25, 76)
aluno4 = Estudante('Manoel', 71, 100)
aluno5 = Estudante('Georgia', 31, 24)
aluno6 = Estudante('jujuba', 100, 1000)
curso_random = Curso('Escola mundial', 5)

curso_random.cadastro(aluno1)
curso_random.cadastro(aluno2)
curso_random.cadastro(aluno3)
curso_random.cadastro(aluno4)
curso_random.cadastro(aluno5)
curso_random.cadastro(aluno6)

print(curso_random.media_alunos())
curso_random.mostra_alunos()
        
        