#Functions is a block of reusable code

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


