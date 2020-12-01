import unittest
import datetime

from models.tag import Tag
from models.merchant import Merchant
from models.transaction import Transaction

class TestTransaction(unittest.TestCase):

    def setUp(self):
        self.tag = Tag("Groceries", 2)
        self.merchant = Merchant("Tesco", 3)
        self.datetime_1 = datetime.datetime(2020, 10, 7, 14, 2, 0)
        self.datetime_2 = datetime.datetime(2020, 9, 5, 13, 3, 0)
        self.transaction = Transaction(3.20, self.merchant, self.tag, self.datetime_1, 4)
        self.transaction_no_id = Transaction(3.20, self.merchant, self.tag, self.datetime_2)


    def test_transaction_has_amount(self):
        self.assertEqual(self.transaction.amount, 3.20)

    def test_transaction_has_id(self):
        self.assertEqual(self.transaction.id, 4)

    def test_transaction_has_tag(self):
        self.assertEqual(self.transaction.tag, self.tag)
  
    def test_transaction_has_merchant(self):
        self.assertEqual(self.transaction.merchant, self.merchant)

    def test_transaction_has_datetime(self):
        self.assertEqual(self.transaction.trans_time, self.datetime_1)

    def test_transaction_id_starts_as_none(self):
        self.assertIsNone(self.transaction_no_id.id)
