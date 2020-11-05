"""1. Accept number from user and display below pattern.
Input : 5
Output : A B C D E

class pattern:
    def prog1(self,no):
        j = 1
        for i in range(65,90):
            if j<=no:
                print(chr(i)," ",end="")
                j+=1

obj = pattern()
num=int(input("enter a num"))
obj.prog1(num)

2. Accept number from user and display below pattern.
Input : 5
Output : 5 # 4 # 3 # 2 # 1 #

class pattern:
    def prog2(self,no):
        j = no
        while j>=1:
            print(j," ","#"," ",end="")
            j-=1

obj = pattern()
num=int(input("enter a num"))
obj.prog2(num)

3. Accept number from user and display below pattern.
Input : 5
Output : 1 * 2 * 3 * 4 * 5 *

class pattern:
    def prog3(self,no):
        j = 1
        while j<=no:
            print(j," ","*"," ",end="")
            j+=1

obj = pattern()
num=int(input("enter a num"))
obj.prog3(num)

4. Accept number from user and display below pattern.
Input : 4
Output : # 1 * # 2 * # 3 * # 4 *

class pattern:
    def prog4(self,no):
        j = 1
        while j<=no:
            print("#"," ",j," ","*"," ",end="")
            j+=1

obj = pattern()
num=int(input("enter a num"))
obj.prog4(num)

5. Accept number from user and display below pattern.
Input : 8
Output : 2 4 6 8 10 12 14 16
"""
class pattern:
    def prog5(self,no):
        i=2
        while i<=no*2:
            print(i," ",end="")
            i+=2

obj = pattern()
num=int(input("enter a num"))
obj.prog5(num)
