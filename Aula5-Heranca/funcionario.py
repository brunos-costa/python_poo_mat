class Pessoa: #superclasse ou classe-mãe
    def __init__(self, nome, cargo):
        # Estamos mudando a visibilidade do atributo de privado para protegido, dessa forma, as classes filhas poderão acessar os atributos da classe mãe.
        self._nome = nome
        self._cargo = cargo

    def informacoes(self):
        print(f"Olá {self._nome}, na empresa, seu cargo é: {self._cargo}")    

#CRIANDO CLASSE FILHA
class Engenheiro(Pessoa):# a classe Engenheiro está herdando as características da classe Pessoa, que será sua classe mãe
    def mostraDetalhes(self):
        print(f"Olá, eu sou {self._nome} e sou um engenheiro")
    

class Secretario(Pessoa):
    def relatorio(self):
        print(f"Olá meu cargo é {self._cargo}")