from conta import ContaCorrente, ContaPoupanca


class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade


class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.conta = None   # Criando o atributo para preencher posteriormente

    def inserir_conta(self, agencia, conta, saldo, tipo=2, limite=0):
        if tipo == 1:
            if limite == 0:
                self.conta = ContaCorrente(agencia, conta, saldo)
            else:
                self.conta = ContaCorrente(agencia, conta, saldo, limite)
        if tipo == 2:
            self.conta = ContaPoupanca(agencia, conta, saldo)
