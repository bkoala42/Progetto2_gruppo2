from NewAVLTreeMap import NewAVLTreeMap

t = NewAVLTreeMap()
t[1] = "armando"
t[5] = "aaa"
t[3] = "gg"
t[10] = "bbb"

for i in t:
    print(i)

print(t.is_balanced(t.first()))
