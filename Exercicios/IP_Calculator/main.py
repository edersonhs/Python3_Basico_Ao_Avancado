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

    def decimal_converter(self, binary_address):
        values = (128, 64, 32, 16, 8, 4, 2, 1)
        decimal_address = []

        for group in binary_address:
            address_group = 0
            for i in range(8):
                if group[i] == 1:
                    address_group += values[i]
            decimal_address.append(str(address_group))

        return decimal_address

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
            netmask.append(str(mask))

        return netmask

    def broadcast(self):
        binary_ip = self.binary_converter()
        broadcast = []
        aux = []
        count = 0

        for group in binary_ip:
            for number in group:
                if count < int(self.cidr):
                    aux.append(number)
                    count += 1
                else:
                    aux.append(1)
            broadcast.append(aux[:])
            aux.clear()

        return broadcast

    def network_ip(self):
        binary_ip = self.binary_converter()
        broadcast = []
        aux = []
        count = 0

        for group in binary_ip:
            for number in group:
                if count < int(self.cidr):
                    aux.append(number)
                    count += 1
                else:
                    aux.append(0)
            broadcast.append(aux[:])
            aux.clear()

        return broadcast

    def details(self):
        print(f'IP/Rede: {".".join(self.ip)}/{self.cidr}')
        print(f'Prefixo CIDR: /{self.cidr}')
        # print(f'Mascara de sub-rede: {self.netmask()}')
        print(f'Mascara de sub-rede: {".".join(self.netmask())}')
        print(f'Total de IPs: {self.range_ip() + 2}')
        print(f'Total de IPs para uso: {self.range_ip()}')
        print(
            f'IP de Broadcast: {".".join(self.decimal_converter(self.broadcast()))}')
        print(
            f'IP da Rede: {".".join(self.decimal_converter(self.network_ip()))}')


ip = Ip('10.20.12.45', '26')
ip.details()
