import struct_

class BanficoAuthValid (struct_.BanficoAuth):
    def __init__(self, clientId, clientSecret, bearer):
        super().__init__(clientId, clientSecret, bearer)
