"""
Relações entre classes em Python
"""

# 1 - Associação - Uma classe será relacionara-da com outra classe, entretanto nenhuma classe depende da outra para funcionar

from classes import Escritor, Caneta, MaquinaDeEscrever

# * Instanciando as classes...
escritor = Escritor('Joãozinho')
# print(escritor.nome)

caneta = Caneta('Bic')
# print(caneta.marca)

maquina = MaquinaDeEscrever()
# print(maquina)


# Associando as classes
escritor.ferramenta = caneta   # O atributo Ferramenta, da classe escritor, tornou-se uma instancia da classe caneta
escritor.ferramenta.escrever()   # Executando o metodo escrever da classe caneta atráves da instancia "ferramenta"

del escritor   # Apaga a instancia "escritor"

# print(escritor.nome)   # Dispara um erro, pois escritor não existe mais

# As outras classes instanciandas contiuam funcionando normalmente ser a instancia "escritor"...
print(caneta.marca)
maquina.escrever()