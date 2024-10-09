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

#Passo5 - Criar comando SQL para consultar os dados 
sql = "SELECT * FROM funcionario"

#Passo6 - Executar o comando sql
consulta.execute(sql)

#Passo7 - Exibir dados do banco
resultado = consulta.fetchall() # fetchall() irá trazer todos os registros que existem no banco de dados

print(resultado)

print("-"*50)
for itens in resultado:
    print(f"Código: {itens[0]}, Nome: {itens[1]}")

#passo8 - finalizar conexão
conexao.close()