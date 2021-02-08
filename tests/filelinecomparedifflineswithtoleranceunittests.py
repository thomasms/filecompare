import unittest
import os.path
import filecompare as fc

from tests.filelinecompareunittests import FileLineCompareUnitTest


class FileLineCompareDiffLinesWithToleranceUnitTest(FileLineCompareUnitTest, unittest.TestCase):
    
    def setUp(self):
        FileLineCompareUnitTest.setUp(self)
        self.filename_original_text_and_chars = os.path.join(self.base_dir, "original_text_and_chars.txt")
        self.filename_compare_text_and_chars  = os.path.join(self.base_dir, "compare_text_and_chars_with_tolerance.txt")
        self.filename_compare_text_and_chars2 = os.path.join(self.base_dir, "compare_text_and_chars_with_tolerance_and_diff_lines.txt")
    
    def get_test_files_tolerance(self):
        return self.filename_original_text_and_chars, self.filename_compare_text_and_chars
    
    def get_test_files_tolerance2(self):
        return self.filename_original_text_and_chars, self.filename_compare_text_and_chars2
    
    def test_linecompare_diff_with_no_tolerance(self):
        file1, file2 = self.get_test_files_tolerance()
        
        self.operation = fc.FileLineCompareDiffLinesWithTolerance(relative_tolerance=0.0, absolute_tolerance=0.0)
        result = self.operation(file1, file2, ignore=[])
        self.assertNotEqual(0, len(self.operation.diffs), "Assert differences")
        self.assertEqual(result, False)
    
    def test_linecompare_diff_with_low_tolerance(self):
        file1, file2 = self.get_test_files_tolerance()
        
        self.operation = fc.FileLineCompareDiffLinesWithTolerance(relative_tolerance=0.01, absolute_tolerance=0.0)
        result = self.operation(file1, file2, ignore=[])
        self.assertNotEqual(0, len(self.operation.diffs), "Assert differences")
        self.assertEqual(result, False)
    
    def test_linecompare_diff_with_acceptable_tolerance_no_ignore(self):
        file1, file2 = self.get_test_files_tolerance()
        
        self.operation = fc.FileLineCompareDiffLinesWithTolerance(relative_tolerance=0.1, absolute_tolerance=0.0)
        result = self.operation(file1, file2, ignore=[])
        self.assertNotEqual(0, len(self.operation.diffs), "Assert differences")
        self.assertEqual(result, False)
    
    def test_linecompare_diff_with_acceptable_tolerance_with_ignore(self):
        file1, file2 = self.get_test_files_tolerance()
        
        self.operation = fc.FileLineCompareDiffLinesWithTolerance(relative_tolerance=0.1, absolute_tolerance=0.0)
        result = self.operation(file1, file2, ignore=['3fg'])
        self.assertEqual(0, len(self.operation.diffs), "Assert no differences")
        self.assertEqual(result, True)
    
    def test_linecompare_diff_with_low_tolerance_and_ignore(self):
        file1, file2 = self.get_test_files_tolerance()
        
        self.operation = fc.FileLineCompareDiffLinesWithTolerance(relative_tolerance=0.01, absolute_tolerance=0.0)
        result = self.operation(file1, file2, ignore=['3fg'])
        self.assertNotEqual(0, len(self.operation.diffs), "Assert differences")
        self.assertEqual(result, False)
    
    def test_linecompare_diff_with_abs_tolerance_and_ignore(self):
        file1, file2 = self.get_test_files_tolerance()
        
        self.operation = fc.FileLineCompareDiffLinesWithTolerance(relative_tolerance=0.0, absolute_tolerance=0.9)
        result = self.operation(file1, file2, ignore=['3fg'])
        self.assertNotEqual(0, len(self.operation.diffs), "Assert differences")
        self.assertEqual(result, False)
    
    def test_linecompare_diff_with_abs_tolerance_no_ignore(self):
        file1, file2 = self.get_test_files_tolerance()
        
        self.operation = fc.FileLineCompareDiffLinesWithTolerance(relative_tolerance=0.0, absolute_tolerance=1.0)
        result = self.operation(file1, file2, ignore=[])
        self.assertNotEqual(0, len(self.operation.diffs), "Assert differences")
        self.assertEqual(result, False)
    
    def test_linecompare_diff_with_abs_tolerance_and_ignore_pass(self):
        file1, file2 = self.get_test_files_tolerance()
        
        self.operation = fc.FileLineCompareDiffLinesWithTolerance(relative_tolerance=0.0, absolute_tolerance=1.0)
        result = self.operation(file1, file2, ignore=['3fg'])
        self.assertEqual(0, len(self.operation.diffs), "Assert no differences")
        self.assertEqual(result, True)
    
    def test_linecompare_diff_with_abs_tolerance_and_rel_tolerance(self):
        file1, file2 = self.get_test_files_tolerance()
        
        self.operation = fc.FileLineCompareDiffLinesWithTolerance(relative_tolerance=0.01, absolute_tolerance=0.9)
        result = self.operation(file1, file2, ignore=['3fg'])
        self.assertEqual(0, len(self.operation.diffs), "Assert no differences")
        self.assertEqual(result, True)
    
    def test_linecompare_diff_with_abs_tolerance_and_rel_tolerance_fail(self):
        file1, file2 = self.get_test_files_tolerance()
        
        self.operation = fc.FileLineCompareDiffLinesWithTolerance(relative_tolerance=1e-3, absolute_tolerance=0.9)
        result = self.operation(file1, file2, ignore=['3fg'])
        self.assertNotEqual(0, len(self.operation.diffs), "Assert differences")
        self.assertEqual(result, False)

    def test_linecompare_diff_with_abs_tolerance_and_rel_tolerance_and_ignore_in_one_file_only(self):
        file1, file2 = self.get_test_files_tolerance2()
        
        self.operation = fc.FileLineCompareDiffLinesWithTolerance(relative_tolerance=0.1, absolute_tolerance=0.0)
        result = self.operation(file1, file2, ignore=['This line is to be ignored', '3fg'])
        self.assertEqual(0, len(self.operation.diffs), "Assert no differences")
        self.assertEqual(result, True)

    def test_linecompare_diff_with_abs_tolerance_and_rel_tolerance_and_ignore_in_one_file_only2(self):
        file1, file2 = self.get_test_files_tolerance2()
        
        self.operation = fc.FileLineCompareDiffLinesWithTolerance(relative_tolerance=0.1, absolute_tolerance=0.0)
        result = self.operation(file1, file2, ignore=['ignored', '3fg'])
        self.assertEqual(0, len(self.operation.diffs), "Assert no differences")
        self.assertEqual(result, True)
    
    def test_linecompare_diff_with_abs_tolerance_and_rel_tolerance_and_ignore_in_one_file_only_fail(self):
        file1, file2 = self.get_test_files_tolerance2()
        
        self.operation = fc.FileLineCompareDiffLinesWithTolerance(relative_tolerance=0.0, absolute_tolerance=0.0)
        result = self.operation(file1, file2, ignore=['This line is to be ignored', '3fg'])
        self.assertEqual(3, len(self.operation.diffs), "Assert differences")
        self.assertEqual(result, False)
    
    def test_linecompare_diff_with_abs_tolerance_and_rel_tolerance_and_ignore_in_one_file_only_fail2(self):
        file1, file2 = self.get_test_files_tolerance2()
        
        self.operation = fc.FileLineCompareDiffLinesWithTolerance(relative_tolerance=0.0, absolute_tolerance=0.0, custom_splitter="f")
        result = self.operation(file1, file2, ignore=['ignored not', '3fg'])
        self.assertEqual(0, len(self.operation.diffs), "Assert no differences since number of lines are different")
        self.assertEqual(result, False)
