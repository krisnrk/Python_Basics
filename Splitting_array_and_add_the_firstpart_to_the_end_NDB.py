x=[9,5,3,7,8,4]
y=int(len(x)/2)
print(x[y])
z=0
for i in range(y,len(x)):
    #print(i)
    if (z<=y):
     temp=x[z]
     x[z]=x[i]
     x[i]=temp
    z=z+1
print(x)
        