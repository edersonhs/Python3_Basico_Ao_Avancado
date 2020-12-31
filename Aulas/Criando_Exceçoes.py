"""
Depois de buscar por todas as exceções do python na documentação e não
encontrar a desejada, pode-se criar uma excessão com o nome de sua escolha,
da seguinte forma:
"""
# Por convenção o nome do erro sempre termina com "Error"


class TaErradoError(Exception):   # Herda a classe "Exception" do python.
    pass


"""
Depois de criar a excessão, pode-se tratá-la como qualquer outra exceção do
python.
"""
# EX:


def testar():
    raise TaErradoError('Errado!')   # Levantando a exceção criada com o raise


# testar()   # __main__.TaErradoError: Errado!
try:
    testar()
except TaErradoError as erro:
    print(f'Erro: {erro}')   # Erro: Errado!
