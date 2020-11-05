"""1. Write a program which accept number from user and if number is less than 50  then print small , if it is greater than 50 and less than 100 then print medium, if it is  greater than 100 then print large.
Input : 75  
Output : Medium  


def check(no):
    if no<50:
        print("no is small")
    elif no> 50 and no <100:
        print("no is medium")
    else:
        print("no is greater")

num=int(input("enter a num"))
check(num)

2. Accept single digit number from user and print it into word.
Input : 9
Output : Nine
Input : -3
Output : Three
Input : 12
Output : Invalid Number

def check(no):
    list1 = ["one","two","three","four","five","six","seven","eight","nine","ten"]
    for i in range(len(list1)):
        if i == no:
            print(list1[i-1])

num=int(input("enter a num"))
check(num)

3.Write a program to find factorial of given number.
Input : 5
Output : 120 (5 * 4 * 3 * 2 * 1)
Input : -5
Output : 120 (5 * 4 * 3 * 2 * 1)
Input : 4
Output : 24 (4 * 3 * 2 * 1)

def fact(no):
    count = 1
    for i in range(1,no+1):
        count = i * count
    print(count)

num = int(input("enter a number for factorial"))
fact(num)

4.Write a program which accept number from user and display its table.  Input : 2
Output : 2 4 6 8 10 12 14 16 18 20
Input : 5
Output : 5 10 15 20 25 30 35 40 45 50
Input : -5
Output : 5 10 15 20 25 30 35 40 45 50

def table(no):
    for i in range(no,(no*10)+1,no):
        print(i)

num = int(input("enter a no"))
table(num)

5. Write a program which accept number from user and display its table in reverse  order.
Input : 2
Output : 20 18 16 14 12 10 8 6 4 2

def table(no):
    count = no*10
    while no <= count:
        print(count)
        count -=no;

num = int(input("enter a no"))
table(num)

def check(no):
    count = 0
    if no == 0:
        print("plz enter non-zero no")
        return
    while no != 0:
        r = int(no % 10)
        count +=1
        no = int(no/10)
    print(count)
num=int(input("enter a num"))
check(num)


def check(name):
    #for i in name:
        #print(name.index(i))
    str = ""
    for i in name:
        str = i + str
    print(str)
name=input("enter a string")
check(name)
"""
import sys

x = sys.argv[1]
print(x)

