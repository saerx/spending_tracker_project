import unittest

from models.merchant import Merchant

class TestMerchant(unittest.TestCase):

    def setUp(self):
        self.merchant = Merchant("Tesco", 3)
        self.merchant_no_id = Merchant("eBay")

    def test_can_test(self):
        self.assertEqual(True, True)

    def test_merchant_has_name(self):
        self.assertEqual(self.merchant.name, "Tesco")

    def test_merchant_id_starts_as_none(self):
        self.assertIsNone(self.merchant_no_id.id)

    def test_merchant_has_id(self):
        self.assertEqual(self.merchant.id, 3)

