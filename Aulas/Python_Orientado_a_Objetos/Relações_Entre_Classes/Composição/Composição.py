"""
Composição - È a relação mais forte entre classes

Neste caso uma classe será a "dona" de objetos de outras classes. Ou seja, se a classe principal for apagada,
todos os objetos que classe principal utilizou serão apagados com ela.
"""
from classes import *

cliente1 = Cliente('Luiz', 32)
cliente1.insere_endereco('Belo Horizonte', 'MG')
print(cliente1.nome)
cliente1.lista_enderecos()
del cliente1   # Apaga o objetos do cliente1 manualmente, ou seja, no fim do código o garbage collector não vai precisar apagar mais ele
print()

# Um cliente com dois endereços
cliente2 = Cliente('Maria', 55)
cliente2.insere_endereco('Salvador', 'BA')
cliente2.insere_endereco('Rio de Janeiro', 'RJ')
print(cliente2.nome)
cliente2.lista_enderecos()
print()

cliente3 = Cliente('João', 19)
cliente3.insere_endereco('São Paulo', 'SP')
print(cliente3.nome)
cliente3.lista_enderecos()
print()

print('##############################################################################')
"""
Quando o codigo esta terminando o Garbage collector(Coletor de lixo) do python apagou os 
elementos que ainda estavam na memoria.

-------------------------------------------
Saída no terminal após o fim do código:
###########################################

Maria FOI APAGADO   # Apagou Maria e todos os endereços que pertenciam a ela, que são instancias da classe endereço
Rio de Janeiro/RJ FOI APAGADO
Salvador/BA FOI APAGADO
João FOI APAGADO    # Apagou João e todos os endereços que pertenciam a ele, que são instancias da classe endereço
São Paulo/SP FOI APAGADO
"""
