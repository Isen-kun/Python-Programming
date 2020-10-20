# To find the sum of all the odd and even numbers between 1-100

sum1 = 0
sum2 = 0

print("The Odd numbers:")
for i in range(1, 101):
    if i % 2 != 0:
        print(i, end=", ")
        sum1 += i
print("\nThe sum of Odd numbers is:", sum1)
print("")
print("The Even numbers:")
for i in range(1, 101):
    if i % 2 == 0:
        print(i, end=", ")
        sum2 += i
print("\nThe sum of Even numbers is:", sum2)
