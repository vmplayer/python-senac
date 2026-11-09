class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def resumo(self):
        print(f"Nome: {self.nome}")
        print(f"Preço: R${self.preco}")
        print(f"Qtd. estoque: {self.estoque} unidades.")

    def vender(self, quantidade):
        if quantidade <= 0:
            return "Erro: Quantidade inválida."
        elif quantidade > self.estoque:
            return "Erro: Estoque Insuficiente"
        else:
            self.estoque -= quantidade
            return f"Venda realizada!\nValor da venda: R${self.preco * quantidade}."

produto1 = Produto("PlayStation 5", 3000.00, 10)
produto2 = Produto("Honda Civic", 128000, 5)

produto1.resumo()
print()
print(produto1.vender(5))
print("\n-----------------\n")
produto1.resumo()
