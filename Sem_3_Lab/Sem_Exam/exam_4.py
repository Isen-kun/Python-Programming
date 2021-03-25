lst = []
flag = 0
n = int(input("Enter number of elements of the list: "))

for i in range(0, n):
    x = int(input())
    lst.append(x)

for i in range(len(lst)):
    for j in range(len(lst)):
        if i != j:
            if lst[i] == lst[j]:
                flag = 1

if(flag == 0):
    print("All the elements in the list are unique")
else:
    print("All the elements in the list are NOT unique")
