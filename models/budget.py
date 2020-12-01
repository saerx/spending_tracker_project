class Budget:
    def __init__(self, amount, id = None):
        self.amount = amount
        self.id = id

    def display_amount(self):
        return ("£%.2f" % self.amount)
