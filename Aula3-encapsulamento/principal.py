from contaBancaria import Conta

minhaConta = Conta(123,"Ermenegildo Sousa",1000)

minhaConta.detalhes()

print(f"O limite atual é {minhaConta.getLimite()}")

minhaConta.setLimite(259)# alterando o valor do limite

print(f"O limite atual é {minhaConta.getLimite()}")

minhaConta.depositar(100)
minhaConta.detalhes()

minhaConta.sacar(500)
minhaConta.detalhes()