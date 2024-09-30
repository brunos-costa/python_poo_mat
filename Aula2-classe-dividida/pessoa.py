class Pessoa:
    #criando método construtor
    def __init__(self, nome, idade, pratoPreferido):
        self.nome = nome
        self.idade = idade
        self.pratoPreferido = pratoPreferido
    
    #criando métodos
    def mostrarComida(self):
        print(f"{self.nome} gosta de comer {self.pratoPreferido}")