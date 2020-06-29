import unittest
from unittest.mock import patch
from more_fun_with_collections import assign_average


class TestSwitch(unittest.TestCase):
    def test_switch_a(self):
        self.assertEqual(assign_average.switch_average(1), "You chose a")

    def test_switch_A(self):
        self.assertEqual(assign_average.switch_average(2), "You chose A")

    def test_switch_b(self):
        self.assertEqual(assign_average.switch_average(3), "You chose b")

    def test_switch_B(self):
        self.assertEqual(assign_average.switch_average(4), "You chose B")

    def test_switch_c(self):
        self.assertEqual(assign_average.switch_average(5), "You chose c")

    def test_switch_C(self):
        self.assertEqual(assign_average.switch_average(6), "You chose C")

    def test_switch_default(self):
        self.assertEqual(assign_average.switch_average(10), "Invalid choice")
