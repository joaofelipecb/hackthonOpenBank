import control_.Banfico
import struct_
import develop_
def get_credentials():
    credentials = struct_.BanficoAuth('PSDAA-AAAAAAAA-AAAAAAAAAA','GeoCred@123','')
    return credentials
    
def get_user_accounts(banficoConsent):
    json = control_.Banfico.get_user_accounts(banficoConsent)
    list = []
    for account in json['Data']['Account']:
        list.append(develop_.BanficoAccountValid(account['AccountId'],account['Nickname']))
    return list
