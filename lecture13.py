#Assigning values to variable
name = "John Doe"
age = 30
height = 5.9


#Data Types
#integer
num = 10

#inbuilt functions and operations for integer
print(abs(num)) #Absolute value

print(bin(num)) #Binary Representation

print(hex(num)) #Hexadecimal Representation

print(pow(num,2)) #power function (num^2)

print(divmod(num,3)) #Quotient and remainder

#float
price = 99.99

#Inbuilt function and operation for float
print(round(price)) #Rounding

print(abs(price)) #Absolute value

print(int(price)) #Convert to integer

print(float("123.45")) #Convert string to float

print(price.is_integer()) #Check if the float is an integer


#String
greeting = "Hello, World!"

#Inbuilt functions and operations for strings
print(greeting.lower()) #Convert to lowercase

print(greeting.upper()) #Convert to uppercase

print(greeting.replace("World","Python")) #Replace substring

print(greeting.split()) #Split string into a list

print(greeting.find("World")) #Find Substring

print(len(greeting)) #LEngth of the String

#List
fruits = ["apple","banana","cherry"]

#Inbuilt functions and operations for list
fruits.append("Orange") #Append an element (add an element in the list)

fruits.extend(["grape","melon"]) #Extend list with another lsit

fruits.remove("banana") #Remove an element

fruits.pop() #Remove the last element

fruits.sort() #Sort the list

print(fruits)

print(len(fruits)) #Length of the list

print(fruits.index("cherry")) #Find index of element

print("apple" in fruits) #Check if element is in list


#Tuple
Coordinateed = (10.0,20.0)

#Inbuilt functions and operations for tuple
print(coordinates.count(10.0)) #Count occurences of a value

print(coordinates.index(20.0)) #Find index of element

print(len(coordinates)) #Length of the tuple

#if we want to change the element in tuple we have to convert the tuple to list and then change and after changing the element in list we have to change again into tuple
#Dictionary
person = {"name": "John", "age": 30} # {Key : value}

#Inbuilt functions and operations for Dictionary
print(person.keys()) #Get all keys

print(person.values()) #Get all values

print(person.items()) #Get all key-value pairs

print(person.get("name")) or person["name"] #Get value by key

person.update({"height": 180}) #Update dictionary with another dictionary

person.pop("age") #Remove key-value pair by key

print(person)

print(len(person)) #Length of the dictionary


#SET
se={1,2,3,4}

#not allow duplicates
se={1,1,1,1,1} #will only print a single value
result -> {1}


#lenght
print(len(se))

#add
se.add(9)

se.update({10,11,12}) #add another set

#remove
se.remove(10)

#Boolean
is_active = True

#Inbuilt functions and operations for Boolean
print(int(is_active)) #Convert to integer1 for True, 0 for False

print(bool(0)) #Convert integer to boolean (False)

print(bool(1)) #Convert integer to boolean (True)

print(bool("Hello")) #convert string to boolean (True)

print(is_active and False) #Logical AND

print(is_active or False) #Logical OR

print(not is_active) #Logical NOT


#Conditional Statement in Python

#Basic if-elif-else Statement
age = 20

if age<18:
  print("Minor")
elif age >= 18 and age <65:
  print("Adult")
else:
  print("Senior")


#Checking Even or Odd Number
number = 42

if number % 2 == 0:
  print("Even Number")
else:
  print("Odd number")

#Grade Evaluation
score = 85

if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >=70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D")
else:
  print("Grade: F")


#Temperature Check
temp = 30

if temp > 30:
  print("It's a hot day")
elif temp >= 20:
  print("It's a nice day")
else:
  print("It's a cold day")


#Nested Conditionals and BMI Calculation
weight = 70 #in kg
height = 1.75 #in meters

bmi = weight / (height ** 2)

if bmi < 18.5:
  print("Underweight")
else:
  if bmi < 24.9:
    print("Normal weight")
  else:
    if bmi < 29.9:
      print("Overweight")
    else:
      print("Obesity")
#result -> Normal Weight



























