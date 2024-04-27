#!/usr/bin/python3
""" Unittest for max_integer([..])
"""
import unittest
max_no = __import__("6-max_integer").max_integer


class Test_max_integer(unittest.TestCase):
    """
    class containing test cases
    inherited from unittest.testcase
    """
    def cor_output(self):
        """
        checks the correct out puts
        """
        """ tests easy numbers"""
        self.assertAlmostEqual(max_no([1, 2, 3]), 3)
        """ tests letters with ascii code"""
        self.assertAlmostEqual(max_no("abc"), 'c')
        """ tests empty list"""
        self.assertAlmostEqual(max_no([]), None)
        """tests hexa numbers"""
        self.assertAlmostEqual([0x01, 0x4, 0x2], 0x02)
        """tests floats"""
        self.assertAlmostEqual([0.3, -0.3, 5.2], 5.2)
