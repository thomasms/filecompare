from filecompare.utils.line import comparelines
from filecompare.compare.filelinecompare import FileLineCompare


class FileLineCompareWithFloatTolerance(FileLineCompare):
    def __init__(self, relative_tolerance, absolute_tolerance=0.0, custom_splitter=None):
        FileLineCompare.__init__(self)
        self.relative_tolerance = relative_tolerance
        self.absolute_tolerance = absolute_tolerance
        self.custom_splitter = custom_splitter

    def applyfilters(self, line1, line2):
        return comparelines(line1, line2, rel_tol=self.relative_tolerance, abs_tol=self.absolute_tolerance, custom_splitter=self.custom_splitter)
