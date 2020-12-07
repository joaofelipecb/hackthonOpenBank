import struct_

class BanficoAccountValid (struct_.BanficoAccount):
    def __init__(self, accountId, nickname):
        super().__init__(accountId, nickname)
