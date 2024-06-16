#Data Manipulation and Analysis with NumPy
#NumPY is a fundamentak package for scientific computing with Python. It provides support for arrays, matrices,and a large collection of mathematical function to operate on these data structure. NumPy arrays are more efficient and provide better performance for numerical operations compared to pyhton's built -in lists.

#First install the library -------->>>>>>  #pip install library name
#then import the library where we have to use that library -------->>>>>> import library name

#create a NumPy Array from a list
import numpy as np
#Creating a 1d array from a list
arr1 = np.array([1,2,3,4,5])
print(arr1)

#create a 2D array from a list of lists
arr2 = np.array([[1,2,3],[4,5,6]])
print(arr2)



#Creating Arrays with Functions
#create an array as zeros
zeros = np.zeros((3,4))
print(zeros)


#create an array of ones
ones = np.ones((3,4))
print(ones)


#Creating an array with a range of values
range_Arr = np.arange(start=10, stop=20, step=2) or range_Arr = np.arange(10,20,2)
print(range_Arr)


#Creating an array with random values
random_arr = np.random.rand(3,3)
print(random_arr)
