"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra. Banco
tem clientes e contas.

Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
"""
from banco import Banco
from cliente import Cliente

banco = Banco()

cliente1 = Cliente('Vitor', 21)
cliente2 = Cliente('Maria', 43)

cliente1.inserir_conta(1111, 159657, 0)   # Conta Poupança
cliente2.inserir_conta(2222, 159658, 0, tipo=1, limite=5000)   # Conta corrente

banco.inserir_cliente(cliente1)
banco.inserir_conta(cliente1.conta)

if banco.autentica(cliente1):
    cliente1.conta.detalhes()   # Agência: 1111 Conta: 159657 Saldo: 0
    cliente1.conta.depositar(3000)   # Agência: 1111 Conta: 159657 Saldo: 3000
    cliente1.conta.sacar(3500)   # O valor ultrapassa o saldo disponivel!
    cliente1.conta.sacar(2500)    # Agência: 1111 Conta: 159657 Saldo: 500
else:
    print('Cliente não autenticado')

print('\n==============================================\n')

banco.inserir_cliente(cliente2)
banco.inserir_conta(cliente2.conta)

if banco.autentica(cliente2):
    cliente2.conta.detalhes()   # Agência: 2222 Conta: 159658 Saldo: 0
    cliente2.conta.depositar(2000)   # Agência: 2222 Conta: 159658 Saldo: 2000
    cliente2.conta.sacar(3500)   # Agência: 2222 Conta: 159658 Saldo: -1500
    cliente2.conta.sacar(4600)    # O valor ultrapassa o saldo disponivel!
else:
    print('Cliente não autenticado')
