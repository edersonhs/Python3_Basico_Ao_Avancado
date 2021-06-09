# Incluindo arquivos parciais (Modularização)

* Arquivos com **_** na frente, por convenção são arquivos parciais, isso não é obrigatorio, mas é interessante utilizar.
* O diretorio dos arquivos parciais deve estar incluido no settings (Nesse caso é o 'DIRS': [path.join(BASE_DIR, 'templates')],)

```
Exemplos de include no codigo:
{% include 'parciais/_head.html' %}
{% include 'parciais/_nav.html'%}
```