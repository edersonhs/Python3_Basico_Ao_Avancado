"""
PyQT é u m toolkit desenvolvido em C++ utilizado por vários programas para
criação de aplicações GUI (Interface Gráfica). Também inclui diversas
funcionalidades, como: acesso a base de dados, threads, comunicação de rede,
etc...

pip install pyqt5
"""

# Criando uma janela:
import sys   # Para inicialização
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication   # Para executar
from PyQt5.QtWidgets import QPushButton   # Para adicionar o botão
from PyQt5.QtWidgets import QWidget   # Widget central
from PyQt5.QtWidgets import QGridLayout


class App(QMainWindow):   # Herdando de QMainWindow
    def __init__(self, parent=None):
        super().__init__(parent)   # Construtor da QMainWindow
        self.cw = QWidget()   # Instanciando o central widget
        self.grid = QGridLayout(self.cw)

        # Criando o botão
        self.btn = QPushButton('Texto do botão')

        # Definindo o estilo do texto do botão por css
        self.btn.setStyleSheet('font-size: 20px;')

        # Adicionando o botão no grid
        self.grid.addWidget(self.btn, 0, 0, 1, 1)
        """
        GRID = Grade
        Linhas, colunas, qtd de linhas que o btn vai ocupar,
        qtd colunas que o btn vai ocupar
        """

        # Definindo uma operação para quando o botão é clicado
        self.btn.clicked.connect(lambda: print('Ola mundo!'))
        """
        Pega o evento de click e executa um método da classe. Neste
        caso esta executando uma função lambda que vai printar 'Ola mundo!'
        no terminal toda vez que o botão for clicado, como exemplo. 
        
        Exemplo de código com método de classe:
        self.btn.clicked.connect(self.teste)
        """

        self.setCentralWidget(self.cw)

    def teste(self):
        print('Alguma coisa...')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = App()
    app.show()
    qt.exec_()
