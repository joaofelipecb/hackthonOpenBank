class BanficoAuth:
    def __init__(self, client_id, client_secret, bearer=None):
        self.__clientId = client_id;
        self.__clientSecret = client_secret;
        self.__bearer = bearer
        
    @property
    def clientId(self):
        return self.__clientId
        
    @property
    def clientSecret(self):
        return self.__clientSecret

