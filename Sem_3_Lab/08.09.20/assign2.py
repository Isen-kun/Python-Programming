# To find the largest of three numbers

a = int(input("Enter the First Number "))
b = int(input("Enter the Second Number "))
c = int(input("Enter the Third Number "))

if a > b and a > c:
    print(a, "is the largest number")
elif b > c and b > a:
    print(b, "is the largest number")
else:
    print(c, "is the largest number")
