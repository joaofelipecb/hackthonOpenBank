import struct_

class BanficoConsentValid (struct_.BanficoConsent):
    def __init__(self, banficoAuth, consentId):
        super().__init__(banficoAuth, consentId)
