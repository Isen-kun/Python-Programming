def rect_area():
    l = int(input("Enter rectangle's length: "))
    b = int(input("Enter rectangle's breadth: "))
    ar = l * b
    print("The area of rectangle is", ar)


def tri_area():
    h = int(input("Enter triangle's height length: "))
    b = int(input("Enter triangle's breadth length: "))
    ar = 0.5 * b * h
    print("The area of triangle is", ar)


def cir_area():
    r = int(input("Enter circle's radius length: "))
    pi = 3.14
    ar = pi * r * r
    print("The area of triangle is", ar)


while(1):
    choice = int(input(
        "Select the name of shape whose area you want to find: \n 1. rectangle. \n 2. Triangle \n 3. circle. \n 4. Exit. \n"))
    if choice == 1:
        rect_area()
    elif choice == 2:
        tri_area()
    elif choice == 3:
        cir_area()
    elif choice == 4:
        break
    else:
        print("Sorry! This shape is not available")
