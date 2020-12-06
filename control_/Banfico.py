import command_.Banfico
import except_
import data_.Banfico

def authenticate(banficoAuth):
    response = command_.Banfico.authenticate(banficoAuth)
    if response.status_code != 200:
        raise except_.BanficoResponse(response.status_code)
    banficoAuth = command_.Banfico.bearer(banficoAuth,response)
    return banficoAuth

def create_access_consents(banficoAuth, financialId, permissions):
    response = command_.Banfico.create_access_consents(banficoAuth, financialId, permissions)
    if response.status_code != 201:
        raise except_.BanficoResponse(response.status_code)
    banficoConsent = command_.Banfico.consent(banficoAuth,response)
    return banficoConsent
    