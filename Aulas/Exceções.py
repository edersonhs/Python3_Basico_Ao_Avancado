try:
    a = {}
    # print(a[4])
except NameError as erro:   # Semelhante a passar a descrição do erro para a variavel 'erro'
    print('Erro:', erro)
except (IndexError, KeyError) as erro:   # IndexError = erro de indice de uma lista / KeyError chave de dicionario invalida
    print('Erro de indice ou chave.')
except Exception as erro:   # Inclui todas as possiveis excessões
    print('Ocorreu um erro inesperado.')
else:   # Caso não dispare nenhuma exceção no try, o else será executado
    print('Código executado com sucesso!')
finally:   # Sempre será executado, mesmo se houver exceção
    print('Finalmente')
