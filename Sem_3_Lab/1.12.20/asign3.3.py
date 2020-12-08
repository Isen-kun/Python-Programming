# To find the sum of the series 1! + 2! + 3! + .....

n = int(input("Enter the no of terms of the series: "))


def r_fact(n):
    if n == 0:
        return 1
    else:
        return n*r_fact(n-1)


def ser(n):
    sum = 0
    for i in range(1, n+1):
        f = r_fact(i)
        print(str(i) + "!(" + str(f) + ")", end=" + ")
        sum += f
    print("\nThe sum is:", sum)


print("The given series is: ")
ser(n)
