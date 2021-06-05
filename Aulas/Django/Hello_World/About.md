# Django

## Instalar Django
* Iniciar projeto com virtualenv
* pip install django

## Criar projeto no Django
* django-admin startproject nome-do-projeto .

O comando acima irá criar um projeto Django chamado “nome-do-projeto” com a seguinte estrutura de pastas:

Basicamente, há quatro arquivos no projeto criado, onde a função de cada um deles pode ser vista abaixo:

**settings.py:** Arquivo para armazenar as configurações gerais do projeto, como os pacotes a serem utilizados, configurações de bancos de dados, localização de arquivos estáticos, etc.
**urls.py:** Arquivo para armazenar as rotas que serão utilizadas no projeto. Este arquivo armazenará as rotas do projeto em geral, é recomendável que cada aplicação do projeto possua um arquivo de rotas específico.
**wsgi.py:** Interface simples e universal para troca de informações entre servidores web e aplicações criadas com Python.
**manage.py:** Arquivo responsável por gerenciar o projeto como um todo. É, basicamente, um CLI para projetos Django.

## Iniciar servidor local Django
python manage.py runserver

## Criar APP
 Um projeto Django é dividido em diversas apps. Cada app é responsável por um módulo da aplicação e permite uma maior organização e legibilidade do projeto.

* python manage.py startapp nome_da_app

##### Ao executar o comando acima, uma série de arquivos é criada, estes arquivos são:

* **Diretório migrations:** Diretório responsável por armazenar os arquivos de migração para o banco de dados de uma aplicação Django.
* **admin.py:** Arquivo responsável por definir os models a serem utilizados no módulo administrativo do Django.
* **apps.py:** Arquivo responsável pela configuração da app do projeto Django.
* **models.py:** Arquivo responsável por definir os modelos da aplicação. Basicamente, um modelo é a representação das tabelas a serem criadas no banco de dados.
* **tests.py:** Arquivo responsável por definir as regras de testes da aplicação.
* **views.py:** Arquivo responsável por definir as regras de negócio do app.

Ao criar a aplicação, precisamos registrá-la no arquivo settings.py do projeto. Isso fará com que o projeto Django saiba que essa app faz parte do projeto e que ele pode gerenciá-la. Para fazer isso, no arquivo settings.py, adicionamos o nome_da_app.apps.nome-da-classe-do-app.py-do-app no array INSTALLED_APPS.
