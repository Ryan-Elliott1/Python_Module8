import unittest
from unittest.mock import patch
from more_fun_with_collections import dict_membership


class TestSet(unittest.TestCase):
    def test_in_dict_true(self):
        self.assertTrue(dict_membership.in_dict({'Billy': 1, 'Bob': 2, 'Jerry': 3}, 'Bob'), True)

    def test_in_dict_false(self):
        self.assertFalse(dict_membership.in_dict({'Billy': 1, 'Bob': 2, 'Jerry': 3}, 'Tom'), False)
