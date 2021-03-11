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


class App(QMainWindow):   # Herdando de QMainWindow
    def __init__(self, parent=None):
        super().__init__(parent)   # Construtor da QMainWindow


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = App()
    app.show()
    qt.exec_()
