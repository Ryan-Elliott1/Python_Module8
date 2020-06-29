import unittest
from unittest.mock import patch
from more_fun_with_collections import half_birthday_assignment


class TestSwitch(unittest.TestCase):
    def test_half_birthday(self):
        self.assertEqual(half_birthday_assignment.half_birthday('8/8/2020'), '2020-02-08 00:00:00')
