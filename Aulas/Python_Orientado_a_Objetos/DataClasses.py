"""
O que são dataclasses? O módulo dataclasses fornece um decorador e funções
para criar automaticamente métodos, como __init__(), __repr__(), __eq__ (etc)
em classes definidas pelo usuário.
Basicamente, dataclasses são syntax sugar para citar classes normais.

Foi originalmente descrito na PEP 557.
Adicionado na versão 3.7 do Python.

Leia a documentação: https://docs.python.org/pt-br/3/library/dataclasses.html
"""
from dataclasses import dataclass
from dataclasses import field, fields   # Para ocultar parametros do repr
from dataclasses import asdict, astuple   # Converter a classe para dict/tuple

# @dataclass(eq=False, repr=False, order=False, frozen=False, init=False)
# para desativar a definição automatica dos métodos magicos.
# O padrão é: eq=True, repr=True, order=False, frozen=False, init=True


@dataclass(order=True)
class Pessoa:
    nome: str
    # Sobrenome não será mostrado no repr e terá uma valor padrão 'Missing'
    sobrenome: str = field(default='Missing', repr=False)

    # Caso seja necessario utilizar o init, pode-se desativar o init da
    # dataclass ou utilizar o __post_init__() que é executado APÓS o init
    def __post_init__(self):
        # levantando exceção caso nome não seja uma string
        if not isinstance(self.nome, str):
            raise TypeError(
                f'Invalid Type {type(self.nome).__name__} != str em {self}')

    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'


"""
Com dataclasses, por padrão já temos um __repr__ definido, ou seja, ao printar
a classe teremos uma apresentação legivel para pessoas e não a posição de
memoria, conforme ocorria anteriormente.
"""
p1 = Pessoa('Luiz', '8')
print(p1)    # Pessoa(nome='Luiz', sobrenome='Otavio')
print(p1.nome)
print(p1.sobrenome)
print(p1.nome_completo)

# O método também __eq__ é configurado por padrão pela dataclass
p2 = Pessoa('João', '3')
print(p1 == p2)

# o parametro order da dataclass permite que as instancias sejam ordenadas
pessoas = [p1, p2]
print(sorted(pessoas))   # ordena as instancias por ordem alfabetica
print(sorted(pessoas, key=lambda pessoa: pessoa.sobrenome))   # Ord. sbr.nome

print()

print(asdict(p1))   # Convertendo p1 em um dicionario
print(astuple(p1))   # Convertendo p1 em uma tupla

print(fields(p1))   # Mostra todos os fields da instancia
