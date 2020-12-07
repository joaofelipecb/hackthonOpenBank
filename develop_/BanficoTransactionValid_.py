import struct_

class BanficoTransactionValid (struct_.BanficoTransaction):
    def __init__(self, transactionId, transactionReference, valueDateTime, creditDebitIndicator, amount, code):
        super().__init__(transactionId, transactionReference, valueDateTime, creditDebitIndicator, amount, code)
