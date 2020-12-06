import requests
import base64
import json
import datetime
import OpenSSL
from urllib.parse import urlencode
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
    
def get_consent_request(banficoAuth, financialId, response):
    json = response.json()
    return develop_.BanficoConsentRequestValid(banficoAuth, financialId, json['Data']['ConsentId'])
    
def request_consent(banficoConsentRequest):
    url = 'https://auth.obiebank.banfico.com/auth/realms/provider/protocol/openid-connect/auth'
    banficoAuth = banficoConsentRequest.banficoAuth
    state = 1224489742391
    nonce = 1440569813538
    exp = int((datetime.datetime.now() + datetime.timedelta(hours=1)).astimezone(datetime.timezone.utc).timestamp())
    iat = int(datetime.datetime.now().astimezone(datetime.timezone.utc).timestamp())
    param = {'response_type':'code','client_id':banficoAuth.clientId,'redirect_uri':'https://developer.obiebank.banfico.com/callback','scope':'openid profile email accounts','state':state,'nonce':nonce}
    requestHeader = {'alg': 'RS256','typ': 'JWT'}
    requestPayload = {'aud': 'https://auth.obiebank.banfico.com/auth/realms/provider',
                      'iss': banficoAuth.clientId,
                      'client_id': banficoAuth.clientId,
                      'redirect_uri': 'https://developer.obiebank.banfico.com/callback',
                      'scope': 'openid profile email accounts',
                      'state': state,
                      'nonce': nonce,
                      'exp': exp,
                      'response_type': 'code id_token',
                      'claims': {
                                 'userinfo': {
                                              'openbanking_intent_id': {
                                                                        'value': 'urn:obiebank:accounts:' + banficoConsentRequest.consentId,
                                                                        'essential': True
                                                                        }
                                },
                                'id_token': {
                                             'openbanking_intent_id': {
                                                                       'value': 'urn:obiebank:accounts:' + banficoConsentRequest.consentId,
                                                                       'essential': True
                                                                      },
                                             'acr': {
                                                       'essential': True,
                                                        'values': [
                                                                    'urn:openbanking:psd2:sca',
                                                                    'urn:openbanking:psd2:ca'
                                                        ]
                                            }
                                }
                     },
                     'iat': iat
                    }
    param['request'] = base64.b64encode(json.dumps(requestHeader).encode('ascii')) + '.'.encode('ascii') + base64.b64encode(json.dumps(requestPayload).encode('ascii'))
    privkeyfile = 'C:\\xampp\\htdocs\\hackathonOpenBank\\data_\\key.pem'
    with open(privkeyfile, "r") as key_file:
        key = key_file.read()
    pkey = OpenSSL.crypto.load_privatekey(OpenSSL.crypto.FILETYPE_PEM, key)
    sign = OpenSSL.crypto.sign(pkey, param['request'], "sha256") 
    param['request'] = param['request'] + '.'.encode('ascii') + base64.urlsafe_b64encode(sign)
    url = url+'?'+urlencode(param)
    return url

def authenticate_by_code(banficoConsentRequest, code):
    url = 'https://auth.obiebank.banfico.com/auth/realms/provider/protocol/openid-connect/token'
    banficoAuth = banficoConsentRequest.banficoAuth
    payload = {'grant_type':'authorization_code','code':code,'client_id':banficoAuth.clientId,'client_secret':banficoAuth.clientSecret,'redirect_uri':'https://developer.obiebank.banfico.com/callback'}
    response = requests.post(url, data=payload)
    return response
    
def bearer_consent(banficoConsentRequest, response):
    json = response.json()
    banficoAuth = banficoConsentRequest.banficoAuth
    financialId = banficoConsentRequest.financialId
    consentId = banficoConsentRequest.consentId
    banficoAuthConsent = develop_.BanficoAuthValid(banficoAuth.clientId,banficoAuth.clientSecret,json['access_token'])
    return develop_.BanficoConsentValid(banficoAuth, banficoAuthConsent, financialId, consentId)
    
def get_user_accounts(banficoConsent):
    url = 'https://gw-dev.obiebank.banfico.com/obie-aisp/v3.1/aisp/accounts'
    financialId = banficoConsent.financialId
    bearer = 'Bearer ' + banficoConsent.banficoAuthConsent.bearer
    headers = {'x-fapi-financial-id':banficoConsent.financialId, 'Authorization':bearer}
    response = requests.get(url, headers=headers)
    return response

def get_account_transactions(banficoConsent, banficoAccount):
    url = 'https://gw-dev.obiebank.banfico.com/obie-aisp/v3.1/aisp/accounts/' + banficoAccount.accountId + '/transactions'
    financialId = banficoConsent.financialId
    bearer = 'Bearer ' + banficoConsent.banficoAuthConsent.bearer
    headers = {'x-fapi-financial-id':banficoConsent.financialId, 'Authorization':bearer}
    response = requests.get(url, headers=headers)
    return response
    