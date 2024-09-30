#Estamos acessando o arquivo 'pessoa' e dentro do arquivo estamos importando a classe 'Pessoa'
from pessoa import Pessoa

#Criando os objetos
p1 = Pessoa("César", 49,"Lasanha")
p2 = Pessoa("Lívia",31, "Churrasco")

p1.mostrarComida()
p2.mostrarComida()