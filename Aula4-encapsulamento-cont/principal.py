from funcionario import Funcionario

funcionario1 = Funcionario("Gerente",3000)
print("Seu cargo atual é: ",funcionario1.getCargo())

#Tentando mudar o valor do atributo
funcionario1.__cargo = "Supervisor"# Acessando o atributo direto
funcionario1.setCargo("Engenheiro")# acessando o método para mudar o cargo
print("Seu cargo atual é: ",funcionario1.getCargo())

# EXIBINDO O SALÁRIO
print("O seu salário atual é ", funcionario1.salario)

funcionario1.salario = -100
print("O seu salário atual é ", funcionario1.salario)