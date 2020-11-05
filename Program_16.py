"""1. Accept number of rows and number of columns from user and display  below pattern.
Input : iRow = 4 iCol = 4
Output :
 1 2 3 4
 5 6 7 8
 9 1 2 3
 4 5 6 7

class ass16:
    def prog1(self,row,col):
        count=1
        for i in range(row):
                for j in range(col):
                    print(count," ",end="")
                    count+=1
                    if count > 9:
                        count=1
                print()
obj=ass16()
row=int(input("emter no of rows"))
col=int(input("enter no of col"))
obj.prog1(row,col)

2. Accept number of rows and number of columns from user and display  below pattern.
Input : iRow = 4 iCol = 4
Output :
 2 4 6 8 10
 1 3 5 7 9
 2 4 6 8 10
 1 3 5 7 9

class ass16:
    def prog2(self,row,col):
        for i in range(row):
            count1 = 2
            count2 = 1
            for j in range(col):
                if i%2==0:
                    print(count1," ",end="")
                    count1+=2
                else:
                    print(count2," ",end="")
                    count2+=2
            print()
obj=ass16()
row=int(input("emter no of rows"))
col=int(input("enter no of col"))
obj.prog2(row,col)

3. Accept number of rows and number of columns from user and display  below pattern.
Input : iRow = 5 iCol = 5
Output :
 a b c d e
 1 2 3 4 5
 a b c d e
 1 2 3 4 5
 a b c d e

class ass16:
    def prog3(self,row,col):
        for i in range(row):
            count1 = 97
            count2 = 1
            for j in range(col):
                if i%2==0:
                    print(chr(count1)," ",end="")
                    count1+=1
                else:
                    print(count2," ",end="")
                    count2+=1
            print()
obj=ass16()
row=int(input("emter no of rows"))
col=int(input("enter no of col"))
obj.prog3(row,col)

4. Accept number of rows and number of columns from user and display  below pattern.
Input : iRow = 5 iCol = 5
Output :
 1 2 3 4 5
 -1 -2 -3 -4 -5
 1 2 3 4 5
 -1 -2 -3 -4 -5
 1 2 3 4 5

class ass16:
    def prog4(self,row,col):
        for i in range(row):
            count1 = 1
            count2 = -1
            for j in range(col):
                if i%2==0:
                    print(count1," ",end="")
                    count1+=1
                else:
                    print(count2," ",end="")
                    count2-=1
            print()
obj=ass16()
row=int(input("emter no of rows"))
col=int(input("enter no of col"))
obj.prog4(row,col)

5. Accept number of rows and number of columns from user and display  below pattern.
Input : iRow = 4 iCol = 4
Output :
 1 2 3 4
 2 3 4 5
 3 4 5 6
 4 5 6 7
"""
class ass16:
    def prog5(self,row,col):
        count1 = 1
        for i in range(1,row+1):
            for j in range(col):
                print(count1," ",end="")
                count1+=1
            print()
            count1 = 1
            count1 = count1+i
obj=ass16()
row=int(input("emter no of rows"))
col=int(input("enter no of col"))
obj.prog5(row,col)
