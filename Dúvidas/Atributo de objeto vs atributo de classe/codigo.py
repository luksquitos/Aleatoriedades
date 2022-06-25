class Amigos:
    taxa = 1.05
    quant_amigos = 0
    list_amigos = []
    def __init__(self, nome, salario) -> None:
        self.nome = nome
        self.quant_amigos += 1 #Criação do atributo do objeto e acrescentação do valor 1
        Amigos.quant_amigos += 1 #Utilização da variável da classe
        self.list_amigos.append(self)#Utilização do atributo da classe
        self.salario = salario
        
    def aumento_salario(self):
        self.salario *= self.taxa #Se o objeto possuir o atributo, será usado o dele
                                  #Caso contrario sera usado o da classe.
 
var1 = Amigos('Ronaldo', 2300)
var2 = Amigos('Carlos', 1400)
var3 = Amigos('Juliano', 12)

print(var1.__dict__) # 1ª Execução
#{'nome': 'Ronaldo', 'quant_amigos': 1} #quant_amigos é um atributo do obj var1

print(var1.taxa)# 2ª Execução

#3ª Execução
var1.taxa = 4 #Criação do atributo taxa para o objeto var1
print(var1.taxa)
print(var2.taxa)
print(Amigos.taxa)