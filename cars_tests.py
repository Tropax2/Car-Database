from main import *
import unittest
from collections import Counter

# Tests the functions on main
class TestMainFunctions(unittest.TestCase):
        
    def test_write_on_database(self):
        result = write_on_database('jeep', 'avenger', 2025, testing=True)
        expected = [{'brand': 'Jeep', 'model': 'Avenger', 'year': 2025}]
        self.assertEqual(result, expected)

    def test_brands_and_amount(self):
        result = dict(Counter(brands_and_amount([{'brand': 'Jeep', 'model': 'Avenger', 'year': 2025}])))
        expected = {'Jeep': 1}
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main() 