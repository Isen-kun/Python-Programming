# To print the sum of the series of 1! + 2! + 3! + 4! +.........N!(Input N)

def fact(n):
    mul = 1
    for i in range(1, n+1):
        mul *= i
    return mul


N = int(input("Enter the value of N for N! term: "))
sum1 = 0
for i in range(1, N+1):
    print(str(i) + "!", end=" + ")
    sum1 += fact(i)

print("\nThe Sum is:", sum1)
print("")

print("Using while Loop:")
i = 1
sum2 = 0
while i <= N:
    print(str(i) + "!", end=" + ")
    sum2 += fact(i)
    i += 1

print("\nThe Sum is:", sum2)
