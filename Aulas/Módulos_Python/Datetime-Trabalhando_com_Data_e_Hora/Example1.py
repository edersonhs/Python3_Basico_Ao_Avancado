"""
Documentação: https://docs.python.org/3/library/datetime.html
"""
from datetime import datetime

"""
Timedelta = Duração/Intervalo de tempo
"""

# Instanciando uma data
data = datetime(2021, 1, 10, 10, 53, 20)  # Hora/minuto/segundo são opcionais
"""
datetime(Ano, mês, dia, hora, minuto e segundo)
"""
print(data)   # 2021-01-10 10:53:20 padrão americano

# Formatando a data manualmente com o metodo strftime da instancia
print(data.strftime('%d/%m/%Y %H:%M:%S'))   # 10/01/2021 10:53:20
"""
As diretivas (%d, %m, %Y, %H, %M, %S...) podem ser encontradas na documentação
oficial do modulo.
"""

# Normalmente os dados de data e hora não são recebidos divididos por partes,
# por isto usamos a função strptime() para tornar a string em um objeto de data
data1 = datetime.strptime('20/04/2019', '%d/%m/%Y')
"""
 # strptime('', '') recebe uma string e um formato.
"""
print(data1)   # 2019-04-20 00:00:00 Segundos zerados por não serem definidos

"""
Timestamp()   # Contagem de segundos desde 01/01/1970 até a data definida na
instancia.

Com um timestamp, podemos fazer a convesão do mesmo para a data
atual.
"""
# print(data1.timestamp())   # 1555729200.0

# Convertendo o timestamp para data
data3 = datetime.fromtimestamp(1555729200.0)
print(data3)
