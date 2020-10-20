# Python 3 program to add two numbers

a = int(input('enter the first number:'))
b = int(input('enter the second number:'))
print(type(a))
print(type(b))
c = a+b

print('the addition of {0} and {1}={2}'.format(a, b, c))
print("the addition of", a, " and ", b, " is = ", c)
print("the addition of %d and %d = %f" % (a, b, c))
