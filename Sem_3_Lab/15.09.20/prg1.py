s1 = 0
s2 = 0
n = int(input('enter'))
# for i in range(1,n+1): <- for 1 to n
# for i in range(1,n+1,2): <- for 1 to n with steps
# for i in range(n,0,-1): <- reverse loop
for i in range(n):
    print(i)
    s1 = s1+1

i = 1
while i <= n:
    print(i, end=" ")  # To print in a single line
    s2 = s2+1
    i += 1

print("\nsum of the series is = ", s1, s2)

# Example of break, continue, pass statement in python
n = 0
for n in range(10):
    if n == 5:
        # break
        continue
        # pass
    print("\t Number is = ", n)

else:
    print("\n Out of the Loop \n")
