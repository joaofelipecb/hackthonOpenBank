class BanficoAccount:
    def __init__(self, accountId, nickname):
        self.__accountId = accountId
        self.__nickname = nickname
        
    @property
    def accountId(self):
        return self.__accountId

    @property
    def nickname(self):
        return self.__nickname
        