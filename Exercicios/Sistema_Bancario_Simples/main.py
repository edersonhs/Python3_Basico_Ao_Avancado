from metodos.conta import Banco, ContaCorrente, ContaPoupanca
from metodos.pessoa import Cliente

cliente1 = Banco(Cliente('João', 28), ContaPoupanca(101, 1518, 3500))
print(
    f'Cliente: {cliente1.cliente.nome}, Idade: {cliente1.cliente.idade} anos')
cliente1.conta.sacar(3400)
cliente1.conta.depositar(1200)
cliente1.conta.sacar(1400)   # Teste com valor acima do saldo disponivel

print('\n========================\n')

cliente2 = Banco(
    Cliente('Luiz', 49),
    ContaCorrente(101, 1010, 20000, limite=10000)
)

print(
    f'Cliente: {cliente2.cliente.nome}, Idade: {cliente2.cliente.idade} anos')

cliente2.conta.sacar(1000)
cliente2.conta.depositar(1000)
cliente2.conta.sacar(30000)
