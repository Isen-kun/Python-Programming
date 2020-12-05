# Factorial of a given number using function

n=int(input("Enter a number: "))

def fact(n):
    mul=1
    while n>0:
        mul*=n
        n-=1
    return mul

print("The factorial of the number is:",fact(n))    