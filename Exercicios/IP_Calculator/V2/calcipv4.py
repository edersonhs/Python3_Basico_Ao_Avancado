import re   # Expressão Regular


class CalcIPv4:
    """
    Faz o cálculo de redes IPv4

    Modo de uso 1:
    calc_ipv4 = CalcIPv4(ip='192.168.0.128', prefixo=10)

    Modo de uso 2:
    calc_ipv4 = CalcIPv4(ip='192.168.0.128', mascara='255.255.255.0')
    """

    def __init__(self, ip, mascara=None, cidr=None):
        self.ip = ip
        self.mascara = mascara
        self.cidr = cidr

        if mascara is None and cidr is None:
            raise ValueError('É obrigatorio o envio de máscara ou cidr')

        if mascara and cidr:   # Verifica se recebeu os dois parametros
            raise ValueError('É necessario máscara ou cidr, não ambos.')

        self._set_broadcast()
        self._set_rede()

    @property
    def rede(self):
        return self._rede

    @property
    def broadcast(self):
        return self._broadcast

    @property
    def numero_ips(self):
        return self._get_numero_ips()

    @property
    def ip(self):
        return self._ip

    @property
    def mascara(self):
        return self._mascara

    @property
    def cidr(self):
        if self._cidr is None:
            return

        return self._cidr

    @ip.setter
    def ip(self, value):
        if not self._valida_ip(value):
            raise ValueError('IP inválido.')

        self._ip = value
        self._ip_bin = self._ip_to_bin(value)

    @mascara.setter
    def mascara(self, value):
        if not value:   # Se value estiver vazio, True
            return

        if not self._valida_ip(value):
            raise ValueError('Máscara inválida.')

        self._mascara = value
        self._mascara_bin = self._ip_to_bin(value)

        # Se o atributo "prefixo" não existir na instancia, cria-o
        if not hasattr(self, 'cidr'):
            self.cidr = self._mascara_bin.count('1')

    @cidr.setter
    def cidr(self, value):
        if value is None:
            return

        try:
            value = int(value)
        except:
            raise ValueError('Prefixo precisa ser um inteiro.')

        if value > 32 or value < 0:
            raise TypeError('Prefixo precisa ter 32Bits')

        self._cidr = value
        # formata o conteudo a esquerda completando o espaços em branco com 0
        self._mascara_bin = (value * '1').ljust(32, '0')

        if not hasattr(self, 'mascara'):
            self.mascara = self._bin_to_ip(self._mascara_bin)

    @staticmethod
    def _valida_ip(ip):
        """
        regexp: Regular Expression / Expressão Regular
        """
        regexp = re.compile(
            r'^([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3})$'
        )

        if regexp.search(ip):
            return True

    @staticmethod
    def _ip_to_bin(ip):
        blocos = ip.split('.')
        blocos_bin = [bin(int(bloco))[2:].zfill(8) for bloco in blocos]
        blocos_bin_str = ''.join(blocos_bin)
        qtd_bits = len(blocos_bin)

        if qtd_bits > 32:
            raise ValueError('IP ou máscara tem mais que 32 bits.')

        return blocos_bin_str

    @staticmethod
    def _bin_to_ip(ip):
        n = 8
        blocos = [str(int(ip[i:n + i], 2)) for i in range(0, 32, n)]
        return '.'.join(blocos)

    def _set_broadcast(self):
        host_bits = 32 - self.cidr
        self._broadcast_bin = self._ip_bin[:self.cidr] + (host_bits * '1')
        self._broadcast = self._bin_to_ip(self._broadcast_bin)

    def _set_rede(self):
        host_bits = 32 - self.cidr
        self._rede_bin = self._ip_bin[:self.cidr] + (host_bits * '0')
        self._rede = self._bin_to_ip(self._rede_bin)

    def _get_numero_ips(self):
        return 2 ** (32 - self.cidr)
