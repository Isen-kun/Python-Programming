s = input("Enter Password: ")
u = 0
l = 0
n = 0
a = 0
if(len(s) >= 8):
    for i in s:
        if(i.isupper == False):
            u = 1
            if(u == 1):
                print("Code is Invalid")
                break
        elif(i.islower == False):
            l = 1
            if(l == 1):
                print("Code is Invalid")
                break
        elif(i.isnumeric == False):
            n = 1
            if(n == 1):
                print("Code is Invalid")
                break
        elif(i.isprintable == True and s[i].isalnum == False):
            a = 1
            if(a == 1):
                print("Code is Invalid")
                break
    if(u == 0 and l == 0 and n == 0 and a == 0):
        print("Its a valid password")


else:
    print("Its not a valid password")
