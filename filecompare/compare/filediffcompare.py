from difflib import Differ

from filecompare.compare.filesimplecompare import FileSimpleCompare


class FileLineDiffCompare(FileSimpleCompare):
    def __init__(self):
        self.diffs = []

    def __call__(self, filename_original, filename_compare):
        self.diffs = []
        FileSimpleCompare.validate(filename_original)
        FileSimpleCompare.validate(filename_compare)

        result = True
        with open(filename_original) as fo, open(filename_compare) as fc:
            differ = Differ()
            for line in differ.compare(fo.readlines(), fc.readlines()):
                # from https://docs.python.org/2/library/difflib.html
                # - " " means lines are identical
                if not line.startswith(' '):
                    self.diffs.append(line)
                    result = False

        return result

