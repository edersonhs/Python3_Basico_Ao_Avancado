class LogMixin:   # Mixin Class
    """
    Uma classe Mixin não esta relacionada com as outras classes e não faz
    parte da hierarquia. Tem como objetivo conter métodos para serem
    utilizados por outras classes.
    """
    @staticmethod   # O método não precisa saber da instancia em nenhum momento
    def write(msg):
        with open('log.log', 'a+') as f:
            f.write(msg)
            f.write('\n')

    def log_info(self, msg):
        self.write(f'INFO: {msg}')

    def log_error(self, msg):
        self.write(f'ERROR: {msg}')


class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    def ligar(self):
        if self._ligado:
            return
        self._ligado = True

    def desligar(self):
        if not self._ligado:
            return
        self._ligado = False


# Herda a classe mãe (Sempre a classe mãe primeiro) e depois a classes mixin
class Smartphone(Eletronico, LogMixin):
    def __init__(self, nome):
        super().__init__(nome)
        self._conectado = False

    def conectar(self):
        if not self._ligado:
            info = f'{self._nome} não esta ligado!'
            print(info)
            self.log_info(info)
            return

        if self._conectado:
            error = f'{self._nome} já esta conectado!'
            print(error)
            self.log_error(error)
            return

        info = f'{self._nome} está conectado!'
        print(info)
        self.log_info(info)
        self._conectado = True

    def desconectar(self):
        if not self._conectado:
            error = f'{self._nome} não esta conectado!'
            print(error)
            self.log_error(error)
            return

        info = f'{self._nome} foi desconectado com sucesso!'
        print(info)
        self.log_info(info)
        self._conectado = False


smartphone = Smartphone('Pocophone F1')
smartphone.conectar()   # Pocophone F1 não esta ligado!
smartphone.desligar()
smartphone.ligar()
smartphone.conectar()   # Pocophone F1 está conectado!
smartphone.conectar()
smartphone.desligar()
smartphone.conectar()
smartphone.desconectar()
