from filecompare.utils.line import comparelines
from filecompare.compare.filesimplecompare import FileSimpleCompare
from filecompare.compare.filelinecomparewithfloattolerance import FileLineCompareWithFloatTolerance


class FileLineCompareDiffLinesWithTolerance(FileLineCompareWithFloatTolerance):
    def __init__(self, relative_tolerance, **kwargs):
        FileLineCompareWithFloatTolerance.__init__(self, relative_tolerance, **kwargs)

    def __call__(self, filename_original, filename_compare, ignore=[]):
        self.diffs = []
        FileSimpleCompare.validate(filename_original)
        FileSimpleCompare.validate(filename_compare)
        result = True

        # ignore blank lines
        def readlines(filename, lines):
            with open(filename) as f:
                for line in f:
                    if not self.applyignores(ignore, line, line) and line.strip():
                        lines.append(line.strip())


        # read everything into memory and then compare
        # after skipping lines which we shall ignore
        olines = []
        clines = []
        readlines(filename_original, olines)
        readlines(filename_compare, clines)

        if len(olines) != len(clines):
            return False

        for lo, lc in zip(olines, clines):
            if not self.applyfilters(lo, lc):
                self.diffs.append((lo, lc))
                result = False

        return result
