"""
Na agregação as classes podem existir uma sem a outra, entretanto um não funciona corretamente sem o outro
"""
from classes import *

carrinho = CarrinhoDeCompras()   # CarrinhoDeCompras pode ser instanciada sem a classe produtos, apesar da classe não poder fazer nada sem a classe Produtos.
# print(carrinho)

p1 = Produto('Camiseta', 50)
p2 = Produto('iPhone', 10000)
p3 = Produto('Caneca', 15)

carrinho.lista_produtos()   # Neste momento o carrinho esta vazio

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)
carrinho.inserir_produto(p1)   # Não tem problema adicionar o mesmo produto mais de uma vez, pois são dois produtos independentes dentro do carrinho

carrinho.lista_produtos()   # Agora os 4 produtos estão no carrinho
print(carrinho.soma_total())   # Saída: 10115
