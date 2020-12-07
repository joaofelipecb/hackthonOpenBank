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
    banficoConsentRequest = command_.Banfico.get_consent_request(banficoAuth, financialId, response)
    return banficoConsentRequest
    
def request_consent(banficoConsentRequest):
    url = command_.Banfico.request_consent(banficoConsentRequest)
    return url
    
def authenticate_by_code(banficoConsentRequest, code):
    response = command_.Banfico.authenticate_by_code(banficoConsentRequest, code)
    if response.status_code != 200:
        raise except_.BanficoResponse(response.status_code)
    banficoConsent = command_.Banfico.bearer_consent(banficoConsentRequest,response)
    return banficoConsent

def get_user_accounts(banficoConsent):
    response = command_.Banfico.get_user_accounts(banficoConsent)
    if response.status_code != 200:
        raise except_.BanficoResponse(response.status_code)
    return response.json()
    
def get_account_transactions(banficoConsent, banficoAccount):
    response = command_.Banfico.get_account_transactions(banficoConsent, banficoAccount)
    if response.status_code != 200:
        raise except_.BanficoResponse(response.status_code)
    return response.json()    
    