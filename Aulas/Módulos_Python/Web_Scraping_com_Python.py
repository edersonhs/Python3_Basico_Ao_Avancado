"""
Web Scraping
A coleta de dados web, ou raspagem web, é uma forma de mineração que permite a
extração de dados de sites da web convertendo-os em informação estruturada para
posterior análise.

Requisitos:
pip install requests
pip install beautifulsoup4
"""
import requests   # Acessar o site e pegar os dados
from bs4 import BeautifulSoup   # Manipular o html dentro do Python

url = 'https://pt.stackoverflow.com/questions/tagged/python'
response = requests.get(url)
# print(response.text)   # Para visualizar o html recebido

html = BeautifulSoup(response.text, 'html.parser')   # Analisando html

# Filtrando apenas a classe question summary do html
for pergunta in html.select('.question-summary'):
    titulo = pergunta.select_one('.question-hyperlink')
    data = pergunta.select_one('.relativetime')
    votos = pergunta.select_one('.vote-count-post strong')

    print()
    print(titulo.text)
    print(data.text, f'Votos: {votos.text}', sep='\t\t\t')
