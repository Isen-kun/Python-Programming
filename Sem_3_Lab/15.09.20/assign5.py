# To print the sum of the series of 1 - 1/3 + 1/9 - 1/27 + 1/81-.........Nth term(Input N)

N = int(input("Enter the number of terms: "))
print("Using for Loop:")
sum1 = 0
for i in range(N):
    if i % 2 == 0:
        print(str(1) + "/" + str(3**i), end=" - ")
        sum1 += 1/(3**i)
    else:
        print(str(1) + "/" + str(3**i), end=" + ")
        sum1 -= 1/(3**i)

print("\nThe Sum is:", sum1)
print("")

print("Using while Loop:")
i = 0
sum2 = 0
while i < N:
    if i % 2 == 0:
        print(str(1) + "/" + str(3**i), end=" - ")
        sum2 += 1/(3**i)
    else:
        print(str(1) + "/" + str(3**i), end=" + ")
        sum2 -= 1/(3**i)
    i += 1

print("\nThe Sum is:", sum2)
