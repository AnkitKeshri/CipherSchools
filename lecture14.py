#Functions is a block of reusable code

def square(a):  #defining a function
  print(a**2)

a=int(input("Enter the value of a= ")) 
square(a) #calling a function 
#without calling nothing is printed


def square(a):  #defining a function
  return a**2

a=int(input("Enter the value of a= ")) 
c = square(a) #calling a function 
print("c = " ,c)


def add_numbers(a,b):
""" Function to add two numbers"""
return a + b
#Calling the function
print(add_number(3,4))


#Function with Default Arguments
def greet(name, message="Hello"):
  """Function to greet a person with a default message"""
  return f"{message}, {name}!"
#Calling the function
print(greet("Bob"))
print(greet("Alice","Hi"))


#Function with variable-Length Arguments
def sum_all(*args):
"""Function to sum all given arguments"""
return sum(args)

#Calling the function
print(sum_all(1,2,3,4,5))


#Function with Keyword Arguments
def display_info(**kwargs):
  """Function to display information using keyword arguments"""
  for key, value in kwarsg.items():
      print(f"{key}: {value}")

#calling the function
display_info(name="John", age=30, city="New York")


#Highest-Order function
def apply_function(func,x,y):
  """Function to apply another function to give aarguments"""
    return func(x,y)

def multiply(a,b):
  return a * b
