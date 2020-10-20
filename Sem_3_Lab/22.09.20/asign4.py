# To find the sum of all Prime numbers in a given range

a = int(input("Enter the lower limit: "))
b = int(input("Enter the upper limit: "))
sum = 0
print("The prime numbers:")
for i in range(a, b+1):
    flag = 0
    for j in range(2, i):
        if (i % j) == 0:
            flag = 1
            break
    if flag == 0:
        print(i, end=", ")
        sum += i

print("\nThe sum is", sum)
