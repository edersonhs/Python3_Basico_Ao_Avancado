"""
Comma Separated Values - CSV (Valores separados por vírgula)
É um formato de dados muito usado em tabelas (Excel, Google Sheets), base de
dados, clientes de e-mail, etc...

Cada linha do csv representa uma linha da tabela e cada informação separada
por virgula representa uma tabela da coluna da tabela.
"""
import csv

caminho_csv = r'Aulas\Módulos_Python\CSV-Comma_Separated_Values\clientes.csv'

# ########################### Lendo arquivo CSV ############################
with open(caminho_csv, 'r', encoding='utf8') as arquivo:
    # Vai retornar um gerador, ou seja, só vai ser possivel acessar os dados
    # dentro deste with.
    dados = csv.reader(arquivo)   # Lendo o arquivo csv e inserindo em dados
    # Dados será um iterador e cada linha do csv será uma lista com os
    # elementos separados por virgula.

    # next(dados)   # Caso seja necessario pular o cabeçalho

    for dado in dados:
        print(dado)

print()

# Retornando o csv como dicionario
with open(caminho_csv, 'r', encoding='utf8') as arquivo:
    # Vai retornar um gerador, ou seja, só vai ser possivel acessar os dados
    # dentro deste with.
    dados = csv.DictReader(arquivo)   # Retorna cada linha como um dicionario.

    for dado in dados:
        print(dado)

    # Exemplo de print dos nomes do dicionario através das chaves
    # for dado in dados:
    #     print(dado['Nome'], dado['Sobrenome'], dado['E-mail'])

print()

# ###################### Lendo arquivo CSV fora do with #######################
with open(caminho_csv, 'r', encoding='utf8') as arquivo:
    # Para que a variavel possa ser acessada fora do escopo do with, deve-se
    # utilizar de list comprehension
    dados = [x for x in csv.DictReader(arquivo)]
    # Vai retornar uma lista, com o dicionario de cada linha do arquivo csv

# ####### Convertendo do python para csv e gravando em um arquivo #############
with open('clientes2.csv', 'w', encoding='utf8') as arquivo:
    escreve = csv.writer(   # Configurando o objeto de escrita no arquivo csv
        arquivo,   # Arquivo onde os dados serão escritos
        delimiter=',',   # Definindo o delimitador que ficará entre os dados
        # Definindo o caractere de aspas do arquivo para evitar possiveis
        # problemas (Opcional)
        quotechar='"',
        # Definindo que todos os dados sejam delimitados por aspas, como uma
        # string. (Opcional)
        quoting=csv.QUOTE_ALL
    )

    # Montando a primeira linha (Onde seria os titulos da tabela)
    chaves = dados[0].keys()   # Pegando todas as chaves do dicionario
    chaves = list(chaves)   # Convertendo para uma lista
    escreve.writerow(   # Escreve linha no arquivo
        [   # Dados a serem inseridos na primeira linha do arquivo csv
            chaves[0],   # Titulo "Nome"
            chaves[1],   # Titulo "Sobrenome"
            chaves[2],   # Titulo "E-mail"
            chaves[3]    # Titulo "Telefone"
        ]
    )

    for dado in dados:
        escreve.writerow(   # Escreve linha no arquivo
            [   # Dados a serem inseridos na linha do arquivo csv
                dado['Nome'],
                dado['Sobrenome'],
                dado['E-mail'],
                dado['Telefone']
            ]
        )

"""
util:
PARA IMPORTAÇÃO LEGIVEL DO CSV NO EXCEL:

O arquivo CSV é salvo com apenas "uma coluna". Digo isso entre aspas
pois na verdade ele está sim separado em mais de uma coluna, só para
entendimento CSV significa Comma Separate Values, ou seja, Valores
Separados por Virgula.

Sendo assim, a vírgula é um delimitador desse tipo de arquivo e a coluna é
separada por virgula, para fazer com que o excel separe as colunas por
virgulas tem várias maneiras, a mais fácil (para mim) é:

1 - Abra um arquivo no Excel e clique em “Dados”. Em seguida selecione a opção
“De Texto”;

2 - Selecione o arquivo CSV desejado e clique em “Importar”;

3 - Depois disso, selecione a opção “Delimitado”. Em seguida, clique em na
opção “Avançar”;

4 - Para que a importação seja feita com sucesso é preciso atentar para um
detalhe importante. Nesta etapa, é imprescindível selecionar a opção “Vírgula”
antes de clicar em “Avançar”.

Com isso, já é possível perceber na opção “Visualização dos Dados” que as
informações começam a aparecer de forma legível.;

5 - Na tela seguinte é disponibilizado um passo considerado opcional. Isso
porque alguns arquivos CSV transformam vírgulas ( , ) em pontos ( . );

Pronto, agora você tem eles separados em colunas no excel.
"""
