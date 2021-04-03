"""
1. No QTDesigner constrói a interface e salva no projeto.(Nesse ex é o design.ui)
2. Abre o terminal e executa o comando abaixo para converter o arquivo de design para .py:
    "pyuic5 design.ui -o design.py" - > pyuic5 nome_da_origem -o saída
"""
import sys
from design import *   # Importando o conteúdo do arquivo de design .py para o main
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWidgets import QFileDialog   # Para o botão de escolher o arquivo
from PyQt5.QtGui import QPixmap   # Será o responsável por manipular a imagem


class RedimensionarImagem(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)   # Rodando o método setupUi da Ui_MainWindow do design.py
        self.btnEscolherArquivo.clicked.connect(self.abrir_imagem)   # Definindo função do botão
        self.btnRedimensionar.clicked.connect(self.redimensionar)
        self.btnSalvar.clicked.connect(self.salvar)

    def abrir_imagem(self):
        imagem, _ = QFileDialog.getOpenFileName(   # Vai retornar o nome do arquivo selecionado na janela
            self.centralwidget,   # Pai da caixa de dialogo
            'Abrir imagem',   # Título da janela
            r'\ '.strip(),   # Caminho inicial da janela
            # options=QFileDialog.DontUseNativeDialog   # Caso ocorra algum problema com o explorador padrão
        )

        self.inputAbrirArquivo.setText(imagem)   # Definindo o texto do input para o dir da img
        self.original_img = QPixmap(imagem)   # Criando uma imagem original para não alterar a selecionada
        self.labelImg.setPixmap(self.original_img)   # Mostrando a imagem na label

        # Quando uma imagem for carregada os inputs de altura e largura receberão esses valores da imagem por padrão
        self.inputLargura.setText(str(self.original_img.width()))
        self.inputAltura.setText(str(self.original_img.height()))

    def redimensionar(self):
        largura = int(self.inputLargura.text())   # Largura recebe o texto do input de largura
        self.nova_imagem = self.original_img.scaledToWidth(largura)   # Calcula a a altura de acordo com a largura
        self.labelImg.setPixmap(self.nova_imagem)

        # Pegando novamente a altura e largura para os inputs
        self.inputLargura.setText(str(self.nova_imagem.width()))
        self.inputAltura.setText(str(self.nova_imagem.height()))

    def salvar(self):
        imagem, _ = QFileDialog.getSaveFileName(
            self.centralwidget,  # Pai da caixa de dialogo
            'Salvar imagem',  # Título da janela
            r'\ '.strip(),  # Caminho inicial da janela
            # options=QFileDialog.DontUseNativeDialog   # Caso ocorra algum problema com o explorador padrão
        )

        try:
            self.nova_imagem.save(imagem, 'PNG')
        except Exception as e:
            pass


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    redimensionar_imagem = RedimensionarImagem()   # Instanciando a classe
    redimensionar_imagem.show()   # Mostrando a classe
    qt.exec_()
