import os

# Caminho de onde a busca começara
caminho_procura = input('Digite um caminho: ')
termo_procura = input('Digite um termo de procura: ')


def formata_tamanho(tamanho):
    base = 1024
    kilo = base
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4
    peta = base ** 5

    if tamanho < kilo:
        texto = 'B'   # Byte
    elif tamanho < mega:
        tamanho /= kilo
        texto = 'K'   # KiloByte
    elif tamanho < giga:
        tamanho /= mega
        texto = 'M'   # MegaByte
    elif tamanho < tera:
        tamanho /= giga
        texto = 'G'   # GigaByte
    elif tamanho < peta:
        tamanho /= tera
        texto = 'T'   # TeraByte
    else:
        tamanho /= peta
        texto = 'P'   # PetaByte

    tamanho = round(tamanho, 2)   # Formatando tamanho para duas casa decimais
    return f'{tamanho}{texto}'.replace('.', ',')


contador = 0

for raiz, diretorios, arquivos in os.walk(caminho_procura):
    """
    raiz: pasta sendo verificada no momento
    diretorios: lista de diretorios que existe na raiz
    arquivos: lista de arquivos que existem na raiz
    """
    for arquivo in arquivos:
        if termo_procura in arquivo:
            try:
                contador += 1
                caminho_completo = os.path.join(raiz, arquivo)
                nome_arquivo, ext_arquivo = os.path.splitext(arquivo)
                tamanho = os.path.getsize(caminho_completo)   # Tamanho em Byte

                print()
                print('Encontrei o arquivo:', arquivo)
                print('Caminho:', caminho_completo)
                print('Nome:', nome_arquivo)
                print('Extensão:', ext_arquivo if ext_arquivo else None)
                print('Tamanho:', tamanho)
                print('Tamanho formatado:', formata_tamanho(tamanho))
            except PermissionError:
                print('Sem permissão neste arquivo.')
            except FileNotFoundError:
                print('Arquivo não encotrado.')
            except Exception as e:
                print('Erro desconhecido:', e)

print(F'\n{contador} arquivo(s) encontrado(s).')
