"""
1. Accept number of rows and number of columns from user and display below  pattern.
Input : iRow = 4 iCol = 4
Output : A B C D
 A B C D
 A B C D
 A B C D

class ass15:
    def prog1(self,row,col):
        for i in range(row):
            k=1
            for j in range(65,90):
                if k<=col:
                    print(chr(j)," ",end="")
                    k+=1
            print()

obj = ass15()
row=int(input("enter no of rows"))
col=int(input("enter no of columns"))
obj.prog1(row,col)

2. Accept number of rows and number of columns from user and display below  pattern.
Input : iRow = 4 iCol = 4
Output : A B C D
 a b c d
 A B C D
 a b c d

class ass15:
    def prog2(self,row,col):
        for i in range(row):
            k=1
            if i%2 ==0:
                for j in range(65,90):
                    if k<=col:
                        print(chr(j)," ",end="")
                        k+=1
            else:
                k=1
                for j in range(97,122):
                    if k<=col:
                        print(chr(j)," ",end="")
                        k+=1
            print()

obj = ass15()
row=int(input("enter no of rows"))
col=int(input("enter no of columns"))
obj.prog2(row,col)

3. Accept number of rows and number of columns from user and display below  pattern.
Input : iRow = 3 iCol = 5
Output : A A A A A
 B B B B B
 C C C C C

class ass15:
    def prog3(self,row,col):
        k = 1
        for i in range(65,90):
            for j in range(col):
                if k<=row:
                    print(chr(i)," ",end="")
            k+=1
            print()

obj = ass15()
row=int(input("enter no of rows"))
col=int(input("enter no of columns"))
obj.prog3(row,col)

4. Accept number of rows and number of columns from user and display below  pattern.
Input : iRow = 4 iCol = 5
Output : 4 4 4 4 4
 3 3 3 3 3
 2 2 2 2 2
 1 1 1 1 1

class ass15:
    def prog4(self,row,col):
        for i in range(row):
            for j in range(col):
                    print(row-i,end="")
            print()

obj= ass15()
row=int(input("enter no of rows : "))
col=int(input("enter no of columns : "))
obj.prog4(row,col)
00
5. Accept number of rows and number of columns from user and display below  pattern.
Input : iRow = 3 iCol = 4
Output : 1 2 3 4
 5 6 7 8
 9 10 11 12
"""
class ass15:
    def prog4(self,row,col):
        counter=1
        for i in range(row):
            for j in range(col):
                if i<=row:
                    print(counter," ",end="")
                    counter+=1
            print()
obj= ass15()
row=int(input("enter no of rows : "))
col=int(input("enter no of columns : "))
obj.prog4(row,col)

