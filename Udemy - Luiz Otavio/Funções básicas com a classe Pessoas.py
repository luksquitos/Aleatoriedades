class Pessoa:
    def __init__(self, nome, comendo=False, falando=False) -> None:
        self.nome = nome
        self.comendo = comendo
        self.falando = falando
        
    def comer(self, coisa):
        if self.comendo:
            print(f"{cores[1]}{self.nome} já está comendo. {cores[0]}")
            return #Retorna None, mesmo não escrevendo nada.
        elif self.falando:
            print(f'{cores[1]}{self.nome} não pode comer enquanto fala{cores[0]}')
            return
        print(f'{cores[2]}{self.nome} está comendo {coisa}{cores[0]}')
        self.comendo = True
        
    def parar_comer(self):
        if self.comendo:
            print(f'{cores[2]}{self.nome} parou de comer{cores[0]}')
            self.comendo = False
            return None
        print(f'{cores[1]}Você não está comendo.{cores[0]}')
    
    def falar(self, assunto):
        if not self.comendo:
            print(f'{cores[2]}{self.nome} está falando sobre {assunto}{cores[0]}')
            self.falando = True  
            return None
        print(f"{cores[1]}{self.nome} não pode falar de boca cheia{cores[0]}")
    
    def parar_falar(self):
        if self.falando:
            print(f'{cores[2]}{self.nome} parou de falar{cores[0]}')
            self.falando = False
            return None
        print(f'{cores[1]}Você não está falando{cores[0]}')

cores = (
    '\033[m',
    '\033[31m',
    '\033[36m', 
)

p1 = Pessoa('Lucas')
p1.comer('paçoca')
p1.comer('paçoca')