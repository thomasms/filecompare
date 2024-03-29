def arevaluesthesame(value1, value2, relative_tolerance, abs_tol=0.0):
    # Use math.isclose algorithm, it is better than numpy.isclose method.
    # See https://github.com/numpy/numpy/issues/10161 for more on the discussion
    # Since some python version don't come with math.isclose we implement it here directly
    
    return abs(value1 - value2) <= max(relative_tolerance * max(abs(value1), abs(value2)), abs_tol)


def getfloat(value):
    """
        Gets the floating point value from a string
        Will allow for fortran style floats, i.e -2.34321-308
        If it is neither then it will return "nan"
    """
    if istradiationalfloat(value):
        return float(value)
    else:
        return getfortranfloat(value)


def istradiationalfloat(value):
    """
        Checks if the string can be converted to a floating point value
        Does not allow for fortran style floats, i.e -2.34321-308
        only standard floats.
    """
    try:
        float(value)
        return True
    except ValueError:
        return False

def isfloat(value):
    """
        Checks if the string can be converted to a floating point value
        Will allow for fortran style floats, i.e -2.34321-308
        If it is neither then it will return False
    """
    return (istradiationalfloat(value) or isfortranfloat(value))


def isfortranfloat(value):
    passfunc = lambda sign, esign, parts: True
    failfunc = lambda: False
    
    return _fortranfloat(value, passfunc, failfunc)


def getfortranfloat(value):
    passfunc = lambda sign, esign, parts: float(sign + parts[0] + 'E' + esign + parts[1])
    failfunc = lambda: "nan"
    
    return _fortranfloat(value, passfunc, failfunc)


def _fortranfloat(value, passfunc, failfunc):
    # could be 2.3
    #          2.3e+10
    #          -2.3e+10
    #          -2.3+10
    #          -2.3-10
    #          2.3-10
    #          +2.3-10
    #          +2.3+10
    #          -2.3+10
    
    signs = ['-', '+']
    
    valueasstring = str(value)
    sign = ""
    if len(valueasstring) > 0:
        # check for sign at the front
        if valueasstring[0] in signs:
            sign = valueasstring[0]
            valueasstring = valueasstring[1:]

        # cannot have both separators in the value for a valid float
        if not all(s in valueasstring for s in signs):
            # check the values in both parts recursively
            for sn in signs:
                if sn in valueasstring:
                    parts = valueasstring.split(sn, 1)
                    if istradiationalfloat(parts[0]) and \
                       istradiationalfloat(parts[1]) and \
                       '.' in parts[0] and not '.' in parts[1]:
                        return passfunc(sign, sn, parts)
    return failfunc()
