# To find the sum of the series 1 + 1/4 + 1/9 +....

n = int(input("Enter the no of terms of the series: "))


def ser(n):
    sum = 0
    for i in range(1, n+1):
        print(str(1)+"/"+str(i**2), end=" + ")
        sum += 1/(i**2)
    print("\nThe sum is:", sum)


print("The given series is: ")
ser(n)
