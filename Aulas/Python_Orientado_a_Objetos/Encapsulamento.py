"""
Nas outras linguagens: public, protected, private

No python existem convenções que funcionam de forma semelhante a estas palavras reservadas:
_ - Private / Protected - O atributo/metodo é privado (de forma mais sutil, ou seja, ele não é recomendado pelo IDE, mas ainda pode ser utilizado publicamente. Entretanto por convenção, a variavel não deve ser acessada fora da classe)
__ - Private. Proibe que o atributo/metodo seja acessado fora da classe   (Pode ser acessado e alterado , caso haja a necessidade com: _NOMECLASSE_nomeatributo) 
"""

class BaseDeDados:
    def __init__(self):
        self.__dados = {}
    
    @property
    def dados(self):   # Caso seja necessario dar o acesso aos dados do atributo __dados, pdoe-se usar getters e setters
        return self.__dados
    
    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})   # Atualiza o dicionario, inserindo os novos dados
    
    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self._dados['clientes'][id]

bd = BaseDeDados()
bd.inserir_cliente(1, 'Otávio')
bd.inserir_cliente(2, 'Miranda')
bd.inserir_cliente(3, 'Rose')
# bd.apaga_cliente(2)

bd.__dados = 'Outra coisa'   # Neste caso a classe não quebra, pois o Python impede que o atributo da classe seja alterado, criando um outro atributo
# bd._dados = 'Outra coisa'   # Exemplo de ocorrencia que poderia quebrar a classe se alterado, por isso deve-se respeitar a convenção
bd.lista_clientes()

print(bd.__dados)   # Saída: Outra coisa.   / O interpretador do python criou outro atributo com o mesmo nome, trocando o nome do atributo __dados que não pode ser alterado para _NomeDaClasse__Atributo
print(bd._BaseDeDados__dados)   # Para visualizar o atributo real fora da classe
print(bd.dados)   # Executando o método dados(que é um getter) que pega os dados do atributo __dados que é privado lá na classe

bd.dados = 'Outro valor'   # levanta uma excessão por que não por que o Python impede de alterar, mas sim por que um setter não foi configurado para o getter   /   AttributeError: can't set attribute
