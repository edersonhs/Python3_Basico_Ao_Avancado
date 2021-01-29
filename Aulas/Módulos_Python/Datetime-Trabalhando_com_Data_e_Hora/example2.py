"""
Documentação: https://docs.python.org/3/library/datetime.html
"""
from datetime import datetime, timedelta

data = datetime.strptime('20/04/1987 20:00:00', '%d/%m/%Y %H:%M:%S')
# Somando + 5 dias e 59 segundos na data
data += timedelta(days=5, seconds=59)

print(data.strftime('%d/%m/%Y %H:%M:%S'))   # 25/04/1987 20:00:00

print()

"""
Com timedelta é possivel somar, subtrair, comparar datas e muito mais
"""
d1 = datetime.strptime('20/04/1987 20:00:00', '%d/%m/%Y %H:%M:%S')
d2 = datetime.strptime('25/04/1987 22:33:00', '%d/%m/%Y %H:%M:%S')
diferenca = d2 - d1   # retorna um "timedelta"
print(f'{diferenca} de diferença.')   # 5 days, 2:33:00
print(diferenca.total_seconds())   # somente o total de segundos de diferença
# print(diferenca.days)   # Apenas os dias de diferença entre as duas datas

# print(d1.time())   # Retorna apenas a hora de d1

# print(d2 > d1)   # True - a data2 é maior que a data1
