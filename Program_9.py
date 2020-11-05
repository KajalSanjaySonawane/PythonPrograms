"""1.Write a program which accept number from user and print that number of $ & *  on screen.
Input : 5
Output : $ * $ * $ * $ * $ *
Input : 3
Output : $ * $ * $ *
Input : -3
Output : $ * $ * $ *

def check(no):
    for i in range(no):
        print("$*"," ",end="")

num=int(input("enter a num"))
check(num)

2.Write a program which accept number from user and print numbers till that  number.
Input : 8
Output : 1 2 3 4 5 6 7 8

def check(no):
    for i in range(1,no+1):
        print(i," ",end="")

num=int(input("enter a num"))
check(num)

3. Write a program which accept number from user and print its numbers line.  Input : 4
Output : -4 -3 -2 -1 0 1 2 3 4

def check(no):
    for i in range(-no,no+1):
        print(i," ",end="")

num=int(input("enter a num"))
check(num)

4. Write a program which accepts N from user and print all odd numbers up to N.
Input : 18
Output : 1 3 5 7 9 11 13

def check(no):
    for i in range(1,no+1):
        if i % 2  != 0:
            print(i," ",end="")

num=int(input("enter a num"))
check(num)

5. Write a program which accept N and print first 5 multiples of N.
Input : 4
Output : 4 8 12 16 20
"""
def check(no):
    for i in range(no,(no*5)+1,no):
        print(i)

num=int(input("enter a num"))
check(num)
