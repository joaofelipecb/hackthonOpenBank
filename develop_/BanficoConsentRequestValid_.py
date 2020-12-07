import struct_

class BanficoConsentRequestValid (struct_.BanficoConsentRequest):
    def __init__(self, banficoAuth, financialId, consentId):
        super().__init__(banficoAuth, financialId, consentId)
