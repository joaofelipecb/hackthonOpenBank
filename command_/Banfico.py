import requests
import base64
import develop_

def authenticate(banficoAuth):
    url = 'https://auth.obiebank.banfico.com/auth/realms/provider/protocol/openid-connect/token'
    basic = banficoAuth.clientId + ':' + banficoAuth.clientSecret
    basic = basic.encode('ascii')
    basic = base64.b64encode(basic)
    basic = 'Basic '.encode('ascii')+basic
    headers = {'Authorization':basic}
    payload = {'grant_type':'client_credentials','scope':'accounts'}
    response = requests.post(url, headers=headers, data=payload)
    return response
    
def bearer(banficoAuth, response):
    json = response.json()
    print(json['access_token'])
    return develop_.BanficoAuthValid(banficoAuth.clientId,banficoAuth.clientSecret,json['access_token'])
