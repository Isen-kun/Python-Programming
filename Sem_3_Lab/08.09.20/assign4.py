# To check whether a year is a leap year or not

y = int(input("Enter a year "))
if y % 400 == 0 or (y % 100 != 0 and y % 4 == 0):
    print("Its a leap year")
else:
    print("Its not a leap year")
