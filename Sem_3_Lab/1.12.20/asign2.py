# GCD and LCM of a given number using functions

n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))

def Gcd(a,b):
    if a == 0:
        return b
    return Gcd(b % a, a)

def Lcm(a,b):
    return (a // Gcd(a,b))* b

print("The GCD of the two numbers is:", Gcd(n1,n2))
print("The LCM of the two numbers is:", Lcm(n1,n2))