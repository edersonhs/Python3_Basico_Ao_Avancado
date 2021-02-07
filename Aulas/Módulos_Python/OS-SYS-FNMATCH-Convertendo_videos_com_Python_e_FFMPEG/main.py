"""
SCRIPT PARA AUTOMATIZAR CONVERSÃO DE VIDEO
-----------------------------------------------------------------------------
FFMPEG - Um dos melhores conversores de video. (não possui interface gráfica)

Comando exemplo FFMPEG:
ffmpeg -i "ENTRADA" -i "LEGENDA" -c:v libx264 -crf 23 - preset ultrafast
-c:a aac -b:a 320k -c:s srt -map v:0 -map a -map 1:0 -ss 00:00:00 -to 00:00:10
"SAIDA"

Documentação ffmpeg - https://ffmpeg.org/documentation.html
Download ffmpeg - https://ffmpeg.org/download.html

Baixar o ffmpeg e deixar o .exe em ffmpeg/ffmpeg.exe
"""
import os
import fnmatch   # verificar a extensão dos arquivos
import sys   # para conferir o sistema operacional

if sys.platform == 'linux':
    comando_ffmpeg = 'ffmpeg'
else:
    comando_ffmpeg = r'Aulas\Módulos_Python\OS-SYS-FNMATCH-' \
        r'Convertendo_videos_com_Python_e_FFMPEG\ffmpeg\ffmpeg.exe'

codec_video = '-c:v libx264'   # H.264
# CRF - "Controle de qualidade" entre 15 e 28, sendo que 18 é a melhor
# qualidade e 28 a pior.
crf = '-crf 23'
preset = '-preset ultrafast'
codec_audio = '-c:a aac'
bitrate_audio = '-b:a 320k'
# debug = ''   # Para converter do inicio ao fim
debug = '-ss 00:00:00 -to 00:00:15'   # Tempo de video a ser convertido

caminho_origem = r'C:\Users\eders\OneDrive\Desktop\Videos'
caminho_destino = r'C:\Users\eders\OneDrive\Desktop\Saída\ '.strip()

for raiz, pastas, arquivos in os.walk(caminho_origem):
    for arquivo in arquivos:
        # Se não encontrar .mp4 no arquivo vai para o proximo arquivo do for
        if not fnmatch.fnmatch(arquivo, '*.mp4'):
            continue

        caminho_completo = os.path.join(raiz, arquivo)
        # splitext divide a string quando encontra o ponto
        nome_arquivo, extensao_arquivo = os.path.splitext(caminho_completo)
        caminho_legenda = nome_arquivo + '.srt'

        if os.path.isfile(caminho_legenda):   # Verificando se a legenda existe
            input_legenda = f'-i "{caminho_legenda}"'
            # Mapeando legenda - video e audio tem de ser mapeados também
            map_legenda = '-c:s srt -map v:0 -map a -map 1:0'
        else:
            input_legenda = ''
            map_legenda = ''

        # Sobrescrevendo as variaveis de arquivo anteriores
        nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)

        arquivo_saida = f'{caminho_destino}' + \
            f'{nome_arquivo}_NOVO{extensao_arquivo}'

        comando = f'{comando_ffmpeg} -i "{caminho_completo}" {input_legenda} '\
            f'{codec_video} {crf} {preset} {codec_audio} {bitrate_audio} '\
            f'{debug} {map_legenda} "{arquivo_saida}"'

        os.system(comando)   # Executando o comando no sistema
