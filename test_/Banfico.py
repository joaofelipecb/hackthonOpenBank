import control_.Banfico
import struct_
import develop_
import except_
import data_.Banfico

def authenticate_happy():
    try:
        banficoAuth = data_.Banfico.get_credentials()
        banficoAuth = control_.Banfico.authenticate(banficoAuth)
        if not isinstance(banficoAuth,develop_.BanficoAuthValid):
            return False
        else:
            return True
    except Exception as err:
        print(err)
        return False

def authenticate_raise():
    try:
        banficoAuth = struct_.BanficoAuth('','')
        banficoAuth = control_.Banfico.authenticate(banficoAuth)
        if not isinstance(banficoAuth,develop_.BanficoAuthValid):
            return False
        else:
            return False
    except except_.BanficoResponse:
        return True
    except Exception as err:
        print(err)
        return False
        
def create_access_consents_happy():
    try:
        banficoAuth = data_.Banfico.get_credentials()
        banficoAuth = control_.Banfico.authenticate(banficoAuth)
        if not isinstance(banficoAuth,develop_.BanficoAuthValid):
            return False
        else:
            financialId = '5fcc3d68b01ef2001da27048';
            permissions = ['ReadAccountsBasic', 'ReadAccountsDetail', 'ReadBalances', 'ReadBeneficiariesDetail',
                            'ReadDirectDebits', 'ReadProducts', 'ReadStandingOrdersDetail', 'ReadTransactionsCredits',
                            'ReadTransactionsDebits', 'ReadTransactionsDetail', 'ReadOffers', 'ReadPAN', 'ReadParty',
                            'ReadPartyPSU', 'ReadScheduledPaymentsDetail', 'ReadStatementsDetail']
            banficoConsent = control_.Banfico.create_access_consents(banficoAuth, financialId, permissions)
            if not isinstance(banficoConsent,develop_.BanficoConsentValid):
                return False
            return True
    except Exception as err:
        print(err)
        return False
        
def create_access_consents_raise():
    try:
        banficoAuth = data_.Banfico.get_credentials()
        financialId = '5fcc3d68b01ef2001da27048';
        permissions = ['ReadAccountsBasic', 'ReadAccountsDetail', 'ReadBalances', 'ReadBeneficiariesDetail',
                        'ReadDirectDebits', 'ReadProducts', 'ReadStandingOrdersDetail', 'ReadTransactionsCredits',
                        'ReadTransactionsDebits', 'ReadTransactionsDetail', 'ReadOffers', 'ReadPAN', 'ReadParty',
                        'ReadPartyPSU', 'ReadScheduledPaymentsDetail', 'ReadStatementsDetail']
        control_.Banfico.create_access_consents(banficoAuth, financialId, permissions)
        return False
    except except_.BanficoResponse:
        return True
    except Exception as err:
        print(err)
        return False
    
'''if authenticate_happy():
    print("Benfico Auth Happy: ok")
else:
    print("Benfico Auth Happy: ERROR")
    
if authenticate_raise():
    print("Benfico Auth Raise: ok")
else:
    print("Benfico Auth Raise: ERROR")'''
    
if create_access_consents_happy():
    print("Benfico Create Access Consents Happy: ok")
else:
    print("Benfico Create Access Consents Happy: ERROR")

'''if create_access_consents_raise():
    print("Benfico Create Access Consents Raise: ok")
else:
    print("Benfico Create Access Consents Raise: ERROR")'''