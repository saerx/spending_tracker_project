import unittest

from models.tag import Tag
from models.merchant import Merchant
from models.transaction import Transaction

class TestTransaction(unittest.TestCase):

    def setUp(self):
        self.tag = Tag("Groceries", 2)
        self.merchant = Merchant("Tesco", 3)
        self.transaction = Transaction(3.20, self.merchant, self.tag, 4)
        self.transaction_no_id = Transaction(3.20, self.merchant, self.tag)

    def test_transaction_has_amount(self):
        self.assertEqual(self.transaction.amount, 3.20)

    def test_transaction_has_id(self):
        self.assertEqual(self.transaction.id, 4)

    def test_transaction_has_tag(self):
        self.assertEqual(self.transaction.tag, self.tag)
  
    def test_transaction_has_merchant(self):
        self.assertEqual(self.transaction.merchant, self.merchant)

    def test_transaction_id_starts_as_none(self):
        self.assertIsNone(self.transaction_no_id.id)
