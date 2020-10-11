"""
1. Accept number of rows and number of columns from user and display
below pattern.
Input : iRow = 4 iCol = 3
Output : * * *
* * *
* * *
* * *

class pattern:
    def prog1(self,row,col):
        for i in range(row):
            for j in range(col):
                print("*",end="")
            print()
obj = pattern()
row=int(input("enter no of rows"))
col=int(input("enter no of columns"))
obj.prog1(row,col)

2. Accept number of rows and number of columns from user and display  below pattern.
Input : iRow = 4 iCol = 3
Output : 1 2 3
 1 2 3
 1 2 3
 1 2 3

class pattern:
    def prog2(self,row,col):
        for i in range(1,row+1):
            for j in range(1,col+1):
                print(j,end="")
            print()
obj = pattern()
row=int(input("enter no of rows"))
col=int(input("enter no of columns"))
obj.prog2(row,col)

3. Accept number of rows and number of columns from user and display  below pattern.
Input : iRow = 3 iCol = 5
Output : 5 4 3 2 1
 5 4 3 2 1
 5 4 3 2 1

class pattern:
    def prog3(self,row,col):
        i=1
        while i<=row:
            j = 5
            while j>=1:
                print(j,end="")
                j-=1
            i += 1
            print()
obj = pattern()
row=int(input("enter no of rows"))
col=int(input("enter no of columns"))
obj.prog3(row,col)

4. Accept number of rows and number of columns from user and display  below pattern.
Input : iRow = 3 iCol = 4
Output : * # * #
 * # * #
 * # * #

class pattern:
    def prog4(self,row,col):
        for i in range(row):
            for j in range(col):
                if (j%2) != 0:
                    print("#",end="")
                else:
                    print("*",end="")
            print()
obj = pattern()
row=int(input("enter no of rows"))
col=int(input("enter no of columns"))
obj.prog4(row,col)

5. Accept number of rows and number of columns from user and display  below pattern.
Input : iRow = 3 iCol = 4
Output : 1 1 1 1
 2 2 2 2
 3 3 3 3
 4 4 4 4
"""
class pattern:
    def prog5(self,row,col):
        for i in range(1,row+1):
            for j in range(1,col+1):
                print(i,end="")
            print()
obj = pattern()
row=int(input("enter no of rows"))
col=int(input("enter no of columns"))
obj.prog5(row,col)
