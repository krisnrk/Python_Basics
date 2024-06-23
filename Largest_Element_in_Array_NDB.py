x=[30,1,41,75,99,14,53,62] #only workes where there are unique elements in array
for i in range(len(x)):
    count=0
    for j in range(0,len(x)):
          if x[i]>x[j]:
               count=count+1
          y=count
    if y==len(x)-1:
      print("The Greatest number in the Array is",x[i])
      break    
    

  