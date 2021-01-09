class Ip:
    def __init__(self, ip, cidr):
        self._ip = ip.split('.')
        self._cidr = cidr

    @property
    def ip(self):
        return self._ip

    @property
    def cidr(self):
        return self._cidr

    def validator(self, model=1):
        if model == 1:
            for group in self.ip:
                if not group.isdigit() or len(group) > 3:
                    return False
                return True
        else:   # CIDR
            if int(self.cidr) > 32 or not self.cidr.isdigit():
                return False
            return True

    def binary_converter(self, model=1):
        values = (128, 64, 32, 16, 8, 4, 2, 1)
        binary_ip = []

        if model == 1:   # IP
            if self.validator():
                for group in self.ip:
                    binary = []
                    count = 0

                    for number in values:
                        if number <= int(group) and (count+number) <= int(group):
                            binary.append(1)
                            count += number
                        else:
                            binary.append(0)
                    binary_ip.append(binary[:])

                return binary_ip
        else:   # CIDR
            if self.validator(2):
                binary_cidr = []
                for count in range(int(self.cidr)):
                    binary_cidr.append(1)

                while len(binary_cidr) < 32:
                    binary_cidr.append(0)

            return binary_cidr

    def range_ip(self):
        aux = ''
        for number in self.binary_converter(2):
            aux += str(number)
        valid_ip = (2 ** aux.count('0')) - 2
        return valid_ip

    def netmask(self):
        values = (128, 64, 32, 16, 8, 4, 2, 1)
        binary_netmask = []
        netmask = []
        aux = []
        count = 0

        # Agrupando
        for element in self.binary_converter(2):
            if count < 8:
                aux.append(element)
                count += 1
            if count == 8:
                binary_netmask.append(aux[:])
                aux.clear()
                count = 0

        for group in binary_netmask:
            mask = 0
            for i in range(8):
                if group[i] == 1:
                    mask += values[i]
            netmask.append([mask])

        return netmask

    def details(self):
        print(f'IP/Rede: '
              f'{self.ip[0]}.{self.ip[1]}.{self.ip[2]}.{self.ip[3]}/{self.cidr}')
        print(f'Prefixo CIDR: /{self.cidr}')
        print(f'Mascara de sub-rede: {self.netmask()}')
        print(f'Total de IPs: {self.range_ip() + 2}')
        print(f'Total de IPs para uso: {self.range_ip()}')
        # print(f'IP Binario: {self.binary_converter()}')
        # print(f'Representação binaria da rede: {self.binary_converter(2)}')


ip = Ip('10.20.12.45', '26')
ip.details()
