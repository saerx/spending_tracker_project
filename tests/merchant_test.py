import unittest

from models.merchant import Merchant

class TestMerchant(unittest.TestCase):

    def setUp(self):
        self.merchant = Merchant("Tesco", 3)

    def test_merchant_has_name(self):
        self.assertEqual(self.merchant.name, "Tesco")

    def test_merchant_has_id(self):
        self.assertEqual(self.merchant.id, 3)
