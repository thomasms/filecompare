import unittest
import os.path
import filecompare as fc

from tests.filelinecompareunittests import FileLineCompareUnitTest


class FileLineCompareWithFloatToleranceUnitTest(FileLineCompareUnitTest, unittest.TestCase):
    
    def setUp(self):
        FileLineCompareUnitTest.setUp(self)
        self.filename_original_text_and_chars = os.path.join(self.base_dir, "original_text_and_chars.txt")
        self.filename_compare_text_and_chars = os.path.join(self.base_dir, "compare_text_and_chars_with_tolerance.txt")
    
    def get_test_files_tolerance(self):
        return self.filename_original_text_and_chars, self.filename_compare_text_and_chars
    
    def test_linecompare_diff_with_no_tolerance(self):
        file1, file2 = self.get_test_files_tolerance()
        
        self.operation = fc.FileLineCompareWithFloatTolerance(relative_tolerance=0.0, absolute_tolerance=0.0)
        result = self.operation(file1, file2, ignore=[])
        self.assertEqual(result, False)
    
    def test_linecompare_diff_with_low_tolerance(self):
        file1, file2 = self.get_test_files_tolerance()
        
        self.operation = fc.FileLineCompareWithFloatTolerance(relative_tolerance=0.01, absolute_tolerance=0.0)
        result = self.operation(file1, file2, ignore=[])
        self.assertEqual(result, False)
    
    def test_linecompare_diff_with_acceptable_tolerance_no_ignore(self):
        file1, file2 = self.get_test_files_tolerance()
        
        self.operation = fc.FileLineCompareWithFloatTolerance(relative_tolerance=0.1, absolute_tolerance=0.0)
        result = self.operation(file1, file2, ignore=[])
        self.assertEqual(result, False)
    
    def test_linecompare_diff_with_acceptable_tolerance_with_ignore(self):
        file1, file2 = self.get_test_files_tolerance()
        
        self.operation = fc.FileLineCompareWithFloatTolerance(relative_tolerance=0.1, absolute_tolerance=0.0)
        result = self.operation(file1, file2, ignore=['3fg'])
        self.assertEqual(result, True)
    
    def test_linecompare_diff_with_low_tolerance_and_ignore(self):
        file1, file2 = self.get_test_files_tolerance()
        
        self.operation = fc.FileLineCompareWithFloatTolerance(relative_tolerance=0.01, absolute_tolerance=0.0)
        result = self.operation(file1, file2, ignore=['3fg'])
        self.assertEqual(result, False)
    
    def test_linecompare_diff_with_abs_tolerance_and_ignore(self):
        file1, file2 = self.get_test_files_tolerance()
        
        self.operation = fc.FileLineCompareWithFloatTolerance(relative_tolerance=0.0, absolute_tolerance=0.9)
        result = self.operation(file1, file2, ignore=['3fg'])
        self.assertEqual(result, False)
    
    def test_linecompare_diff_with_abs_tolerance_no_ignore(self):
        file1, file2 = self.get_test_files_tolerance()
        
        self.operation = fc.FileLineCompareWithFloatTolerance(relative_tolerance=0.0, absolute_tolerance=1.0)
        result = self.operation(file1, file2, ignore=[])
        self.assertEqual(result, False)
    
    def test_linecompare_diff_with_abs_tolerance_and_ignore_pass(self):
        file1, file2 = self.get_test_files_tolerance()
        
        self.operation = fc.FileLineCompareWithFloatTolerance(relative_tolerance=0.0, absolute_tolerance=1.0)
        result = self.operation(file1, file2, ignore=['3fg'])
        self.assertEqual(result, True)
    
    def test_linecompare_diff_with_abs_tolerance_and_rel_tolerance(self):
        file1, file2 = self.get_test_files_tolerance()
        
        self.operation = fc.FileLineCompareWithFloatTolerance(relative_tolerance=0.01, absolute_tolerance=0.9)
        result = self.operation(file1, file2, ignore=['3fg'])
        self.assertEqual(result, True)
    
    def test_linecompare_diff_with_abs_tolerance_and_rel_tolerance_fail(self):
        file1, file2 = self.get_test_files_tolerance()
        
        self.operation = fc.FileLineCompareWithFloatTolerance(relative_tolerance=1e-3, absolute_tolerance=0.9)
        result = self.operation(file1, file2, ignore=['3fg'])
        self.assertEqual(result, False)

