from abc import ABC, abstractmethod, abstractproperty

class Conta(ABC):
    
    @abstractmethod
    def depositar(self, valor):
        ...
        
    @abstractmethod        
    def sacar(self, valor):
        ...


class Pessoa(ABC):
    
    @abstractproperty
    def nome(self):
        ...

    
    @nome.setter
    def nome(self, valor):
        ...
        

class ContaCorrente(Conta):
    def __init__(self, valor_inicial=0) -> None:
        from random import randint
        self.dinheiro = valor_inicial
        self.limite = randint(300, 1000)
        if self.limite > 500:
            self.juros_por_atrado = 0.5
        else:
            self.juros_por_atrado = 0.25
    
    def depositar(self, valor_deposito):
        self.dinheiro += valor_deposito

    def sacar(self, valor_saque):
        if self.dinheiro + self.limite >= valor_saque:
            if self.dinheiro >= valor_saque:
                self.dinheiro -= valor_saque
            else:
                valor_saque -= self.dinheiro
                self.dinheiro = 0
                self.limite -= valor_saque
        else:
            raise Exception("Você só tem %d para saque" % self.dinheiro + self.limite)


class ContaPoupanca(Conta):
    def __init__(self, valor_inicial=0) -> None:
        self.dinheiro = valor_inicial    
    
    def depositar(self, valor_deposito):
        self.dinheiro += valor_deposito
        
    def sacar(self, valor_saque):
        if self.dinheiro >= valor_saque:
            self.dinheiro -= valor_saque
        else:
            raise Exception("Você tem apenas %f para saque" % self.dinheiro)
      

class Cliente(Pessoa):
    def __init__(self, nome, conta) -> None:
        self.nome = nome
        self.conta = conta
    
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, name: str):
        caracteres_especiais = "!@#$%¨&*()_-+=[{}^~:;><.,']"
        
        if not isinstance(name, "str"):
            raise TypeError("Seu nome precisa ser do tipo string")
        
        name_has_special_characteres = any(
            [letter in caracteres_especiais for letter in name]
        )
        
        if name_has_special_characteres:
            raise Exception("Seu nome não pode ter caracteres especiais")

        self._nome = name.capitalize()


class Banco:
    def __init__(self) -> None:
        self.clientes = []
        
    def cadastrar_cliente(self, nome_cliente, tipo_conta, dep_inicial=0):
        assert tipo_conta in ("Corrente", "Poupança"), "Tipo de conta inválida"
        if tipo_conta == "Corrente":
            conta = ContaCorrente(dep_inicial)
        else:
            conta = ContaPoupanca(dep_inicial)
        cliente = Cliente(nome_cliente, conta)
        self.clientes.append(cliente)
    