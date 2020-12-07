class BanficoConsent:
    def __init__(self, banficoAuth, banficoAuthConsent, financialId, consentId):
        self.__banficoAuth = banficoAuth;
        self.__banficoAuthConsent = banficoAuthConsent;
        self.__financialId = financialId;
        self.__consentId = consentId;
        
    @property
    def banficoAuth(self):
        return self.__banficoAuth
        
    @property
    def banficoAuthConsent(self):
        return self.__banficoAuthConsent
        
    @property
    def financialId(self):
        return self.__financialId

    @property
    def consentId(self):
        return self.__consentId
