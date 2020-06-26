import unittest
from unittest.mock import patch
from more_fun_with_collections import set_membership


class TestSet(unittest.TestCase):
    def test_in_set_true(self):
        self.assertTrue(set_membership.in_set({2, 4, 5, 6}, 4), True)

    def test_in_set_false(self):
        self.assertFalse(set_membership.in_set({2, 4, 5, 6}, 3), False)
