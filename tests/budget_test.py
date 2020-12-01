import unittest

from models.budget import Budget

class TestBudget(unittest.TestCase):

    def setUp(self):
        self.budget_1 = Budget(600.00)

    def test_budget_has_amount(self):
        self.assertEqual(self.budget_1.amount, 600.00)

    def test_budget_id_starts_none(self):
        self.assertIsNone(self.budget_1.id)