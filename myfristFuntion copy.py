'''def step1():
    print("This is my first Function")
# we need to call the function in inorder to see the output
step1()
'''
'''def step2(a,b):
    return a+b
step2(3,5) # it executes but does not see the output
add_numbers=step2(3,5)
print(add_numbers)
'''
'''def step3(i,j):
    return i*j
mnumbers = step3(int(input("Enter first number:\n")),int(input("Enter Second Number:\n")))
print(mnumbers)
'''
def hello_func(greetings):
    return "{} World".format(greetings)
print(hello_func("hi"))

def hello_func(greetings,name='You'):
    return "{} {}".format(greetings,name)
print(hello_func("hi"))
print(hello_func("hi","Nimu"))
