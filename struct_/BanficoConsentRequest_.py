class BanficoConsentRequest:
    def __init__(self, banficoAuth, financialId, consentId):
        self.__banficoAuth = banficoAuth;
        self.__financialId = financialId;
        self.__consentId = consentId;
        
    @property
    def banficoAuth(self):
        return self.__banficoAuth
        
    @property
    def financialId(self):
        return self.__financialId

    @property
    def consentId(self):
        return self.__consentId
