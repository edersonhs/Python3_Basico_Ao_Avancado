class Banco:
    def __init__(self):
        self.agencias = [1111, 2222, 3333]
        self.contas = []
        self.clientes = []

    def inserir_conta(self, conta):
        self.contas.append(conta)

    def inserir_cliente(self, cliente):
        self.clientes.append(cliente)

    def autentica(self, cliente):
        if cliente.conta.agencia not in self.agencias:
            return False
        if cliente not in self.clientes:
            return False
        if cliente.conta not in self.contas:
            return False

        return True
