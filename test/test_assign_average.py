import unittest
from unittest.mock import patch
from more_fun_with_collections import assign_average


class TestSwitch(unittest.TestCase):
    def test_switch_A(self):
        self.assertEqual(assign_average.switch_average('A'), "You chose A")

    def test_switch_a(self):
        self.assertEqual(assign_average.switch_average('a'), "You chose A")

    def test_switch_B(self):
        self.assertEqual(assign_average.switch_average('B'), "You chose B")

    def test_switch_b(self):
        self.assertEqual(assign_average.switch_average('b'), "You chose B")

    def test_switch_C(self):
        self.assertEqual(assign_average.switch_average('C'), "You chose C")

    def test_switch_c(self):
        self.assertEqual(assign_average.switch_average('c'), "You chose C")

    def test_switch_default(self):
        self.assertEqual(assign_average.switch_average('Z'), "Invalid choice")
