class A:
    vc = 123   # Variavel de classe que esta disponivel para todas as instancias da classe

    def __init__(self):   # Este método é executado assim que instanciamos a classe
        # self.vc = 321   # Inicialmetne as duas instancias receberiam este valor, desta forma a variavel "vc" da classe estaria disponivel apenas diretamente na classe
        pass

a1 = A()   
a2 = A()


# A.vc = 321   # Usando a classe para alterar o valor da instancia. (O valor de todas as outras instancia será redefinido tanbém, caso o atributo "vc" já não exista na instancia)

a1.vc = 123   # Criando um atributo "vc" com o valor 123 diretamente na instancia
"""
* O interpretador do python vai buscar a variavel na instancia e caso não encontre, passa a buscar direto na classe
"""

print(a1.__dict__)   # Mostra todos os elementos da instancia. / Saida: {'vc': 123}
print(a2.__dict__)   # Mostra todos os elementos da instancia. / Saida: {}  # Não tem nenhum atributo
print(A.__dict__)    # Mostra todos os elementos da classe.    / Saida: {'__module__': '__main__', 'vc': 321, '__dict__': <attribute '__dict__' of 'A' objects>, '__weakref__': <attribute '__weakref__' of 'A' objects>, '__doc__': None}
 
print(a1.vc)
print(a2.vc)
print(A.vc)
