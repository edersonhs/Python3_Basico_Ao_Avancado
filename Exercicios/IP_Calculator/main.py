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

    def validator(self, ip):
        for group in self.ip:
            if not group.isdigit() or len(group) > 3:
                return False
        return True

    def details(self):
        binary_ip = BinaryIp(self.ip, self.cidr).conversor(self.ip)
        print(binary_ip)


class BinaryIp(Ip):
    def __init__(self, ip, cidr):
        self._ip = ip
        self._cidr = cidr

    def conversor(self, ip):
        values = (128, 64, 32, 16, 8, 4, 2, 1)
        binary_ip = []

        if self.validator(ip):
            for group in ip:
                binary = []
                count = 0

                for number in values:
                    if number <= int(group) and (count + number) <= int(group):
                        binary.append(1)
                        count += number
                    else:
                        binary.append(0)
                binary_ip.append(binary[:])

            return binary_ip


ip = Ip('10.20.12.45', '26')
# print(ip.ip)
ip.details()
