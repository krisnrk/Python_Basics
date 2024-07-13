#Python function to calculate the factorial of a number
     #Function START
def factorial(num): #defining a function with 1 parameter num (num takes the input given by user)
  if y<0:# if condition to check input is non negative interger or not. It returns below error if input in negative
      return 'Error:enter a non-negative integer'
  else:
   x=1 # declaring variable x with value 1, As we are using x in loop to store the product of numbers
   for i in range(1,num+1): # defining loop with the range between 1 and input given by user + 1
      x=x*i # multiplying i(increment number of the loop) with the value of x and storing it in x
   return x # Returning x value after loop ends
   # Function END
y=int(input("Enter a Number:")) # Taking input from user and storing it in y variable 
print(f' Factorial of {y} is {factorial(y)}') # invoking function and taking in y variable as input argument and at the end the function return x and it is printed