import os
import filecmp

from filecompare.utils.file import content_as_str, file_exists


class FileSimpleCompare:

    # do the comparison
    # returns True if they are exactly the same, False otherwise
    def __call__(self, filename_original, filename_compare):
        FileSimpleCompare.validate(filename_original)
        FileSimpleCompare.validate(filename_compare)
        return filecmp.cmp(filename_original, filename_compare)

    @staticmethod
    def contents(filename):
        FileSimpleCompare.validate(filename)
        return content_as_str(filename)

    @staticmethod
    def validate(filename):
        if not file_exists(filename):
            raise FileNotFoundError('The file: {0} does not exist.'.format(filename))
