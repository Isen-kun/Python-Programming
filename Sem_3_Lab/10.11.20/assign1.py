# To check armstrong numbers within a range

a = int(input("Enter the lower limit: "))
b = int(input("Enter the upper limit: "))
cnt = 0

print("The Armstrong numbers:")
for i in range(a,b+1):
    power = len(str(i))
    c = i
    sum = 0
    while c>0:
        sum += (c%10) ** power
        c //= 10
    if sum == i:
        print(i, end=" ")
        cnt +=1
print("\nThe number of Armsrong numbers: ", cnt)

