import unittest
import filecompare as fc

from tests.filebasecompareunittests import FileBaseCompareUnitTests


class FileSimpleCompareUnitTest(FileBaseCompareUnitTests, unittest.TestCase):
    operation = fc.FileSimpleCompare()

    # different compare implementations give different results for empty files with whitespace
    def test_compare_empty_files_ws(self):
        file1, file2 = self.get_empty_test_files_ws()

        result = self.operation(file1, file2)
        self.assertEqual(result, False)
