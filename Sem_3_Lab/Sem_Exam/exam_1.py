name = input("Please input a name: ")
names = name.split()

print("\nThe abbreviated name is: ")
for i in range(0, len(names)):
    if i < len(names) - 1:
        print(names[i][0], end=". ")
    else:
        print(names[i])
