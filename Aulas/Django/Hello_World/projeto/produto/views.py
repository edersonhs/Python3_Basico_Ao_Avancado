from django.shortcuts import render


def metodo(request):
    # O django vai buscas a render por padrão na pasta template, por isso ela não precisa
    # ser especificada.
    return render(request, 'produto/index.html')
