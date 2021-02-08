from filecompare.compare.filesimplecompare import FileSimpleCompare
from filecompare.utils.file import *


class FileLineCompare(FileSimpleCompare):
    def __init__(self):
        self.diffs = []

    def __call__(self, filename_original, filename_compare, ignore=[]):
        self.diffs = []
        FileSimpleCompare.validate(filename_original)
        FileSimpleCompare.validate(filename_compare)
        result = True

        # check the file lengths first
        fol = nr_of_lines(filename_original, ignore_empty_lines=True)
        foc = nr_of_lines(filename_compare, ignore_empty_lines=True)
        if fol != foc:
            return False

        with open(filename_original) as fo, open(filename_compare) as fc:
            for lo, lc in zip(fo, fc):
                if lo != lc:
                    if not (self.applyignores(ignore, lo, lc) or self.applyfilters(lo, lc)):
                        self.diffs.append((lo, lc))
                        result = False

        return result

    def applyfilters(self, line1, line2):
        return False

    def applyignores(self, ignore, line1, line2):
        # it must exist in both lines
        op = lambda i, l1, l2: i in l1 and i in l2
        return FileLineCompare.checkignores(ignore, line1, line2, op)

    @staticmethod
    def checkignores(ignore, line1, line2, comparisonop):
        for i in ignore:
            if comparisonop(i, line1, line2):
                return True

        return False

