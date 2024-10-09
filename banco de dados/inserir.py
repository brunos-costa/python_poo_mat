import sqlite3 #Importando uma biblioteca de banco de dados

#Passo1 - Estabelecendo conexão com o banco
conexao = sqlite3.connect("departamento.db")# estamos criando um arquivo que irá guardar o nosso banco de dados

#Passo2 - Verificar se a tabela existe ou não
tabela = """
CREATE TABLE IF NOT EXISTS funcionario(
    codigo INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100),
    salario FLOAT,
    cargo VARCHAR(100)
);
"""
#Passo3 - Acessar o bjeto da biblioteca sqlite3 para manipular o banco
consulta = conexao.cursor() #O objeto cursor()  é responsável por manipular dados do banco

#Passo4 - executar o comando de criação da tabela
consulta.execute(tabela)

#Passo5 - solicitar dados 
nome = input("Informe o nome do funcionário: ")
salario = float(input("Informe o salário do funcionário: "))
cargo = input("Informe o cargo do funcionário: ")

#Passo6 - Criando comando SQL para inserir os dados
sql = "INSERT INTO funcionario VALUES(?,?,?,?)" # colocamos ? no lugar dos dados reais, para evitar possíveis ataques de sql injection. Isso é uma implemnetação da biblioteca sqlite3

#Passo7 - Organizar os dados que irão substituir a ? no comando sql para inserir os dados
campos = (None,nome, salario, cargo)#Criando uma tupla com os dados que serão trocados por ?. Ao informar o valor 'None', estamos dizendo que será atribuído o valor padrão do AUTOINCREMENT.

#Passo8 - Executar o comando sql e substituir ? pelos campos
consulta.execute(sql, campos)

#Passo9 - Gravar os dados no banco
conexao.commit()

print(consulta.rowcount, " linha(s) inseridas com sucesso")

#passo10 - finalizar conexão
conexao.close()