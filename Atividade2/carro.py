class Carro:
    #Método Construtor
    def __init__(self, marca, modelo, ano, precoDiaria):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.precoDiaria = precoDiaria
    
    #Criando os métodos
    def exibirDetalhes(self):
        print(f"O carro da marca {self.marca} e modelo {self.modelo} foi fabricado no ano {self.ano}")
    
    def calcularPrecoAluguel(self, diasAluguel):
        total = self.precoDiaria * diasAluguel
        return total
    