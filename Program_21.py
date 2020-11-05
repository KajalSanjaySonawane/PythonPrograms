"""
1. Accept N numbers from user and return difference between summation
of even elements and summation of odd elements.
Input : N : 6
Elements : 85 66 3 80 93 88
Output : 53 (234 - 181)

class Ass21:
    def prog1(self,arr):
        countEven = 0
        countOdd = 0
        for j in range(len(arr)):
            if arr[j] % 2 == 0:
                countEven = countEven + arr[j]
            else:
                countOdd = countOdd + arr[j]
        return countEven - countOdd


obj = Ass21()
N = int(input("how many elements you want"))
arr = []
print("enter the elements")
for i in range(N):
    ele = int(input())
    arr.append(ele)
print("entered elements are :",arr)
difference = obj.prog1(arr)
print("difference between summation of odd and even elements are : ",difference)

2. Accept N numbers from user and display all such elements which are
divisible by 5.
Input : N : 6
 Elements : 85 66 3 80 93 88
Output : 85 80

class Ass21:
    def prog2(self,arr):

        for j in range(len(arr)):
            if arr[j] % 5 == 0:
                print("the elements which are divisible by 5 are : ",arr[j])

obj = Ass21()
N = int(input("how many elements you want"))
arr = []
print("enter the elements")
for i in range(N):
    ele = int(input())
    arr.append(ele)
print("entered elements are :",arr)
obj.prog2(arr)

3. Accept N numbers from user and display all such elements which are
even and divisible by 5.
Input : N : 6
 Elements : 85 66 3 80 93 88
Output : 80

class Ass21:
    def prog3(self,arr):

        for j in range(len(arr)):
            if arr[j] % 5 == 0 and arr[j] % 2 == 0:
                print("the elements which are divisible by 5 and even are : ",arr[j])

obj = Ass21()
N = int(input("how many elements you want"))
arr = []
print("enter the elements")
for i in range(N):
    ele = int(input())
    arr.append(ele)
print("entered elements are :",arr)
obj.prog3(arr)

4. Accept N numbers from user and display all such elements which are
divisible by 3 and 5.
Input : N : 6
 Elements : 85 66 3 15 93 88
Output : 15

class Ass21:
    def prog4(self,arr):

        for j in range(len(arr)):
            if arr[j] % 5 == 0 and arr[j] % 3 == 0:
                print("the elements which are divisible by 5 and 3 are : ",arr[j])

obj = Ass21()
N = int(input("how many elements you want"))
arr = []
print("enter the elements")
for i in range(N):
    ele = int(input())
    arr.append(ele)
print("entered elements are :",arr)
obj.prog4(arr)

5. Accept N numbers from user and display all such elements which are
multiples of 11.
Input : N : 6
 Elements : 85 66 3 55 93 88
Output : 66 55 88
"""
class Ass21:
    def prog5(self,arr):

        for j in range(len(arr)):
            if arr[j] % 11 == 0:
                print("the elements which are multiplies of 11 are: ",arr[j])

obj = Ass21()
N = int(input("how many elements you want"))
arr = []
print("enter the elements")
for i in range(N):
    ele = int(input())
    arr.append(ele)
print("entered elements are :",arr)
obj.prog5(arr)
