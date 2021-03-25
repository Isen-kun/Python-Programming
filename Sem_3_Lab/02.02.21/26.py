string1 = input("Input a word to reverse: ")
string2 = []
string3 = ""

for i in range(len(string1) - 1, -1, -1):
    string2 += string1[i]

for j in string1:
    string3 = j + string3

print("The reversed string is:", ''.join(string2))
print("The reversed string is:", string3)
