#TODO Criar a classe de curas

class Player:
    arsenal = {}
    def __init__(self) -> None:
        self.vida = 100.0
        self.arma = None
        self.dano = 1
        self.carteira = 10000
        
    def andar(self):
        pass    #posição do objeto varia com a movimentação dele
    
    def mudar_arma(self):
        for arma in self.arsenal.values():
            print(arma.nome)
        op = input("Qual arma você gostaria de equipar: ")
        if self.arsenal[op] in self.arsenal.values():
            self.arma = op
            self.dano = self.arsenal[op].dano
        else:
            print('ESSA ARMA NÃO ESTÁ NO SEU INVENTÁRIO, STRANGER')
        
    def atacar(self, inimigo):
        inimigo.vida -= self.dano

class Pistola:
    def __init__(self, nome, dano, recuo) -> None:
        self.nome = nome
        self.dano = dano
        self.recuo = recuo# Tempo para o próximo ataque
    def __str__(self) -> str:
        return self.nome
            
class Mercador:
    opcoes = {
        'deagle':  Pistola('Deagle', 20, 5), 
        'preco_deagle' : 1500,
        'usp': Pistola('USP', 15, 10),
        'preco_usp': 900
    }
    
    def __init__(self) -> None:
        self.vida = 10

    def vender_armas(self, escolha_player=None, player=None):
        if not escolha_player and not player:
            print("WHAT ARE YOU BUYING")
            print(Mercador.opcoes)
        else:
            if Mercador.opcoes[f"preco_{escolha_player}"]<= player.carteira:
                inp = input("Is that all stranger ?\n"
                    f"Gostaria de comprar a {escolha_player}")
                player.arsenal[escolha_player] = escolha_player
                player.carteira -= Mercador.opcoes[f"preco_{escolha_player}"]
                Mercador.opcoes.pop(escolha_player)
            else:
                print("NOT ENOUGH CASH, STRANGER")
                
class Inimigo:
    contato = True
    def __init__(self, vida, forca) -> None:
        self.vida = vida
        self.forca = forca
    def attack(self, objeto):
        if self.contato:
            objeto.vida -= 15
        return True
    
leon = Player()
verdugo = Inimigo(forca=300, vida = 1000)
ganado = Inimigo(100, 10)
handgun = Pistola('Handgun', 10, 2) # Essa arma seria encontrada no chão
leon.arsenal[handgun.nome] = handgun
leon.mudar_arma()
print(leon.arma)
print(leon.dano)
print(leon.vida)
print(leon.arma)



# verdugo.attack(leon)
# miojão = Mercador()

# print(leon.arsenal)
# print(leon.vida)