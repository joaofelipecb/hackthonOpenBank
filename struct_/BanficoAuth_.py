class BanficoAuth:
    def __init__(self, clientId, clientSecret, bearer=None):
        self.__clientId = clientId;
        self.__clientSecret = clientSecret;
        self.__bearer = bearer
        
    @property
    def clientId(self):
        return self.__clientId
        
    @property
    def clientSecret(self):
        return self.__clientSecret

    @property
    def bearer(self):
        return self.__bearer
