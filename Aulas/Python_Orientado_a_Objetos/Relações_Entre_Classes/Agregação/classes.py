"""
Abaixo temos um exemplo de agregação, onde esta classe pode existir sozinha, entretanto ela precisa que a classe 
Produtos exista para funcionar corretamente, visto que todos os metodos da classe CarrinhoDeCompras precisam dos produtos
"""

class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []   # Lista para receber objetos produtos (Uma classe inteira de produtos)
    
    def inserir_produto(self, produto):
        self.produtos.append(produto)
    
    def lista_produtos(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)
    
    def soma_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return total


# A classe produto pode existir sozinha e não depende em nada da classe CarrinhoDeCompras
class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor
