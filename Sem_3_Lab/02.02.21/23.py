string = input("Enter a string: ")
c = 0
for i in string:
    if (i == "a") or (i == "A") or (i == "e") or (i == "E") or (i == "i") or (i == "I") or (i == "o") or (i == "O") or (i == "u") or (i == "U"):
        c += 1
    else:
        continue
print("The total number of vowels in the string is: ", c)
