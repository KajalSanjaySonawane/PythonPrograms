"""1)
#Accept one number from user and print that number of * on screen.
def accept(num):
    for i in range(num):
        print("* ",end="")

num=int(input("enter a no"))
accept(num)

2)Accept one number from user and print that number of * on screen using WHILE loop
def Display(num):
    i = 0
    while num>i:
        print("*")
        num -= 1

num = int(input("Enter a number"))
Display(num)

3)Accept on number from user if number is less than 10 then print
“Hello” otherwise print “Demo”.

def Show(no):
    if(no<10):
        print("Hello")
    else:
        print("Demo")

num = int(input("Enter a number"))
Show(num)


4)Accept number from user and check whether number is even or
odd.

def Check(num):
    if num % 2 == 0:
        print("NO is Even")
    else:
        print("No is odd")
Check(int(input("enter a no")))

5)Accept two numbers from user and display first number in second
number of times.
"""

def Check(num,freq):
    for i in range(freq):
        print(num," ",end="")
num=int(input("Enter a number"))
freq= int(input("Enter a frequency"))
Check(num,freq)

