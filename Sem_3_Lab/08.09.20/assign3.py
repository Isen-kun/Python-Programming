# To grade the average of five marks

a = int(input("Enter the marks "))
b = int(input("Enter the marks "))
c = int(input("Enter the marks "))
d = int(input("Enter the marks "))
e = int(input("Enter the marks "))

avg = (a+b+c+d+e)/5

if avg >= 90 and avg <= 100:
    g = "O"
elif avg >= 80:
    g = "E"
elif avg >= 70:
    g = "A"
elif avg >= 60:
    g = "B"
elif avg >= 50:
    g = "C"
elif avg >= 40:
    g = "D"
else:
    g = "FAIL"

print("The grade of the student is", g)
