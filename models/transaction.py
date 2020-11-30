from datetime import datetime

class Transaction:
    def __init__(self, amount, merchant, tag, trans_time, id=None):
        self.amount = amount
        self.merchant = merchant
        self.tag = tag
        self.trans_time = trans_time
        self.id = id

    def display_amount(self):
        return ("£%.2f" % self.amount)