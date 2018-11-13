from CircularSubstring import circular_substring

str = "This is a cool string"

fp = "g"
sp = "gT"
tp = "gTh"
fop = "gThi"
fip = "gThis is a cool strin"

print(circular_substring(fp,str))
print(circular_substring(sp,str))
print(circular_substring(tp,str))
print(circular_substring(fop,str))
print(circular_substring(fip,str))