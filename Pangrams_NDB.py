#Python function to check whether a string is a pangram or not.
#list 1 contains all the 26 alphabets that are useful for comparision with user input
list1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
index=0 #index is used in remove space code for pop method
#declaring a function with user input which is converted to list
   #START OF FUNCTION
def pangram_logic(input_list):
  index=0
#below code is used to remove space in the sentence enterd by user
  for i in input_list:
   if i==' ':
    input_list.pop(index)
   index+=1
#below code is used to make the elements of the list to lower case
  list3=[l.lower() for l in input_list]
#converting the lists into set so that it will be easy to compare and it doesn't store duplicate values
  a = set(list1)  
  b = set(list3)
  str=" "
  if(a==b):
    return("It is a pangram")
  else:
    return("It is not a pangram")
    #END OF FUNCTION

list2=list(input("Enter the sentence:"))#taking input from user and converting to list.
#converting the user input to list so that it can be compared with list1 containg alphabets
x=pangram_logic(list2)#function call with list2 as argument and storing it in x for printing output
print(x)
