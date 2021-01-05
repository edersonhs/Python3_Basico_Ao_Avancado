class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade

    @nome.setter
    def nome(self, value):
        if isinstance(value, str):
            self._nome = value

    @idade.setter
    def idade(self, value):
        if isinstance(value, int):
            self._idade = value


class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
