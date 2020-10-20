# To print the sum of the series of 1+3+5+7+9.........Nth(Input N)

N = int(input("Enter the number of terms: "))
print("Using for Loop:")
sum1 = 0
c = 1
for i in range(N):
    print(c, end=" + ")
    sum1 += c
    c += 2

print("\nThe Sum is:", sum1)
print("")

print("Using while Loop:")
i = 0
sum2 = 0
c = 1
while i < N:
    print(c, end=" + ")
    sum2 += c
    c += 2
    i += 1

print("\nThe Sum is:", sum2)
