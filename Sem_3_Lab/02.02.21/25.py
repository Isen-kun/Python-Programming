string1 = input("Enter a string : ")
string2 = string1[-1:] + string1[1:-1] + string1[:1]
print("The new string :", string2)
