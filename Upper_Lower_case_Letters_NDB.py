#Python function that accepts a string and counts the number of upper and lower case letters
     #function start
def split_string(words):#split_string function splits the string into elements of the list with user input as parameter
    count2=count=0# count and count2 variables are initialised to zero as they will be used to count the upper(count) and lower(count2) case letter
    for i in list(words):#running the loop for the list element
        if i.isupper() is True:#using string method: isupper() to find if the letter is upper case or not
          count=count+1 # if the letter is upper case the count is incresed and stored in count variable
        else:# if th letter is lower case the else condition is satisfied
          count2=count2+1 # count of lower cases is stored in count2
    return count,count2 # returning count of upper and lower case letters
  #Function END  
words = str(input("Enter the String:")) # input: user enters the word

x,y=split_string(words)#fuction return 2 values(count of upper case and lower case letters) these are stored in x and y varaibles
print(f"upper case letters in {words} :{x}")#upper case count is displyed using print statement
print(f"lower case letters in {words} :{y}")#Lower case count is displyed using print statement

       