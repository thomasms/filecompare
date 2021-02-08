import unittest
import os.path
import filecompare as fc

from tests.filebasecompareunittests import FileBaseCompareUnitTests


class FileLineCompareUnitTest(FileBaseCompareUnitTests, unittest.TestCase):

    operation = fc.FileLineCompare()

    def setUp(self):
        FileBaseCompareUnitTests.setUp(self)
        self.filename_compare_same2 = os.path.join(self.base_dir, "compare_same2.txt")

    def get_test_files_same2(self):
        return self.filename_original, self.filename_compare_same2

    # different compare implementations give different results for empty files with whitespace
    # This is line compare so ignores whitespace
    def test_compare_empty_files_ws(self):
        file1, file2 = self.get_empty_test_files_ws()

        result = self.operation(file1, file2)
        self.assertEqual(result, True)

    def test_linecompare_diff_ignore(self):
        file1, file2 = self.get_test_files_diff()

        result = self.operation(file1, file2, ignore=['sat'])
        self.assertEqual(result, False)

    def test_linecompare_diff_ignore2(self):
        file1, file2 = self.get_test_files_diff()

        result = self.operation(file1, file2, ignore=['sat', 'move'])
        self.assertEqual(result, False)

    def test_linecompare_diff_ignore3(self):
        file1, file2 = self.get_test_files_diff()

        # This should still fail since the framework only ignores line that share the same keywords
        # i.e. it must exist in both files. Since '$' exists in only one file it is not ignored.
        result = self.operation(file1, file2, ignore=['sat', 'move', '$'])
        self.assertEqual(result, False)

    def test_linecompare_diff_ignore4(self):
        file1, file2 = self.get_test_files_diff2()

        # This should still fail since the framework only ignores line that share the same keywords
        # i.e. it must exist in both files. Since the extra whitespace (the return line) is added in one file,
        # the lines do not match up and it should fail
        result = self.operation(file1, file2, ignore=['sat', 'move', 'After'])
        self.assertEqual(result, False)

    def test_linecompare_same_ignore(self):
        file1, file2 = self.get_test_files_same2()

        result = self.operation(file1, file2, ignore=['After some space'])
        self.assertEqual(result, True)
