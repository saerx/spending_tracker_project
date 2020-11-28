import unittest

from models.tag import Tag

class TestTag(unittest.TestCase):

    def setUp(self):
        self.tag = Tag("Groceries", 2)
        self.tag_no_id = Tag("Entertainment")

    def test_tag_has_name(self):
        self.assertEqual(self.tag.name, "Groceries")

    def test_tag_has_id(self):
        self.assertEqual(self.tag.id, 2)

    def test_tag_id_starts_as_none(self):
        self.assertIsNone(self.tag_no_id.id)
