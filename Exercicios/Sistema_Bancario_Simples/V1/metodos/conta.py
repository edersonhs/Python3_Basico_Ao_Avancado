from abc import ABC, abstractmethod


class Banco:
    agencia = 101
    clientes = ['João', 'Mateus', 'Igor']
    contas = [1518, 1010, 2020]

    def __init__(self, cliente, conta):
        self.cliente = cliente
        self.conta = conta

        if __name__ == 'Banco':
            if self.conta.agencia != self.agencia:
                print('O cliente é de uma agencia diferente!')
            if self.cliente.nome not in self.clientes:
                print('O cliente não consta na base de dados!')
            if self.conta.nro_conta not in self.contas:
                print('A conta não consta na base de dados!')


class Conta(ABC):
    def __init__(self, agencia, nro_conta, saldo):
        self.agencia = agencia
        self.nro_conta = nro_conta
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f'Sucesso! O saldo após o deposito é de R${self.saldo}.')

    @abstractmethod
    def sacar():
        pass


class ContaCorrente(Conta):
    # Contas corrente por padrão pode sacar 1k mesmo com saldo zerado
    def __init__(self, agencia, nro_conta, saldo, limite=1000):
        super().__init__(agencia, nro_conta, saldo)
        self.limite = limite

    def sacar(self, valor):
        if valor > (self.limite + self.saldo):
            print(f'R${valor} ultrapassa o saldo disponivel de {self.saldo}!')
            return

        self.saldo -= valor
        print(f'Sucesso! O saldo após o saque é de R${self.saldo}.')


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if valor > self.saldo:
            print(f'R${valor} ultrapassa o saldo disponivel de {self.saldo}!')
            return

        self.saldo -= valor
        print(f'Sucesso! O saldo após o saque é de R${self.saldo}.')
