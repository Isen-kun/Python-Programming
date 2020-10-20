# to generate the PASCAL's triangle upto specified number of rows.

n = int(input("Enter the number of rows: "))

for i in range(n):
    s = n-i
    print("  "*s, end=" ")
    for j in range(i+1):
        res = 1
        if j > i - j:
            j = i - j
        for k in range(j):
            res *= (i - k)
            res //= (k + 1)
        print(res, end="   ")
    print("")
