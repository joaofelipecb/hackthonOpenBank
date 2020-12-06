import requests
import base64
import json
import datetime
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
    return develop_.BanficoAuthValid(banficoAuth.clientId,banficoAuth.clientSecret,json['access_token'])

def create_access_consents(banficoAuth, financialId, permissions):
    url = 'https://gw-dev.obiebank.banfico.com/obie-aisp/v3.1/aisp/account-access-consents'
    bearer = 'Bearer ' + banficoAuth.bearer
    headers = {'x-fapi-financial-id':financialId, 'Authorization':bearer, 'Content-Type': 'application/json; charset=utf-8'}
    data = {'Permissions':permissions,
            'ExpirationDateTime':(datetime.datetime.now() + datetime.timedelta(days=1)).astimezone(datetime.timezone.utc).isoformat(timespec='milliseconds'),
            'TransactionFromDateTime':datetime.datetime.now().astimezone(datetime.timezone.utc).isoformat(timespec='milliseconds'),
            'TransactionToDateTime':datetime.datetime.now().astimezone(datetime.timezone.utc).isoformat(timespec='milliseconds')}
    payload = {'Data':data,'Risk':{}}
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    return response
    
def consent(banficoAuth, response):
    json = response.json()
    return develop_.BanficoConsentValid(banficoAuth,json['Data']['ConsentId'])
    