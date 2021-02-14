from string import Template   # A string class for supporting $-substitutions.
from datetime import datetime

# IMPORTAÇÕES PARA ENVIO DO EMAIL:
# Assunto da mensagem, remetente, destinatario, etc
from email.mime.multipart import MIMEMultipart
# Recebe o corpo do email, podendo ser texto(plain text) ou texto em html
from email.mime.text import MIMEText
# Recebe uma imagem para anexar ao email
from email.mime.image import MIMEImage
# Para conectar no servidor smtp do gmail e enviar a mensagem
import smtplib

meu_email = 'seu_email@gmail.com'
minha_senha = 'sua_senha'

# abrindo arquivo html
caminho_html = r'Aulas\Módulos_Python\String-Template\template.html'
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

# Configurando a mensagem
msg = MIMEMultipart()
msg['from'] = 'Traxr'   # Remetente
msg['to'] = meu_email   # Destinatario
msg['subject'] = 'Atenção: este é um e-mail de testes.'   # Assunto

corpo = MIMEText(corpo_msg, 'html')   # Configurando o corpo
msg.attach(corpo)   # passando o MIMEText para a msg

# Anexando uma imagem
# caminho_img = r'Aulas\Módulos_Python\Enviando_e-mails_com_python\imagem.jpg'
# with open(caminho_img, 'rb') as img:  # rb: Read Bytes
#     # Lendo os bytes da imagem e enviando para o MIMEImage
#     img = MIMEImage(img.read())
#     msg.attach(img)

# Configurando o smtp
"""
Caso ocorra erro de autenticacão no gmail:
Acesse https://myaccount.google.com/lesssecureapps
Habilite a opção de permitir less secure apps
"""
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    try:
        smtp.ehlo()   # Mensagem de hello para o servidor smtp do gmail
        smtp.starttls()   # Transport Layer Security
        smtp.login(meu_email, minha_senha)   # Email de envio
        smtp.send_message(msg)   # Enviando a mensagem
        print('E-mail enviado com sucesso!')
    except Exception as e:
        print('E-mail não enviado...')
        print(f'Erro: {e}')
