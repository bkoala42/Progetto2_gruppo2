from CircularSubstring import circular_substring

full_string = "This is a cool string"

fp = "g"
sp = "gT"
tp = "gTh"
fop = "gThi"
fip = "gThis is a cool strin"


def test_string_not_present():
    pattern_not_present = "armando"
    another_pattern = "armandone"
    if not circular_substring(pattern_not_present, full_string) \
            and not circular_substring(another_pattern, full_string):
        print("Test test_string_not_present passed")
    else:
        print("Test test_string_not_present failed")


def run_test_circular_substring():
    test_string_not_present()


if __name__ == "__main__":
    run_test_circular_substring()
