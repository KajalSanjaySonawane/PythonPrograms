import Constant
"""1.Write a program which accept number from user and display below pattern.
Input : 5
Output : * * * * * # # # # #
Input : 6
Output : * * * * * * # # # # # # #
Input : -5
Output : * * * * * # # # # #
Input : 2
Output : * * # #

class Pattern:
    def prog1(self,no):
        for i in range(no):
            print(Constant.first,end=" ")
        for i in range(no):
            print(Constant.second,end=" ")

pobj= Pattern()
no=int(input("enter a num"))
pobj.prog1(no)

2. Accept amount in US dollar and return its corresponding value in Indian currency.  Consider 1$ as 70 rupees.  
Input : 10  
Output : 700

class Pattern:
    def prog2(self,no):
        print("converted value from dollar to rupee is :",Constant.Dollarvalue * no) #store it in another file so if next time dollar value is getting changed that value will be inserted in every function

pobj= Pattern()
no=int(input("enter a num"))
pobj.prog2(no)

3.Write a program to find even factorial of given number.  
Input : 5  
Output : 8 (4 * 2)  
Input : -5  
Output : 8 (4 * 2)  

class Pattern:
    def prog3(self,no):
        mul=1
        i=no
        while i>=1:
            if i%2 ==0:
                mul = mul * i
                print("even fact are:",i)
            i-=1
        print("fact of even no are:",mul)

pobj= Pattern()
no=int(input("enter a num for factorial"))
pobj.prog3(no)

4. Write a program to find odd factorial of given number.  
Input : 5  
Output : 15 (5 * 3 * 1)  
Input : -5  
Output : 15 (5 * 3 * 1)  
Input : 10  
Output : 945 (9 * 7 * 5 * 3 * 1)

class Pattern:
    def prog4(self,no):
        mul=1
        i=no
        while i>=1:
            if i%2 !=0:
                mul = mul * i
                print("odd fact are:",i)
            i-=1
        print("fact of odd no are:",mul)

pobj= Pattern()
no=int(input("enter a num for factorial"))
pobj.prog4(no)

5. Write a program which returns difference between Even factorial and odd factorial  of given number.  
Input : 5  
Output : -7 (8 - 15)  
Input : -5  
Output : -7 (8 - 15)  
Input : 10  
Output : 2895 (3840 - 945)  
"""
class Pattern:
    def prog5(self,no):
        mul1,mul2=1,1
        i=no
        while i>=1:
            if i%2 ==0:
                mul1 = mul1 * i
                print("even fact are:",i)
            elif i%2 != 0:
                mul2 = mul2 * i
                print("odd fact are:",i)
            i-=1
        print("Difference between even and odd factorial is:",mul1-mul2)

pobj= Pattern()
no=int(input("enter a num for factorial"))
pobj.prog5(no)
