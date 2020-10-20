# To print the sum of the series of 1+2+3+4+.........N(Input N)

N = int(input("Enter the nth term: "))
print("Using for Loop:")
sum1 = 0
for i in range(1, N+1):
    print(i, end=" + ")
    sum1 += i

print("\nThe Sum is:", sum1)
print("")

print("Using while Loop:")
i = 1
sum2 = 0
while i <= N:
    print(i, end=" + ")
    sum2 += i
    i += 1

print("\nThe Sum is:", sum2)
