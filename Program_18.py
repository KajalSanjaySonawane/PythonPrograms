"""
1. Accept number of rows and number of columns from user and display below  pattern.
Input : iRow = 4 iCol = 4
Output :
 *
 * *
 * * *
 * * * *

class Ass18:
    def prog1(self,row,col):
        for i in range(1,row+1):
            for j in range(1,col+1):
                if j<=i:
                    print("*",end="")
            print()
obj=Ass18()
row=int(input("enter no of rows"))
col=int(input("enter no of columns"))
obj.prog1(row,col)

2. Accept number of rows and number of columns from user and display below  pattern.
Input : iRow = 4 iCol = 4
Output :
 * * * *
 * * *
 * *
 *

class Ass18:
    def prog2(self,row,col):
        i=row
        while i>=1:
            j=1
            while j<=col:
                if j<=i:
                    print("*",end="")
                j+=1
            print()
            i -= 1

obj=Ass18()
row=int(input("enter no of rows"))
col=int(input("enter no of columns"))
obj.prog2(row,col)

3. Accept number of rows and number of columns from user and display below  pattern.
Input : iRow = 5 iCol = 5
Output :
 $ * * * *
 # $ * * *
 # # $ * *
 # # # $ *
 # # # # $

class Ass18:
    def prog3(self,row,col):
        i=1
        while i<=row:
            j=1
            while j<=col:
                if j==i:
                    print("$",end="")
                elif i<=j:
                    print("*", end="")
                else:
                    print("#", end="")
                j+=1
            print()
            i += 1

obj=Ass18()
row=int(input("enter no of rows"))
col=int(input("enter no of columns"))
obj.prog3(row,col)

4. Accept number of rows and number of columns from user and display below  pattern.
Input : iRow = 6 iCol = 6
Output :
 * * * * * *
 * * *
 * * *
 * * *
 * * *
 * * * * * *

class Ass18:
    def prog4(self,row,col):
        i=1
        while i<=row:
            j=1
            while j<=col:
                if  i==1 or i==row or j > (col/2):
                    print("*",end="")
                j+=1
            print()
            i += 1

obj=Ass18()
row=int(input("enter no of rows"))
col=int(input("enter no of columns"))
obj.prog4(row,col)

one more pattern
 * * * * * *
 * *       *
 *   *     *
 *     *   *
 *       * *
 * * * * * *

class Ass18:
    def prog4(self,row,col):
        i=1
        while i<=row:
            j=1
            while j<=col:
                if i==1 or i==row or j==1 or j==col or i==j:
                    print("*"," ",end="")
                else:
                    print(" "," ", end="")
                j+=1
            print()
            i += 1
obj=Ass18()
row=int(input("enter no of rows"))
col=int(input("enter no of columns"))
obj.prog4(row,col)

5. Accept number of rows and number of columns from user and display below  pattern.
Input : iRow = 4 iCol = 4
Output :
 1 2 3 4
   2 3 4
     3 4
       4
"""

class Ass18:
    def prog5(self,row,col):
        i=1
        cnt=i
        while i<=row:
            j = cnt
            while j<=col:
                if i<=j:
                    print(j,end="")
                    j+=1
                else:
                    print(" ",end="")
            print()
            i+=1
            cnt+=1
obj=Ass18()
row=int(input("enter no of rows"))
col=int(input("enter no of columns"))
obj.prog5(row,col)
