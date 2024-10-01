from carro import Carro

#Criando Objetos
carro1 = Carro("Chevrolet", "Onix",2022, 150)
carro2 = Carro("Fiat", "Fusion",2021,100)

carro1.exibirDetalhes()
print("O valor das diárias pagas no caaro 1 é ",carro1.calcularPrecoAluguel(4))

carro2.exibirDetalhes()
print("O valor das diárias pagas no caaro 2 é ",carro2.calcularPrecoAluguel(10))