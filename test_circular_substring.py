from CircularSubstring import circular_substring

full_string = "This is a cool string"

fp = "g"
sp = "gT"
tp = "gTh"
fop = "gThi"
fip = "gThis is a cool strin"


if __name__ == "__main__":
    print(circular_substring(fp, full_string))
    print(circular_substring(sp, full_string))
    print(circular_substring(tp, full_string))
    print(circular_substring(fop, full_string))
    print(circular_substring(fip, full_string))