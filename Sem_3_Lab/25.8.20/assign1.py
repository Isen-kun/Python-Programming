# Swap the variables with/out third variable

# swap with third variable
a = int(input("Enter the first number "))
b = int(input("Enter the second number "))

temp = a
a = b
b = temp
print("The swapped values are", a, b)

# swap without third variable
c = int(input("Enter the first number "))
d = int(input("Enter the second number "))

c = c+d
d = c-d
c = c-d
print("The swapped values are", c, d)
