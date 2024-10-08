from funcionario import Pessoa, Engenheiro, Secretario

f1 = Pessoa("Joana","Gerente")
engenheiro1 = Engenheiro("Roberto","Engenheiro Pleno")
secreatrio1 = Secretario("Getúlio", "Secretário Executivo")

f1.informacoes()

engenheiro1.informacoes()
engenheiro1.mostraDetalhes()

secreatrio1.relatorio()