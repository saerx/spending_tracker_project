class Transaction:
    def __init__(self, amount, merchant, tag, id=None):
        self.amount = amount
        self.merchant = merchant
        self.tag = tag
        self.id = id

    def display_amount(self):
        return ("£%.2f" % self.amount)