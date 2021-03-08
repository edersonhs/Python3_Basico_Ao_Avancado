"""
Pillow - Módulo python com diversas funções para manipular imagens
"""
import os
from PIL import Image   # Importando o Pillow


def main(main_images_folder, new_width=800):
    if not os.path.isdir(main_images_folder):   # Levantando exceção caso o dir não exista
        raise NotADirectoryError(f'{main_images_folder} não existe.')

    for root, dir, files in os.walk(main_images_folder):
        for file in files:
            file_full_path = os.path.join(root, file)   # Caminho completo
            file_name, extension = os.path.splitext(file)   # Retorna o nome do arquivo e a extensão

            converted_tag = '_CONVERTED'

            new_file = file_name + converted_tag + extension   # Montando o novo nome
            new_file_full_path = os.path.join(root, new_file)   # Caminho completo do novo arquivo

            if converted_tag in file_full_path:
                continue   # Se o arquivo já tiver a tag de convertido, será ignorado.

            img_pillow = Image.open(file_full_path)   # Abrindo e atribuindo a imagem com pillow

            # Pegando os dados da imagem (Velocidade do obturador, data, hora, localização, etc)
            exif = img_pillow.getexif()  # Retorna um dicionario com as tags
            # print(exif.get(36867))   # mostrando a data em que a foto foi tirada

            width, height = img_pillow.size   # Retorna largura e altura original da imagem
            new_height = round(new_width * height / width)
            """
            Calculando as novas medidas da imagem:
            new_width * height / width == new_height
            """

            new_image = img_pillow.resize(
                (new_width, new_height),
                Image.LANCZOS   # Redimensionando a img
            )

            try:
                new_image.save(
                    new_file_full_path,
                    optmize=True,
                    quality=70,   # De 1 a 100. (referencia: 70 reduz bastante  o tamanho mantendo uma boa qualidade)
                    exif=img_pillow.info['exif']  # Passando o exif original para a nova imagem
                )
            except Exception as e:   # Quando a imagem não tiver exif
                try:
                    new_image.save(
                        new_file_full_path,
                        optmize=True,
                        quality=70,  # De 1 a 100. (referencia: 70 reduz bastante  o tamanho mantendo uma boa qualidade)
                    )
                except:
                    raise RuntimeError(f'Could not convert "{file_full_path}".')

            print(f'{file_full_path} convertido com sucesso!')
            new_image.close()   # Fechando a nova imagem (o save provavelmente fecha também)
            img_pillow.close()   # Fechando a imagem


if __name__ == '__main__':
    main_images_folder = r'C:\Users\eders\OneDrive\Desktop\Pictures'
    main(main_images_folder, 640)
