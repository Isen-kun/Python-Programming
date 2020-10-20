# python 3 program to add, sub, mul, int-div, flt-div, rem, pow

a = int(input('\nEnter the first number:'))
b = int(input('Enter the second number:'))

print("\nThe addition of", a, "and", b, "is = ", a+b)
print("The substraction of {0} and {1} = {2}".format(a, b, a-b))
print("The multiplication of %d and %d = %d" % (a, b, a*b))
print("The integer division of", a, "and", b, "is =", a//b)
print("The float division of", a, "and", b, "is =", a/b)
print("The remainder division of {0} and {1} = {2}".format(a, b, a % b))
print("The %d to the power %d = %d" % (a, b, a**b))
