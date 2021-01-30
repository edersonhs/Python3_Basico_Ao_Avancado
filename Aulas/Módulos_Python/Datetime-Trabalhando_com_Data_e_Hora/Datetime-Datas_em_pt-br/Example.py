from datetime import datetime
from locale import setlocale, LC_ALL   # Para deixar os dados em PT-BR
from calendar import mdays   # Retorna um lista com a qtd de dias de cada mês

setlocale(LC_ALL, 'pt_BR.utf-8')   # Definindo o local para setar o idioma.
"""
Quando a string vem vazia o setlocale tenta definir a "localização"
do sistema operacional.
"""

dt = datetime.now()   # Pegando a data atual
formatacao1 = dt.strftime('%A, %d de %B de %Y')   # Formatando data
formatacao2 = dt.strftime('%d/%m/%Y %H:%M:%S')   # Formatando data
print('Formatação 1:', formatacao1)   # sábado, 30 de janeiro de 2021
print('Formatação 2:', formatacao2)   # 30/01/2021 15:54:08

# Verificando qual o ultimo dia do mês atual
mes_atual = int(dt.strftime('%m'))
qtd_dias_mes = mdays[mes_atual]
"""
mdays é uma lista com a qtd de dias de todos os meses, ou seja, a posição 1 tem
a quantidade de dias de janeiro, posição dois a quantidade de dias de fevereiro
e assim por diante.

print de mdays: [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
"""
print('Mês', mes_atual, 'tem', mdays[mes_atual], 'dias.')
