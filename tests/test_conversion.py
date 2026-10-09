"""
Tests for the unit conversion logic in conversion.py.
Uses Python's unittest framework to test

"""


import unittest
from conversion import find_conversion_factor, convert

class TestConverter(unittest.TestCase):

    #setUp() is a special unittest method. It runs before each test.
    def setUp(self):

        self.graph = {
            "meter": {
                "feet": 3.28084
            },
            "feet": {
                "meter": 1 / 3.28084,
                "inch": 12
            },
            "inch": {
                "feet": 1 / 12
            },
            "kilogram": {
                "gram": 1000
            },
            "gram": {
                "kilogram": 1 / 1000
            }
        }

    #Tests find_conversion_factor()

    #Test 1
    def test_direct_conversion(self):
        factor = find_conversion_factor(self.graph, "meter", "feet")

        self.assertAlmostEqual(factor, 3.28084)

    #Test 2
    def test_reverse_conversion(self):
        factor = find_conversion_factor(self.graph,"feet","meter")

        self.assertAlmostEqual(factor, 1 / 3.28084)


    #Test 3
    def test_indirect_conversion(self):
        factor = find_conversion_factor(self.graph,"meter", "inch")

        self.assertAlmostEqual(factor, 3.28084 * 12)

    #Test 4
    def test_same_unit_conversion(self):
        factor = find_conversion_factor(self.graph,"meter","meter")

        self.assertEqual(factor, 1.0)

    #Tests convert()

    #Test 5
    def test_quantity_conversion(self):
        result = convert(self.graph,5,"meter","feet")
        
        self.assertAlmostEqual(result, 5 * 3.28084)

    #Test 6 : unknown source unit
    def test_unknown_source_unit(self):
        with self.assertRaises(ValueError):
            find_conversion_factor(self.graph, "abc", "inch")

    #Test 7 : unknown target unit
    def test_unknown_target_unit(self):
        with self.assertRaises(ValueError):
            find_conversion_factor(self.graph, "meter", "abc")

    #Test 8 : no conversion path
    def test_no_conversion_path(self):
        with self.assertRaises(ValueError):
            find_conversion_factor(self.graph, "meter", "gram")
