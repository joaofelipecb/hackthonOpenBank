import pymysql
import json
import datetime
import requests

db = pymysql.connect("localhost","root","","openbanking" )
cursor = db.cursor()
cursor.execute("SELECT * FROM DEMANDA")
result = cursor.fetchall()
for row in result:
    print (row)
    url = 'https://core-api.obiebank.banfico.com/obie-aisp/v3.1/accounts/5fcd4048b01ef2001da27201/transactions'
    bearer = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJSeHpPWmc5dW42dTZyNE50T014elNVbUR6cFZwU3gyaVhha25aWUNxUnRJIn0.eyJleHAiOjE2MDczMTU2MDcsImlhdCI6MTYwNzI4NjgxMCwiYXV0aF90aW1lIjoxNjA3Mjg2ODA3LCJqdGkiOiJiYjc4MDMwZi1lNmVlLTRmNjAtYjVlMS1iYTg1ZGZmMzk1YjYiLCJpc3MiOiJodHRwczovL2F1dGgub2JpZWJhbmsuYmFuZmljby5jb20vYXV0aC9yZWFsbXMvcHJvdmlkZXIiLCJhdWQiOlsiY29yZWJhbmstc3BhIiwiYWNjb3VudCJdLCJzdWIiOiIwZWE1NGMyZC00ZTk3LTRhMjMtOGVkNi1lMTE5OTI4NTFhNDUiLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJjb3JlYmFuay1zcGEiLCJub25jZSI6IjM4OTM2MjEiLCJzZXNzaW9uX3N0YXRlIjoiYWYwOTdiNzQtMWMyYi00ZjY2LTg0MWEtZTdiMjRjODA1NTQ4IiwiYWNyIjoiMSIsInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJwc3UiLCJvZmZsaW5lX2FjY2VzcyIsInVtYV9hdXRob3JpemF0aW9uIl19LCJyZXNvdXJjZV9hY2Nlc3MiOnsiYWNjb3VudCI6eyJyb2xlcyI6WyJtYW5hZ2UtYWNjb3VudCIsIm1hbmFnZS1hY2NvdW50LWxpbmtzIiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInN1YiI6ImpvYW8uZmVsaXBlLmMuYi5wZ2VAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJ1c2VyX2lkIjoiMGVhNTRjMmQtNGU5Ny00YTIzLThlZDYtZTExOTkyODUxYTQ1IiwibmFtZSI6Im4vYSBuL2EiLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJqb2FvLmZlbGlwZS5jLmIucGdlQGdtYWlsLmNvbSIsImdpdmVuX25hbWUiOiJuL2EiLCJmYW1pbHlfbmFtZSI6Im4vYSIsImVtYWlsIjoiam9hby5mZWxpcGUuYy5iLnBnZUBnbWFpbC5jb20iLCJjbGllbnRfaWQiOiJjb3JlYmFuay1zcGEifQ.NFlhwIBhKYlxg2pS1OkcO_F7--riXQL0BAGBG3bKTo_2dgGkEshQQl9SVFveY3EVFHxtOH8xiqZIznhO7Ecay7DLEpNJOz_V5HWFfa25ZZ2A-DPfkANVC7xakaeltIk22ddzqyGJ-_1UypnMN0OVc_8oj7raByU6_Qvwp6ejqRyKaw3v9Oc1oyEQJ-xxyTxeTrnDPZ5YCP_F6Kqf-7yAQGesbOT2I8fsEYW_vNxnYLpWw09d_LzCMTTIPROYdC6N8k_3sPorWHG2RSrWQlYSrDml6rXw-7wIdI93t3JhlQcVJnf-zPcq_KRCEwfbh7I-4wegtUSh_4NhNboahjC6Lw'
    headers = {'Authorization':bearer, 'Content-Type': 'application/json; charset=utf-8'}
    payload = {'TransactionReference':'Ref ' + str(row[0]),
               'Amount':{'Amount':row[3],'Currency':'GBP'},
               'CreditDebitIndicator':'Credit',
               'Status':'Booked',
               'BookingDateTime':row[4].astimezone(datetime.timezone.utc).isoformat(timespec='milliseconds'),
               'ValueDateTime':row[4].astimezone(datetime.timezone.utc).isoformat(timespec='milliseconds'),
               'TransactionInformation':'Entrega',
               'AddressLine':'Room 12, 34 Court Road, London, England, W1T 2JY',
               'BankTransactionCode':{
                                    'Code':'IssuedCreditTransfer',
                                    'SubCode':'AutomaticTransfer'
                                    },
                'ProprietaryBankTransactionCode':{
                                    'Code':'Transfer',
                                    'Issuer':
                                    'CoreBank'
                                    },
                'MerchantDetails':{
                                    'MerchantName':'Heating Contractors LTD',
                                    'MerchantCategoryCode':'1711'
                                  }
            }
    print(json.dumps(payload))
    response = requests.post(url, headers=headers, data=json.dumps(payload))
db.close()
