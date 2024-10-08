from pessoa import Pessoa, Aluno, Professor

pessoa1 = Pessoa("Getúlio", 65)
aluno1 = Aluno("Keila",16, "2º ano do ensino médio")
prof1 = Professor("Augusto", 49, "Geografia")

pessoa1.info()

aluno1.info()
aluno1.estudar()

prof1.info()
prof1.ensinar()