import unittest
import os
import sys
import filecompare as fc


class FileUnitTest(unittest.TestCase):
    def setUp(self):
        self.base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'testfiles')
        self.filename_original = os.path.join(self.base_dir, "original.txt")
        self.filename_compare_with_blank_lines = os.path.join(self.base_dir, "compare_text_and_chars_with_tolerance.txt")
        self.filename_empty = os.path.join(self.base_dir, "empty_file.txt")
        self.filename_empty_ws = os.path.join(self.base_dir, "empty_file_with_whitespace.txt")
    
    def test_str_in_file(self):
        self.assertEqual(fc.str_in_file(self.filename_original, "\n"), True)
        self.assertEqual(fc.str_in_file(self.filename_original, "\n\n\n"), True)
        self.assertEqual(fc.str_in_file(self.filename_original, "\n\n\n\n"), False)
        self.assertEqual(fc.str_in_file(self.filename_original, " "), True)
        self.assertEqual(fc.str_in_file(self.filename_original, "A"), True)
        self.assertEqual(fc.str_in_file(self.filename_original, "z"), False)
        self.assertEqual(fc.str_in_file(self.filename_original, "After some space"), True)
        self.assertEqual(fc.str_in_file(self.filename_original, "After some space, "), True)
        self.assertEqual(fc.str_in_file(self.filename_original, "After some space,, "), False)
        self.assertEqual(fc.str_in_file(self.filename_original, "The cat"), True)
        self.assertEqual(fc.str_in_file(self.filename_original, "The rat"), False)
        self.assertEqual(fc.str_in_file("there_is_no_such_file.txt", "The rat"), False)

    def test_nr_of_lines(self):
        # Although there are strictly 6 lines, the last empty line at the end of the file is removed
        self.assertEqual(fc.nr_of_lines(self.filename_original, ignore_empty_lines=False), 5)
        # Although there are strictly 6 lines, there are 3 empty lines
        self.assertEqual(fc.nr_of_lines(self.filename_original, ignore_empty_lines=True), 3)

        # Although there are strictly 14 lines, the last empty line at the end of the file is removed
        self.assertEqual(fc.nr_of_lines(self.filename_compare_with_blank_lines, ignore_empty_lines=False), 13)
        # Although there are strictly 14 lines, there are 10 empty lines
        self.assertEqual(fc.nr_of_lines(self.filename_compare_with_blank_lines, ignore_empty_lines=True), 5)

        self.assertEqual(fc.nr_of_lines(self.filename_empty, ignore_empty_lines=False), 0)
        self.assertEqual(fc.nr_of_lines(self.filename_empty, ignore_empty_lines=True), 0)

        self.assertEqual(fc.nr_of_lines(self.filename_empty_ws, ignore_empty_lines=False), 3)
        self.assertEqual(fc.nr_of_lines(self.filename_empty_ws, ignore_empty_lines=True), 0)

    def test_filename_without_extension(self):
        self.assertEqual(fc.get_filename_no_ext(os.path.realpath(__file__)), "fileunittests")
        self.assertEqual(fc.get_filename_no_ext(self.filename_original), "original")
        self.assertEqual(fc.get_filename_no_ext(self.filename_compare_with_blank_lines), "compare_text_and_chars_with_tolerance")
        self.assertEqual(fc.get_filename_no_ext(self.filename_empty), "empty_file")
        self.assertEqual(fc.get_filename_no_ext(self.filename_empty_ws), "empty_file_with_whitespace")

    def test_file_exists(self):
        self.assertEqual(fc.file_exists(os.path.realpath(__file__)), True)
        self.assertEqual(fc.file_exists(self.filename_original), True)
        self.assertEqual(fc.file_exists(self.filename_compare_with_blank_lines), True)
        self.assertEqual(fc.file_exists(self.filename_empty), True)
        self.assertEqual(fc.file_exists(self.filename_empty_ws), True)
        self.assertEqual(fc.file_exists("It_is_very_likely_this_file_does_not_exist.txt"), False)
        self.assertEqual(fc.file_exists(os.path.dirname(os.path.realpath(__file__))), False)
        self.assertEqual(fc.file_exists(os.path.dirname(sys.path[0])), False)
        self.assertEqual(fc.file_exists(sys.path[0]), False)
        self.assertEqual(fc.file_exists(self.base_dir), False)
    
    def test_dir_exists(self):
        self.assertEqual(fc.dir_exists(os.path.dirname(os.path.realpath(__file__))), True)
        self.assertEqual(fc.dir_exists(os.path.dirname(sys.path[0])), True)
        self.assertEqual(fc.dir_exists(sys.path[0]), True)
        self.assertEqual(fc.dir_exists(self.base_dir), True)
        self.assertEqual(fc.dir_exists("It_is_very_likely_this_dir_does_not_exist"), False)
        self.assertEqual(fc.dir_exists(os.path.join(os.path.dirname(os.path.abspath(__file__)),"It_is_very_likely_this_dir_does_not_exist")), False)
        self.assertEqual(fc.dir_exists(os.path.realpath(__file__)), False)
        self.assertEqual(fc.dir_exists(self.filename_original), False)
        self.assertEqual(fc.dir_exists(self.filename_compare_with_blank_lines), False)
        self.assertEqual(fc.dir_exists(self.filename_empty), False)
        self.assertEqual(fc.dir_exists(self.filename_empty_ws), False)

    # disabled incase users do not have permissions to do this
    # ToDo: Implement using python mock testing
    def _test_make_rm_dir(self):
        temp_dir_name = 'temp_dir'
        temp_dir = os.path.join(self.base_dir, temp_dir_name)
        
        fc.rm_dir(temp_dir)
        self.assertEqual(fc.dir_exists(temp_dir), False)
        
        fc.make_dir(temp_dir)
        self.assertEqual(fc.dir_exists(temp_dir), True)
        
        fc.rm_dir(temp_dir)
        self.assertEqual(fc.dir_exists(temp_dir), False)

    # disabled incase users do not have permissions to do this
    # ToDo: Implement using python mock testing
    def _test_file_copy(self):
        temp_dir_name = 'temp_file_copy_dir'
        temp_dir = os.path.join(self.base_dir, temp_dir_name)
        
        file_to_copy = os.path.join(temp_dir, os.path.basename(self.filename_original))
        
        fc.rm_dir(temp_dir)
        self.assertEqual(fc.dir_exists(temp_dir), False)
        
        fc.make_dir(temp_dir)
        self.assertEqual(fc.dir_exists(temp_dir), True)
        
        # do the directory copy and check the new file exists
        self.assertEqual(fc.file_exists(file_to_copy), False)
        fc.file_copy(self.filename_original, file_to_copy)
        self.assertEqual(fc.file_exists(file_to_copy), True)
        
        # remove the temp directory and check the new file no longer exists
        # but that the old still remains
        fc.rm_dir(temp_dir)
        self.assertEqual(fc.dir_exists(temp_dir), False)
        self.assertEqual(fc.file_exists(file_to_copy), False)
        self.assertEqual(fc.file_exists(self.filename_original), True)

    # disabled incase users do not have permissions to do this
    # ToDo: Implement using python mock testing
    def _test_dir_copy(self):
        temp_dir_name = 'temp_dir_copy_dir'
        
        # cannot be a sub directory, otherwise it will be an infinite loop
        temp_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), temp_dir_name)
        
        dir_to_copy = self.base_dir
        new_dir = os.path.join(temp_dir, os.path.basename(dir_to_copy))
        
        fc.rm_dir(temp_dir)
        self.assertEqual(fc.dir_exists(temp_dir), False)
        
        fc.make_dir(temp_dir)
        self.assertEqual(fc.dir_exists(temp_dir), True)
        
        # do the directory copy and check files exist
        self.assertEqual(fc.dir_exists(new_dir), False)
        fc.file_copy(dir_to_copy, new_dir)
        self.assertEqual(fc.dir_exists(new_dir), True)
        self.assertEqual(fc.file_exists(os.path.join(new_dir, os.path.basename(self.filename_original))), True)
        self.assertEqual(fc.file_exists(os.path.join(new_dir, os.path.basename(self.filename_compare_with_blank_lines))), True)
        self.assertEqual(fc.file_exists(os.path.join(new_dir, os.path.basename(self.filename_empty))), True)
        self.assertEqual(fc.file_exists(os.path.join(new_dir, os.path.basename(self.filename_empty_ws))), True)
        
        # remove the new directory check the new files no longer exist
        fc.rm_dir(temp_dir)
        self.assertEqual(fc.dir_exists(temp_dir), False)
        self.assertEqual(fc.dir_exists(new_dir), False)
        self.assertEqual(fc.file_exists(os.path.join(new_dir, os.path.basename(self.filename_original))), False)
        self.assertEqual(fc.file_exists(os.path.join(new_dir, os.path.basename(self.filename_compare_with_blank_lines))), False)
        self.assertEqual(fc.file_exists(os.path.join(new_dir, os.path.basename(self.filename_empty))), False)
        self.assertEqual(fc.file_exists(os.path.join(new_dir, os.path.basename(self.filename_empty_ws))), False)

        # check the original files still exist
        self.assertEqual(fc.file_exists(self.filename_original), True)
        self.assertEqual(fc.file_exists(self.filename_compare_with_blank_lines), True)
        self.assertEqual(fc.file_exists(self.filename_empty), True)
        self.assertEqual(fc.file_exists(self.filename_empty_ws), True)

    def test_replace_in_file1(self):
        def strip_white_space(string):
            return string.replace("\n", "").replace(" ", "")
        
        files_file = os.path.join(self.base_dir, "files")
        self.maxDiff = None
        newstr = fc.replace_in_file(files_file, r'\S+nuclear_data\/' , "/path/to/nuclear_data/")
        expectedstr = """# gamma attenuation data
            absorp  /path/to/nuclear_data/EAF2010data/eaf_abs_20100
            
            # index of nuclides to be included
            ind_nuc  /path/to/nuclear_data/EAF2010data/eaf_index_20100
            
            # Library cross section data
            enbins /path/to/nuclear_data/EAF2010data/ebins_66
            crossec  /path/to/nuclear_data/EAF2010data/eaf_n_gxs_066_fis_20100
            crossunc  /path/to/nuclear_data/EAF2010data/eaf_un_20100
            
            # fluxes
            fluxes  fluxes
            
            # Library decay data
            decay  /path/to/nuclear_data/EAF2010data/eaf_dec_20100.001
            
            # Library fission  data
            asscfy  /path/to/nuclear_data/EAF2010data/eaf_n_asscfy_20100
            fissyld  /path/to/nuclear_data/EAF2010data/eaf_n_fis_20100
            
            # Library regulatory data
            hazards  /path/to/nuclear_data/EAF2010data/eaf_haz_20100
            clear  /path/to/nuclear_data/EAF2010data/eaf_clear_20100
            a2data  /path/to/nuclear_data/EAF2010data/eaf_a2_20100
            
            # collapsed cross section data (in and out)
            collapxi  COLLAPX
            collapxo  COLLAPX
            
            # condensed decay and fission data (in and out)
            arrayx  ARRAYX
            """
        self.assertEqual(strip_white_space(expectedstr), strip_white_space(newstr))


    def test_replace_in_file2(self):
        def strip_white_space(string):
            return string.replace("\n", "").replace(" ", "")
        
        collapse_input = os.path.join(self.base_dir, "collapse.i")
        self.maxDiff = None
        newstr = fc.replace_in_file(collapse_input, r'(\bGETXS\b)([\t\f ]+-1 )' , "GETXS 1")
        expectedstr = """<< -----collapse cross section data----- >>
            NOERROR
            PROJ 4
            GETXS 1 1
            FISPACT
            * TENDL gxs-162: alpha   1 MeV - 200 MeV
            PRINTLIB 4
            END
            * END OF RUN
            """
        self.assertEqual(strip_white_space(expectedstr), strip_white_space(newstr))

    def test_replace_in_file3(self):
        def strip_white_space(string):
            return string.replace("\n", "").replace(" ", "")
        
        collapse_input = os.path.join(self.base_dir, "collapse2.i")
        self.maxDiff = None
        newstr = fc.replace_in_file(collapse_input, r'(\bGETXS\b)([\t\f ]+-?1 )' , "GETXS 2364")
        expectedstr = """<< -----collapse cross section data----- >>
            NOERROR
            PROJ 4
            GETXS 2364 1
            FISPACT
            * TENDL gxs-162: alpha   1 MeV - 200 MeV
            PRINTLIB 4
            END
            * END OF RUN
            """
        self.assertEqual(strip_white_space(expectedstr), strip_white_space(newstr))

    def test_replace_in_file4(self):
        def strip_white_space(string):
            return string.replace("\n", "").replace(" ", "")
        
        collapse_input = os.path.join(self.base_dir, "collapse3.i")
        self.maxDiff = None
        newstr = fc.replace_in_file(collapse_input, r'(\bGETXS\b)([\t\f ]+-1 )' , "GETXS 1")
        expectedstr = """<< -----collapse cross section data----- >>
            NOERROR
            PROJ 4
            GETXS -10 1
            FISPACT
            * TENDL gxs-162: alpha   1 MeV - 200 MeV
            PRINTLIB 4
            END
            * END OF RUN
            """
        self.assertEqual(strip_white_space(expectedstr), strip_white_space(newstr))

    def test_replace_in_file5(self):
        def strip_white_space(string):
            return string.replace("\n", "").replace(" ", "")
        
        collapse_input = os.path.join(self.base_dir, "collapse4.i")
        self.maxDiff = None
        newstr = fc.replace_in_file(collapse_input, r'(\bGETXS\b)([\t\f ]+-1 )' , "GETXS 732")
        expectedstr = """<< -----collapse cross section data----- >>
            NOERROR
            PROJ 4
            GETXS 1 1
            FISPACT
            * TENDL gxs-162: alpha   1 MeV - 200 MeV
            PRINTLIB 4
            END
            * END OF RUN
            """
        self.assertEqual(strip_white_space(expectedstr), strip_white_space(newstr))

    def test_replace_in_file6(self):
        def strip_white_space(string):
            return string.replace("\n", "").replace(" ", "")
        
        collapse_input = os.path.join(self.base_dir, "collapse4.i")
        self.maxDiff = None
        newstr = fc.replace_in_file(collapse_input, r'(\bGETXS\b)([\t\f ]+-?1 )' , "GETXS 732")
        expectedstr = """<< -----collapse cross section data----- >>
            NOERROR
            PROJ 4
            GETXS 732 1
            FISPACT
            * TENDL gxs-162: alpha   1 MeV - 200 MeV
            PRINTLIB 4
            END
            * END OF RUN
            """
        self.assertEqual(strip_white_space(expectedstr), strip_white_space(newstr))
