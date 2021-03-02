"""
Documentação:
https://pythonhosted.org/PyPDF2/
Mais exemplos de uso:
http://www.blog.pythonlibrary.org/2018/06/07/an-intro-to-pypdf2/

pip install pypdf2   # virtualenv
pipenv install pypdf2   # pipenv
"""
import PyPDF2
import os

caminho_dos_pdfs = 'PDF'

"""
# Unindo dois PDFs em um único arquivo pdf
novo_pdf = PyPDF2.PdfFileMerger()   # Unir PDFs

for root, dirs, files in os.walk(caminho_dos_pdfs):
    for file in files:
        caminho_completo_arquivo = os.path.join(root, file)

        arquivo_pdf = open(caminho_completo_arquivo, 'rb')   # Abrindo o pdf em modo leitura de bytes
        novo_pdf.append(arquivo_pdf)

with open(f'{caminho_dos_pdfs}/novo_arquivo.pdf', 'wb') as meu_novo_pdf:   # Escrita de bytes
    novo_pdf.write(meu_novo_pdf)
"""

# Dividindo um PDF por pagina
with open(f'{caminho_dos_pdfs}/novo_arquivo.pdf', 'rb') as arquivo_pdf:   # Abrindo o pdf
    leitor = PyPDF2.PdfFileReader(arquivo_pdf)
    num_paginas = leitor.getNumPages()   # Pegando o número de paginas do pdf

    for num_pagina in range(num_paginas):
        escritor = PyPDF2.PdfFileWriter()
        pagina_atual = leitor.getPage(num_pagina)
        escritor.addPage(pagina_atual)

        with open(f'{caminho_dos_pdfs}/novo_arquivo_pag{num_pagina}.pdf', 'wb') as novo_pdf:
            escritor.write(novo_pdf)
