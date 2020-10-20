# To compute the factorial of a number

N = int(input("Enter a number: "))

mul = 1
for i in range(1, N+1):
    mul *= i

print("The factorial of the number is:", mul)
