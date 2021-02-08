import unittest
import os.path


class FileBaseCompareUnitTests(object):
    operation = None

    def setUp(self):
        self.base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'testfiles')

        self.filename_empty = os.path.join(self.base_dir, "empty_file.txt")
        self.filename_empty_ws = os.path.join(self.base_dir, "empty_file_with_whitespace.txt")
        self.filename_original = os.path.join(self.base_dir, "original.txt")
        self.filename_compare_same = os.path.join(self.base_dir, "compare_same.txt")
        self.filename_compare_diff = os.path.join(self.base_dir, "compare_diff.txt")
        self.filename_compare_diff2 = os.path.join(self.base_dir, "compare_diff2.txt")

    def get_empty_test_files(self):
        return self.filename_empty, self.filename_empty

    def get_empty_test_files_ws(self):
        return self.filename_empty, self.filename_empty_ws

    def get_test_files_same(self):
        return self.filename_original, self.filename_compare_same

    def get_test_files_diff(self):
        return self.filename_original, self.filename_compare_diff

    def get_test_files_diff2(self):
        return self.filename_original, self.filename_compare_diff2

    def test_compare_empty_files(self):
        file1, file2 = self.get_empty_test_files()

        result = self.operation(file1, file2)
        self.assertEqual(result, True)

    def test_compare_same(self):
        file1, file2 = self.get_test_files_same()

        result = self.operation(file1, file2)
        self.assertEqual(result, True)

    def test_compare_same2(self):
        file1, file2 = self.get_test_files_same()

        result = self.operation(file1, file1)
        self.assertEqual(result, True)

    def test_compare_same3(self):
        file1, file2 = self.get_test_files_same()

        result = self.operation(file2, file2)
        self.assertEqual(result, True)

    def test_compare_same4(self):
        file1, file2 = self.get_test_files_same()

        result = self.operation(file2, file1)
        self.assertEqual(result, True)

    def test_compare_diff(self):
        file1, file2 = self.get_test_files_diff()

        result = self.operation(file1, file2)
        self.assertEqual(result, False)

    def test_compare_diff2(self):
        file1, file2 = self.get_test_files_diff()

        result = self.operation(file2, file1)
        self.assertEqual(result, False)

    def test_compare_diff21(self):
        file1, file2 = self.get_test_files_diff2()

        result = self.operation(file2, file1)
        self.assertEqual(result, False)

    def test_compare_diff22(self):
        file1, file2 = self.get_test_files_diff2()

        result = self.operation(file1, file2)
        self.assertEqual(result, False)


