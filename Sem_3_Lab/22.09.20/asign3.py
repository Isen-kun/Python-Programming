# To check whether a number is prime or not.

n = int(input("Enter the number: "))
flag = 0

for i in range(2, n):
    if (n % i) == 0:
        flag = 1
        break

if flag == 1 or n == 1:
    print("The Entered number is a NOT a prime number.")
else:
    print("The Entered number is a prime number.")
