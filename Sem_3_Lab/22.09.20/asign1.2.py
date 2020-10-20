# To print the given pattern

n = int(input("Enter the number of rows: "))

for i in range(n, 0, -1):
    k = n-i
    print("  "*k, end=" ")
    for j in range(i):
        print(" * ", end=" ")
    print("")
