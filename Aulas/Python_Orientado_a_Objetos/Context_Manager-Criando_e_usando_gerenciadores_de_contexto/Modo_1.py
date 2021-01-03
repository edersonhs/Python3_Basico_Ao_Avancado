"""
Já vimos quie sempre que precisamos abrir e fechar algo, é necessário um
gerenciador de contexto. Ex:

arquivo = open('abc.txt', 'w')   # Abre o arquivo
arquivo.write('Alguma coisa')   # Escreve no arquivo
arquivo.close()   # Fecha o arquivo

Para evitar que o programador esqueça de fechar o arquivo, o que teria como
resultado possiveis erros no programa. O pessoal de desenvolvimento python
resolveu utilizar um gerenciador de contexto que faz este serviço para você.

Ex:
with open('abc.txt', 'w') as arquivo:   # Abre o arquivo
    arquivo.write('Alguma coisa')   # Escreve no arquivo
    # Fecha automaticamente o arquivo quando termina

O python permite que o programador crie gerenciadores de contexto mais
especificos como para conexões de rede, ou base de dados de dados por exemplo.
"""

# Criando um gerenciador de contexto:


class Arquivo:
    # Fazendo com que a classe funcione como um gerenciador de contexto:
    def __init__(self, arquivo, modo):
        print('Abrindo arquivo')
        self.arquivo = open(arquivo, modo)   # Abre o arquivo

    def __enter__(self):   # É chamado quando o "with" é executado
        print('Retornando arquivo')
        # Retorna o que irá para a variavel especificada (nesse ex é arquivo)
        return self.arquivo   # Retorna o arquivo

    # Método de saída que é executado quando o "with" termina a execução:
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Fechando arquivo')
        self.arquivo.close()   # Fehcando arquivo

        """
        Parâmetros que só serão executados caso ocorra alguma exceção:
        exec_type   # Tipo da exceção
        exec_val   # O valor incorreto
        exec_tb   # O traceback da exceção

        Caso sejam printados sem ocorrer nenhuma exceção retornam None:
        """
        # print(exc_type, exc_val, exc_tb)   # None None None

        """
        Estes parâmetros servem para que o programador trate as exceções
        podendo fazer com que o Python não levante uma exceção, Ex:
        """
        # Impede que o Python levante uma exceção levando em conta que o
        # programador já tratou o problema
        return True


with Arquivo('abc.txt', 'w') as arquivo:
    arquivo.write('Alguma coisa')
