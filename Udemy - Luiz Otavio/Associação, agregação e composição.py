# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela


class Fabricante:
    def __init__(self, nome) -> None:
        self.nome = nome
        

class Motor:
    def __init__(self, nome, fabricante: Fabricante) -> None:
        self.nome = nome
        self.fabricante = fabricante
    
class Carro:
    def __init__(self, nome, fabricante: Fabricante) -> None:
        self.nome = nome
        self.fabricante = fabricante
        self.motor_de_fabrica = Motor("Motor de fábrica", self.fabricante)
        
    def trocar_motor(self, novo_motor):
        self.motor = novo_motor
        

volkswagem = Fabricante("Volks")
motor_1 = Motor("Motor 1.0", volkswagem)
carro_1 = Carro("Polo", volkswagem)
carro_2 = Carro("Vectrus", volkswagem)

