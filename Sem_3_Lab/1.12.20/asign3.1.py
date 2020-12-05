# To find the sum of the series 1 + 2 + 3 + ...

n=int(input('Enter the no of terms of the series: '))

def ser(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
        print(i,end=" + ")
    print("\nThe sum is:",sum)

print("The given series is: ")
ser(n)