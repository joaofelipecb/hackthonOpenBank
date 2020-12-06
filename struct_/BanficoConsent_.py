class BanficoConsent:
    def __init__(self, banficoAuth, consentId):
        self.__banficoAuth = banficoAuth;
        self.__consentId = consentId;
        
    @property
    def banficoAuth(self):
        return self.__banficoAuth
        
    @property
    def consentId(self):
        return self.__consentId
