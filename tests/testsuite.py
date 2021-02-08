import unittest

from tests.filediffcompareunittests import FileDiffCompareUnitTest
from tests.filesimplecompareunittests import FileSimpleCompareUnitTest
from tests.filelinecompareunittests import FileLineCompareUnitTest
from tests.filelinecomparewithfloattoleranceunittests import FileLineCompareWithFloatToleranceUnitTest
from tests.filelinecomparedifflineswithtoleranceunittests import FileLineCompareDiffLinesWithToleranceUnitTest
from tests.numericalunittests import NumericalUnitTest
from tests.fileunittests import FileUnitTest
from tests.lineunittests import LineUnitTest
from tests.jsonfilecompareunittests import JSONFileCompareUnitTest


tests = [
         FileDiffCompareUnitTest,
         FileSimpleCompareUnitTest,
         FileLineCompareUnitTest,
         FileLineCompareWithFloatToleranceUnitTest,
         FileLineCompareDiffLinesWithToleranceUnitTest,
         NumericalUnitTest,
         FileUnitTest,
         LineUnitTest,
         JSONFileCompareUnitTest
         ]

fcsuite = unittest.TestSuite([unittest.TestLoader().loadTestsFromTestCase(tc) for tc in tests])

def main():
    unittest.TextTestRunner(verbosity=3).run(fcsuite)

if __name__ == '__main__':
    unittest.main()

