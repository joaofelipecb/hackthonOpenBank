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
        accountId = account['AccountId']
        nickname = account['Nickname']
        list.append(develop_.BanficoAccountValid(accountId,nickname))
    return list
    
def get_account_transactions(banficoConsent, banficoAccount):
    json = control_.Banfico.get_account_transactions(banficoConsent, banficoAccount)
    list = []
    for transaction in json['Data']['Transaction']:
        transactionId = transaction['TransactionId']
        transactionReference = transaction['TransactionReference']
        valueDateTime = transaction['ValueDateTime']
        creditDebitIndicator = transaction['CreditDebitIndicator']
        amount = transaction['Amount']['Amount']
        code = transaction['BankTransactionCode']['Code']
        list.append(develop_.BanficoTransactionValid(transactionId,transactionReference,valueDateTime,creditDebitIndicator,amount,code))
    return list
