import unittest
import math
from filecompare.utils.line import comparelines


class LineUnitTest(unittest.TestCase):

    def test_compare_no_tolerance(self):
        self.assertEqual(comparelines("g h 123", "g h 123"), True)
        self.assertEqual(comparelines("g h 1213", "g h 123"), False)
        self.assertEqual(comparelines("g h 12.3", "g h 123"), False)
        self.assertEqual(comparelines("1e9", "1e9"), True)
        self.assertEqual(comparelines("1e-9", "1e+9"), False)
        self.assertEqual(comparelines("1e9", "1e+9"), True)
        self.assertEqual(comparelines("1e9 1e-9", "1e+9 1e-9"), True)
        self.assertEqual(comparelines("1e9 1e-9", "1e+9 1e+9"), False)

    def test_compare_no_tolerance_customsplitter(self):
        self.assertEqual(comparelines("g h 123", "g h 123", custom_splitter="-"), True)
        self.assertEqual(comparelines("g h 1213", "g h 123", custom_splitter="-"), False)
        self.assertEqual(comparelines("g h 12.3", "g h 123", custom_splitter="-"), False)
        self.assertEqual(comparelines("1e9", "1e9", custom_splitter="-"), True)
        self.assertEqual(comparelines("1e-9", "1e+9", custom_splitter="-"), False)
        self.assertEqual(comparelines("1e9", "1e+9", custom_splitter="-"), True)
        self.assertEqual(comparelines("1e9 1e-9", "1e+9 1e-9", custom_splitter="-"), True)
        self.assertEqual(comparelines("1e9 1e-9", "1e+9 1e+9", custom_splitter="-"), False)
        
        line1 = 'Li  7 (n,2n   ) Li  6  7.111E-06+-2.0E+01 Li  7 (n,na   ) H   3  7.263E-03+-1.0E+02 Li  7 (n,g    ) Li  8  3.680E-03+-9.7E+00 Li  7 (n,d    ) He  6  2.867E-07+-6.0E+01'
        self.assertEqual(comparelines(line1, line1), True)
        self.assertEqual(comparelines(line1, line1, custom_splitter=" "), True)
        self.assertEqual(comparelines(line1, line1, custom_splitter="?"), True)
        self.assertEqual(comparelines(line1, line1, custom_splitter="-"), True)
        self.assertEqual(comparelines(line1, line1, custom_splitter="+"), True)
        self.assertEqual(comparelines(line1, line1, custom_splitter="+-"), True)

    def test_compare_with_tolerance_customsplitter(self):
        line1 = 'Li  7 (n,2n   ) Li  6  7.111E-06+-2.0E+01 Li  7 (n,na   ) H   3  7.263E-03+-1.0E+02 Li  7 (n,g    ) Li  8  3.680E-03+-9.7E+00 Li  7 (n,d    ) He  6  2.867E-07+-6.0E+01'
        line2 = 'Li  7 (n,2n   ) Li  6  7.113E-06+-2.01E+01 Li  7 (n,na   ) H   3  7.264E-03+-1.0E+02 Li  7 (n,g    ) Li  8  3.680E-03+-9.7E+00 Li  7 (n,d    ) He  6  2.869E-07+-6.0E+01'
        
        self.assertEqual(comparelines(line1, line2), False)
        self.assertEqual(comparelines(line1, line2, custom_splitter=" "), False)
        self.assertEqual(comparelines(line1, line2, custom_splitter="?"), False)
        self.assertEqual(comparelines(line1, line2, custom_splitter="-"), False)
        self.assertEqual(comparelines(line1, line2, custom_splitter="+"), False)
        self.assertEqual(comparelines(line1, line2, custom_splitter="+-"), False)
        self.assertEqual(comparelines(line1, line2, rel_tol=0.01, custom_splitter=" "), False)
        self.assertEqual(comparelines(line1, line2, rel_tol=0.01, custom_splitter="?"), False)
        self.assertEqual(comparelines(line1, line2, rel_tol=0.01, custom_splitter="-"), False)
        self.assertEqual(comparelines(line1, line2, rel_tol=0.01, custom_splitter="+"), False)
        self.assertEqual(comparelines(line1, line2, rel_tol=0.01, custom_splitter="+-"), True)
