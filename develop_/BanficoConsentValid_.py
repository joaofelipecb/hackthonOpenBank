import struct_

class BanficoConsentValid (struct_.BanficoConsent):
    def __init__(self, banficoAuth, banficoConsent, financialId, consentId):
        super().__init__(banficoAuth, banficoConsent, financialId, consentId)
