import command_.Banfico
import data_.Banfico

def authenticate():
    banficoAuth = data_.Banfico.get_credentials()
    response = command_.Banfico.authenticate(banficoAuth)
    if response.status_code != 200:
        raise except_.BanficoAuth(response.status_code)
    banficoAuth = command_.Banfico.bearer(banficoAuth,response)
    return banficoAuth
    
authenticate()
