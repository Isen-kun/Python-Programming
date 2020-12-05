#to check whether a number is a perfect number or not
print("INPUT :")
n=int(input('Enter the number to be checked for : '))
sum=0
count=0
factors=list()
print("\nOUTPUT:\n")
if n<=0:
 print("INCORRECT DATA !!!")
else:
 for i in range(2,int(n/2)+1):
 if n%i==0: #check for factors
 sum=sum+i #sum of factors
 count=count+1 #counting number of factors
 factors.append(i) #storing the factors
 sum=sum+1 #1 is a common factor for all
 print('The factors are :\n1')
 for item in factors:
 print(item)
 print("The number of factors are",count+1)
 if sum==n:
 print(n,"is a perfect number")
 else:
 print(n,"is not a perfect number") 