"""
Criar um template HTML e substituir alguns place holders para o nome do
cliente, data, etc para o envio de emails através do python
"""
from string import Template   # A string class for supporting $-substitutions.
from datetime import datetime

caminho_html = r'Aulas\Módulos_Python\String-Template\template.html'

# abrindo arquivo html
with open(caminho_html, 'r', encoding='utf-8') as html:
    # Template torná-se uma instancia de Template que serve para substituir os
    # place holders do html pelo conteudo desejado
    template = Template(html.read())
    # Pegando data atual e formatando para DD/MM/YYYY
    data_atual = datetime.now().strftime('%d/%m/%Y')
    # Substituindo os place holders do html para o conteudo desejado
    corpo_msg = template.substitute(nome='Ederson H. P. Sá', data=data_atual)
    """
    É importante destacar que caso exista mais algum place holder que não tenha
    sido definido no template.sustitute() uma excessão será disparada.

    Caso queira fazer a substituição de uma maneira segura, evitando que uma
    excessão seja disparada, pode-se utilizar o safe_substitute(). Desta forma
    caso exista algum place holder não especificado ele será simplesmente
    incluido na string com "$NomeDoPlaceHolder"
    """
    # corpo_msg = template.safe_substitute(nome='Ederson', data=data_atual)

print(corpo_msg)
