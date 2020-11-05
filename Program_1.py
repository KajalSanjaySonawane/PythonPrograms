"""1)1.Program to divide two numbers
def Divide(no1,no2):
    if no2>no1:
        print("no2 is greater than no1 so can't divide")
    else :
        ans=no1/no2
        print("Division is :",ans)

Divide(12,9)

2)Program to print 5 times “Marvellous” on screen.
def Display():
    for i in range(5):
        print("Marvellous")

Display()
"""

#3)Program to print 5 to 1 numbers on screen.
def reverseprint(no):
    i=no
    while i>=1:
        print(i)
        i-=1
reverseprint(10)

"""
#4)Accept one number and check whether is is divisible by 5 or not.

def check(num):
    if num % 5 == 0:
        return True
        #print("no is divisible by 5")
    else:
        return False
        #print("no is not divisible by 5")

num = int(input("enter a number"))
ans=check(num)
if ans:
    print("no is divisible by 5")
else:
    print("no is not divisible by 5")

5)
#Accept one number from user and print that number of * on screen.
def accept(num):
    for i in range(num):
        print("* ",end="")

num=int(input("enter a no"))
accept(num)"""
