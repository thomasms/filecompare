import unittest
import os.path

from filecompare.compare.jsonfilecompare import JSONFileCompare


class JSONFileCompareUnitTest(unittest.TestCase):
    
    def setUp(self):
        self.base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'testfiles')
        self.json_original = os.path.join(self.base_dir, "1.json")
        self.json_reordered = os.path.join(self.base_dir, "1_reordered.json")
        self.json_diff = os.path.join(self.base_dir, "1_diff.json")
    
    def test_reordering(self):
        self.operation = JSONFileCompare(relative_tolerance=0.0, absolute_tolerance=0.0)
        self.assertEqual(self.operation(self.json_original, self.json_reordered, ignore=[]), True)
        self.assertEqual(self.operation(self.json_reordered, self.json_original, ignore=[]), True)

    def test_diff(self):
        self.operation = JSONFileCompare(relative_tolerance=0.0, absolute_tolerance=0.0)
        self.assertEqual(self.operation(self.json_original, self.json_diff, ignore=[]), False)
        self.assertEqual(self.operation(self.json_diff, self.json_original, ignore=[]), False)


