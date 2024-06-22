n1=int(input("Enter the 1st number:"))
n2=int(input("Enter the 2nd number:"))

for i in range(n1,n2+1):
    x=0
    for j in range(1,i+1):
        if i%j==0:
             x=x+1
    if(x==2):
     print(i)
   