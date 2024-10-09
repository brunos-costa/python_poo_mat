from produto import Produto, Livro

produto1 = Produto("Mesa", 859.99)
livro1 = Livro("Mémorias Póstumas", 51.56,"Machado de Assis")

produto1.descrever()
livro1.descrever()
livro1.calcularDesconto()