import json

from filecompare.compare.filesimplecompare import FileSimpleCompare
from filecompare.utils.numerical import isfloat, getfloat, arevaluesthesame


class JSONFileCompare(FileSimpleCompare):
    """
        Compare two JSON files with tolerance and ignores
    """
    def __init__(self, relative_tolerance=0.0, absolute_tolerance=0.0):
        self.relative_tolerance = relative_tolerance
        self.absolute_tolerance = absolute_tolerance
        
        # diffs are a list of key, value pairs
        # values are the differences
        self.diffs = []

    def __call__(self, filename_original, filename_compare, ignore=[]):
        self.diffs = []
        FileSimpleCompare.validate(filename_original)
        FileSimpleCompare.validate(filename_compare)

        with open(filename_original) as fo, open(filename_compare) as fc:
            odata = json.loads(fo.read())
            cdata = json.loads(fc.read())

            return self.compare(odata, cdata, ignore=ignore)

    def compare(self, data_original, data_compare, lastkey=None, ignore=[]):
        # is a dictionary?
        if type(data_original) is dict:
            if type(data_compare) != dict:
                return False

            # iterate over dictionary keys
            for key, value in data_original.items():
                lastkey = key
                if key in ignore:
                    continue
                if key not in data_compare:
                    self.diffs.append((key, "Not found in compare"))
                    return False
                if not self.compare(value, data_compare[key], lastkey=key, ignore=ignore):
                    return False

            return True

        # is a list?
        if type(data_original) is list:
            if type(data_compare) != list:
                self.diffs.append(("key {} is list, length ={}".format(lastkey, len(data_original)),
                                   "key {} is not a list".format(lastkey) ))
            if len(data_original) != len(data_compare):
                self.diffs.append(("key {} is list, length ={}".format(lastkey, len(data_original)),
                                   "key {} is list, length ={}".format(lastkey, len(data_compare)) ))
                return False

            # iterate over list items
            for indx, value in enumerate(data_original):
                if (not self.compare(value, data_compare[indx], lastkey=lastkey, ignore=ignore)):
                    return False

            return True

        # apply tolerance to numbers
        if isfloat(data_original):
            if not arevaluesthesame(getfloat(data_original),
                                    getfloat(data_compare),
                                    self.relative_tolerance,
                                    abs_tol=self.absolute_tolerance):
                self.diffs.append((getfloat(data_original), getfloat(data_compare)))
                return False

            return True

        # else assert strings
        if data_original != data_compare:
            self.diffs.append((data_original, data_compare))
            return False
        
        return True
