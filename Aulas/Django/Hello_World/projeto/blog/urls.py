from django.urls import path
from . import views   # ponto referencia a pasta raiz do arquivo, no caso a blogs

# urls internas do app. exemplo /blog/posts
urlpatterns = [
    path('', views.index)   # Quando a string estiver vazia o url continuará
                            # sendo "blog" e vai executar o que foi informado.
]
