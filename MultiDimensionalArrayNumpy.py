from numpy import *
"""
1)
arr = array([
    [1,2,5],
    [5,6,2]

])
print(arr)

print("Type of Array is : ",arr.dtype)
print("This array is :",arr.ndim,"dimensional")
print("No of rows and column in array are : ",arr.shape)
print("Size of Array is : ",arr.size)

2)
arr = array([
    [1,4,6],
    [2,4,8]
])

arr2 = arr.flatten()
print(arr2)

arr3 = arr2.reshape(3,2)
print(arr3)

3)
m1 = matrix('1 2 ; 3 4')
print(m1)

m2= matrix('4 5 6 4 ; 5 6 2 1 ; 4 2 3 0')
print(m2)

print(diagonal(m2))
print(m2.dtype)
print(m2.min())
print(m2.max())
print(m2.sum())

4)"""

m1 = matrix('5 6 2 ; 4 5 6 ; 1 2 3')
print(m1)

m2 = matrix('1 2 6 ; 2 3 1 ; 1 3 2')

m3 = m1 + m2
print("Addition of two array is : ",m3)

m3 = m1 * m2
print("Multiplication of two array is : ",m3)
