#Python function that takes a list and returns a new list with distinct elements from the first list
#START OF FUNCTION
def distinct_elements(input_list):#function takes the input(list1) from user
 index=0#index variable is given zero so that 
 list2=[]#declaring an empty set to store the distinct values
 for i in input_list:#running loop for user input elements 
    if i not in list2: #checking if the user input elements are present in list or not
        list2.insert(index,i)#using insert function to insert unique elements in list2 with indx and user elements
        index+=1 #after inserting the index is incremented by 1 
 return list2 #after inseting distinct elements it is returned
#END OF FUNCTION 
list1=list(input("Enter the elements of the list:"))#taking input from user in the form of list

print(f"Unique List: {distinct_elements(list1)}")