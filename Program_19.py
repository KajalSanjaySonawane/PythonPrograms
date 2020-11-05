"""
1. Accept number of rows and number of columns from user and display below  pattern.
Input : iRow = 4 iCol = 4
Output :
 * * * #
 * * # *
 * # * *
 # * * *

#with third variable i.e. counter
class Ass19:
    def prog1(self,row,col):
        i=1
        cnt = col
        while i<=row:
            j = 1
            while j<=col:
                if j==cnt:
                    print("# ",end="")
                else:
                    print("* ",end="")
                j+=1
            print()
            i+=1
            cnt -= 1

obj = Ass19()
row=int(input("enter no of rows : "))
col=int(input("enter no of col : "))
obj.prog1(row,col)

#without third variable
class Ass19:
    def prog1(self,row,col):
        i=row
        while i>=1:
            j = 1
            while j<=col:
                if i==j:
                    print("# ",end="")
                else:
                    print("* ",end="")
                j+=1
            print()
            i-=1

obj = Ass19()
row=int(input("enter no of rows : "))
col=int(input("enter no of col : "))
obj.prog1(row,col)

2)
Input : iRow = 4 iCol = 4
Output :
 * * * #
 * * # @
 * # @ @
 # @ @ @

class Ass19:
    def prog2(self,row,col):
        i = row
        while i >= 1:
            j = 1
            while j <= col:
                if i == j:
                    print("# ", end="")
                elif j<=i:
                    print("* ", end="")
                else:
                    print("@ ",end="")
                j += 1
            print()
            i -= 1


obj = Ass19()
row = int(input("enter no of rows : "))
col = int(input("enter no of col : "))
obj.prog2(row, col)

3.
output pattern:
* * * * * *
*       * *
*     *   *
*   *     *
* *       *
* * * * * *

class Ass19:
    def prog3(self,row,col):
        i = row
        while i >=1:
            j = 1
            while j <= col:
                if i == j or i==1 or i== row or j==1 or j==col:
                    print("* ", end="")
                else:
                    print("  ",end="")
                j += 1
            print()
            i -= 1


obj = Ass19()
row = int(input("enter no of rows : "))
col = int(input("enter no of col : "))
obj.prog3(row, col)

4)
Input : iRow = 6 iCol = 6
Output :
 * * * * * *
 * # # # * *
 * # # * $ *
 * # * $ $ *
 * * $ $ $ *
 * * * * * *

class Ass19:
    def prog4(self,row,col):
        i = row
        while i >=1:
            j = 1
            while j <= col:
                if i == j or i==1 or i== row or j==1 or j==col:
                    print("* ", end="")
                elif j<=i:
                    print("@ ",end="")
                else:
                    print("$ ",end="")
                j += 1
            print()
            i -= 1
obj = Ass19()
row = int(input("enter no of rows : "))
col = int(input("enter no of col : "))
obj.prog4(row, col)

5)
Input : iRow = 4 iCol = 4
Output :
 1 2 3 4 5
 1 2     5
 1   3   5
 1     4 5
 1 2 3 4 5
"""
class Ass19:
    def prog5(self,row,col):
        i = 1
        while i <= row:
            j = 1
            while j <= col:
                if i == j or i==1 or i== row or j==1 or j==col:
                    print(j," ",end="")
                else:
                    print(" "," ",end="")
                j += 1
            print()
            i += 1
obj = Ass19()
row = int(input("enter no of rows : "))
col = int(input("enter no of col : "))
obj.prog5(row,col)
