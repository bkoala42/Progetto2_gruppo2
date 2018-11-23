from pkg_4.CircularSubstring import circular_substring

full_string = "This is a cool string"


def test_string_not_present():
    pattern_not_present = "armando"
    another_pattern = "armandone"
    if not circular_substring(pattern_not_present, full_string) \
            and not circular_substring(another_pattern, full_string):
        print("Test test_string_not_present passed")
    else:
        print("Test test_string_not_present failed")


def test_string_not_circular():
    pattern, p = "ring", "g"
    if circular_substring(pattern, full_string) and circular_substring(p, full_string):
        print("Test test_string_not_circular passed")
    else:
        print("Test test_string_not_circular failed")


def test_circular_strings_all_cases():
    # All cases from 1 char up to n-1 char repeated circularly
    fp = "gT"           # first boundary case
    sp = "gTh"          # second
    tp = "gThi"         # third
    fop = "gThis"       # fourth
    fifp = "gThis "     # fifth
    sixp = "gThis i"    # sixth
    sevp = "gThis is"   # seventh
    eip = "gThis is "   # eight
    np = "gThis is a"   # ninth
    tenp = "gThis is a "    # tenth
    elep = "gThis is a c"   # eleventh
    twp = "gThis is a co"   # twelfth
    thip = "gThis is a coo"     # thirteenth
    fourp = "gThis is a cool"   # fourteenth
    fiftp = "gThis is a cool "  # fifteenth
    sixtp = "gThis is a cool s" # sixteenth
    sevep = "gThis is a cool st"    # seventeenth
    eighp = "gThis is a cool str"   # eighteenth
    ninp = "gThis is a cool stri"   # nineteenth
    lastp = "gThis is a cool strin"     # last boundary case

    if circular_substring(fp, full_string) and \
        circular_substring(sp, full_string) and \
        circular_substring(tp, full_string) and \
        circular_substring(fop, full_string) and \
        circular_substring(fifp, full_string) and \
        circular_substring(sixp, full_string) and \
        circular_substring(sevp, full_string) and \
        circular_substring(eip, full_string) and \
        circular_substring(np, full_string) and \
        circular_substring(tenp, full_string) and \
        circular_substring(elep, full_string) and \
        circular_substring(twp, full_string) and \
        circular_substring(thip, full_string) and \
        circular_substring(fourp, full_string) and \
        circular_substring(fiftp, full_string) and \
        circular_substring(sixtp, full_string) and \
        circular_substring(sevep, full_string) and \
        circular_substring(eighp, full_string) and \
        circular_substring(ninp, full_string) and \
            circular_substring(lastp, full_string):
        print("Test test_strings_circular passed")
    else:
        print("Test test_strings_circular failed")


def run_test_circular_substring():
    test_string_not_present()
    test_string_not_circular()
    test_circular_strings_all_cases()


if __name__ == "__main__":
    run_test_circular_substring()
