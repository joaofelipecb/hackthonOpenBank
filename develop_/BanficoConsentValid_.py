import struct_

class BanficoConsentValid (struct_.BanficoConsent):
    def __init__(self, banficoAuth, financialId, consentId):
        super().__init__(banficoAuth, financialId, consentId)
