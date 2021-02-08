from filecompare.utils.numerical import isfloat, getfloat, arevaluesthesame


def comparelines(line1, line2, rel_tol=0.0, abs_tol=0.0, custom_splitter=None):
    # if exactly the same then true
    # otherwise we need to compare using tolerance to floats
    if line1 == line2:
        return True

    l1 = line1.strip('\n').split(' ')
    l2 = line2.strip('\n').split(' ')

    strings_lo = [d for d in l1 if d and not isfloat(d)]
    strings_lc = [d for d in l2 if d and not isfloat(d)]

    numbers_lo = [getfloat(d) for d in l1 if isfloat(d)]
    numbers_lc = [getfloat(d) for d in l2 if isfloat(d)]
            
    # if the strings do not match, then apply custom splitter and try again
    # if it fails after the splitter, return false
    if strings_lo != strings_lc:
        # if defined, apply custom splitter, such as +-, to strings
        if custom_splitter is not None:
            _applycustomsplitter(strings_lo, numbers_lo, custom_splitter)
            _applycustomsplitter(strings_lc, numbers_lc, custom_splitter)
            if strings_lo != strings_lc:
                return False
        else:
            return False

    # if no numbers in either file, it is purely text, then it should fail
    if not numbers_lc or not numbers_lo:
        return False

    # apply tolerances only if the same number of values exist per line
    if len(numbers_lc) == len(numbers_lo):
        for i in range(0, len(numbers_lc)):
            if not arevaluesthesame(numbers_lo[i], numbers_lc[i], rel_tol, abs_tol=abs_tol):
                return False
    else:
        return False

    return True

# if defined, apply custom splitter, such as +-, to strings
def _applycustomsplitter(string_list, numerical_list, splitter):
    s_indices_to_remove = []
    for s in range(0, len(string_list)):
        nl = string_list[s].split(splitter)
        if len(nl) > 1 and all(isfloat(item) == True for item in nl):
            s_indices_to_remove.append(s)
            for n in nl:
                numerical_list.append(getfloat(n))

    # remove from string list in reverse order!!
    for s in s_indices_to_remove[::-1]:
        string_list.pop(s)
