#we can't perform array opeartions using normal array so we have to use NUMPY for doing operations
from numpy import *
"""
1)
arr= array([1,2,5,6,8,9])
arr = arr + 1
print(arr)

2)
a1 = array([1,2,5,6,8,9],int)  # Syntax of array used in Numpy here type defined at  last type is optional
    #arr = array('i',[1,2,5,6,8,9])   #Syntax of array used in normal array specifies type of array at start i.e.'i,'I,'u',etc
a2 = array([5,8,6,4,2,3])
ans = a1 + a2     # we can directly perform operations in numpy while in normal array we can't perform
print(ans)
#If we don't give type of aaray it automatically consider it's type so it is optional

3)
first = array([5,10,15,20,25,30])
ans = first * first
print(ans)

4)

first = array([5,10,15,20,25,30])
ans = first * first
print("Square of each elee in array are: ",ans)
print("Max no in array is : ",max(first))
print("Min no in array is : ",min(first))
print("cos values are: ",cos(first))
print("sin values are: ",sin(first))
print("Length of array is : ",len(first))
print("Square root of array ele is : ",sqrt(first))
print("Sqaure of each array ele is : ",square(first))

5)
arr1 = array([1,4,5,6,8,9,10])

arr2 = arr1    # we can directly copy frst array into second but they refer one mem location

print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))

6)
arr1 = array([1,4,5,6,8,9,10])

arr2 = arr1.view()    # by using view we got two different addresses  This is SHALLOW COPY

arr1[2]=0  # in future if we done any change in first array then
            #it'll reflect on second as well so this is shallow copy avoid this we can use deeep copy

print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))

7)
arr1 = array([1,4,5,6,8,9,10])
print("Before change ele : ",arr1)
arr2 = arr1.copy()    # by using copy fun we got two different addresses with different values This is DEEP COPY

arr1[2]=0  # in future if we done any change in first array then
            #it'll not reflect on second so this is deep copy  best practise to copied array element in second

print("after change ele : ",arr1)
print(arr2)
print(id(arr1))
print(id(arr2))

8)
# Add two array using for loop not using in-built functions
arr1 = array([4,5,6,2,3,9])
print(arr1)
arr2 = array([1,5,6,2,7,4])
print(arr2)

for i in range(len(arr1)):
    arr3 = arr1[i] + arr2[i]
    print(arr3, " ", end="")

o/p:
[4 5 6 2 3 9]
[1 5 6 2 7 4]
5  10  12  4  10  13 

9)"""
# find min and max without using in-built functions
arr=array([45,56,2,0,36987,5])
max,min=arr[0],arr[0]
for i in arr:
    if max<i:
        max=i
    elif min>i:
        min=i
print(max,min)