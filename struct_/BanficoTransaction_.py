class BanficoTransaction:
    def __init__(self, transactionId, transactionReference, valueDateTime, creditDebitIndicator, amount, code):
        self.__transactionId = transactionId
        self.__transactionReference = transactionReference
        self.__valueDateTime = valueDateTime
        self.__creditDebitIndicator = creditDebitIndicator
        self.__amount = amount
        self.__code = code
        
    @property
    def transactionId(self):
        return self.__transactionId

    @property
    def transactionReference(self):
        return self.__transactionReference
        
    @property
    def valueDateTime(self):
        return self.__valueDateTime
        
    @property
    def creditDebitIndicator(self):
        return self.__creditDebitIndicator
        
    @property
    def amount(self):
        return self.__amount
        
    @property
    def code(self):
        return self.__code
        