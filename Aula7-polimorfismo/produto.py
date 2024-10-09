class Produto:
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    def descrever(self):
        print(f"O produto {self._nome} custa R$ {self._preco}")

    def calcularDesconto(self):
        pass# este método, na calasse mãe não terá nenhum conteúdo, mas deverá ser utilizado pelas classes filhas

# Classe filha 1 - Livro
class Livro(Produto):
    def __init__(self,nome, preco, autor):
        super().__init__(nome, preco)
        self._autor = autor

    def descrever(self):
        print(f"O livro {self._nome} foi escrito por {self._autor}" )
    
    def calcularDesconto(self):
        desconto = self._preco * 0.1# estamos aplicando um desconto de 10% no livro
        print(f"O livro {self._nome} está com 10% de desconto, custará {self._preco - desconto}")