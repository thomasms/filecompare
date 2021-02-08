import unittest
import filecompare as fc

from tests.filebasecompareunittests import FileBaseCompareUnitTests


class FileDiffCompareUnitTest(FileBaseCompareUnitTests, unittest.TestCase):
    operation = fc.FileLineDiffCompare()

    def test_compare_empty_files_ws(self):
        file1, file2 = self.get_empty_test_files_ws()

        result = self.operation(file1, file2)
        self.assertEqual(result, False)
