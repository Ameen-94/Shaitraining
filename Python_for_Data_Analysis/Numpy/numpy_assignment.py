import numpy as np

# Part 1: Creating NumPy Arrays
# 1- Using Built-in Methods
arr_1 = np.arange(0, 21, 2)
print(f"An array of numbers from 0 to 20 with a step of 2:\n {arr_1}")
print("\n------------------------------------------------\n")

arr_2 = np.identity(3)
print(f"A 3x3 identity matrix:\n {arr_2}")
print("\n------------------------------------------------\n")

arr_3 = np.ones((4, 4))
print(f"A 4x4 array filled with ones:\n {arr_3}")
print("\n------------------------------------------------\n")

arr_4 = np.linspace(5, 50, 10)
print(f"An array of 10 equally spaced numbers between 5 and 50:\n {arr_4}")
print("\n------------------------------------------------\n")

# 2- Creating Arrays from Lists
lst = [10, 20, 30, 40, 50]
arr_5 = np.array(lst)
print(f"Convert a Python list {lst} into a  NumPy array:\n {arr_5}")
print("\n------------------------------------------------\n")

arr_6 = np.random.rand(3, 3)
arr_7 = np.random.randn(3, 3)
arr_8 = np.random.randint(1, 100, (3, 3))
print(f"Generate a 3x3 matrix of random numbers using rand(), randn(), and randint()")
print(f"Using rand():\n {arr_6}\n")
print(f"Using randn():\n {arr_7}\n")
print(f"Using randint():\n {arr_8}")
print("\n------------------------------------------------\n")

# 3- Array Attributes
print(
    f"The 4x4 array filled with ones shape: {arr_3.shape}, size: {arr_3.size}, and data type: {arr_3.dtype}"
)
print("\n------------------------------------------------\n")

#############################################################################################################

# Part 2:  Indexing and Selection
# 1- Basic Indexing and Selection
arr_1 = np.array([5, 10, 15, 20, 25, 30])
print(arr_1)
print(f"The first element: {arr_1[0]}")

print(f"The last three element: {arr_1[3:]}")

print(f"The elements at index positions 1 to 4: {arr_1[1:5]}")
print("\n------------------------------------------------\n")

# 2- Slicing and Views
arr_2 = np.arange(1, 10).reshape(3, 3)
print(arr_2)
print(f"The second row: {arr_2[1]}")

print(f"The first two columns:\n {arr_2[:, :2]}")

print(f"Sub-matrix of shape(2,2):\n {arr_2[:2, :2]}")
print("\n------------------------------------------------\n")

# 3- Broadcasting
arr_3 = arr_2.copy()
print(arr_3)
arr_3 = arr_3 + 10
print(f"After adding 10 to every element:\n {arr_3}")

arr_3[:, :2] = arr_3[:, :2] * 2
print(f"After multiplying the first two columns by 2:\n {arr_3}")
print("\n------------------------------------------------\n")

# 4- Copying Array
# Shallow Copy
arr_4 = np.array([1, 2, 3, 4, 5])
arr_5 = arr_4
print(f"Original array: {arr_4}")
print(f"Shallow copied array: {arr_5}")
arr_5 += 5
print(f"Shallow copied array after modification: {arr_5}")
print(f"Original array after modification: {arr_4}")
print("\n------------------------------------------------\n")
# Deep Copy
arr_6 = np.array([1, 2, 3, 4, 5])
arr_7 = arr_6.copy()
print(f"Original array: {arr_6}")
print(f"Deep copied array: {arr_7}")
arr_7 += 5
print(f"Deep copied array after modification: {arr_7}")
print(f"Original array after modification: {arr_6}")
print("\n------------------------------------------------\n")

# 5- Fancy Indexing
arr_8 = np.arange(10, 101, 10)
print(arr_8)
print(f"Elements 0, 3, and 5 of the array:{arr_8[[0, 3, 5]]}")
print("\n------------------------------------------------\n")

#############################################################################################################

# Part 3: NumPy Operations
# 1- Mathematical Functions
arr_1 = np.array([3, 7, 2, 9, 12, 5, 10])
print(arr_1)
print(f"Maximum value: {np.max(arr_1)} ")
print(f"Minimum value: {np.min(arr_1)} ")
print(f"Maximum value index: {np.argmax(arr_1)} ")
print(f"Minimum value index: {np.argmin(arr_1)} ")
print("\n------------------------------------------------\n")

# 2- Universal Array Functions
arr_2 = np.array([1, 2, 3, 4, 5])
print(arr_2)
print(f"Square root of each element: {np.sqrt(arr_2)}")
print(f"Exponential of each element: {np.exp(arr_2)}")
print(f"Sine of each element: {np.sin(arr_2)}")
print(f"Logarithm of each element: {np.log(arr_2)}")