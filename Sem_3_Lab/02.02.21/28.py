string1 = input("Enter a string: ")
space1 = string1.find(' ')
space2 = string1.find(' ', space1+1)
string2 = string1[0] + '. ' + \
    string1[space1+1] + '. ' + string1[space2+1] + '.'
print("INITIALS: ", string2)
