class A:
    def falar(self):
        print('Falando... Estou em A')


class B(A):   # Herda a classe A e sobrescreve o metodo falar
    def falar(self):
        print('Falando... Estou em B')


class C(A):   # Herda a classe A e sobrescreve o metodo falar
    def falar(self):
        print('Falando... Estou em C')


class D(B, C):   # Herda a classe B e C que possuem o mesmo método.
    """
    O interpretador vai buscar o método falar() em D, se não encontrar, em B,
    se não encotrar buscará em C e se não encontrar novamente, buscará em A,
    que é herdada em C.
    """

    def falar(self):
        print('Falando... Estou em D')


d = D()
d.falar()   # Falando... Estou em D
