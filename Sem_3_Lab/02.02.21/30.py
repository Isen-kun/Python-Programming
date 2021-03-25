string1 = 'SHIFT'
for i in range(0, 6):
    string2 = string1[i:] + string1[:i]
    print(string2)
