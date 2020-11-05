import numpy as np

arr = np.array([1,2,5,6,3,7,8])
print(arr)
print(arr.dtype)
print(type(arr))
print(arr[0])
print(arr[-1])
print(arr[:5])    #slicing
print(arr[2:])
print(arr[1:6:2])
print(arr[-4:-1])
print(arr[::2])

newarr = np.array([1,2,5],dtype='i')   #to define type of array
print(newarr)

newarrr1 = newarr.astype('f')  #astype() change the array type
print(newarrr1)

newarrr2 = newarr.copy()    #copy the array anything change in original array not reflected in copied array
print(newarrr2)
newarr[0] = 50
print(newarr)
newarrr3 = newarr.view()  #view means just the view of original array anything change in original reflects on view as well

newarr[1] = 60
print(newarrr3)
newarrr3[2] = 100
print(newarr)

arr = np.array([1,2,3,4,5], ndmin=4)
print(arr)

print(arr.shape)    #array shape
arr1 = np.array([[1,2,3,7],[5,6,5,8]])

print(arr1.shape)   # (2,4) means 2-D array with 4 elements
arr2 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(arr2.reshape(2,6))
print(arr2.reshape(4,3))    #reshape 1-D array to 2-D array but make sure that while reshaping
                                # we have that many elements e.g we have 8 elements we can't make it as 3x3=9

print(arr2.reshape(2,3,2))   #reshape 1-D array to 3-D array

print(arr2.reshape(6,2).base)    #The example returns the original array, so it is a view means original array we get

print(np.flip(arr1))

