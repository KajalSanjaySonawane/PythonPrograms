"""1) Write a program which accept one number from user and print that number of
even numbers on screen.
Input : 7
Output: 2 4 6 8 10 12 14

def check(num):
    i=1
    while i<=num+num:
        if i % 2 == 0:
            print(i," ",end="")
        i+=1

check(int(input("Enter a number")))

2. Write a program which accept number from user and print even factors of that  number.
Input : 24
Output: 1 2 4 6 8 12

"""
#Factorial Logic
def fact(no):
    for i in range(1,int(no/2)+1):
        if no % i == 0:
            print(i)
        #print(i)

num = int(input("enter a number:- "))
fact(num)

"""
#Print even factorials of any number
def fact(no):
    for i in range(1,int(no/2)+1):
        if no % i == 0:
            if i % 2 == 0:
                print(i)

num = int(input("enter a number"))
fact(num)

3. Write a program which accept number from user and print even factors of that  number.
Input : 36
Output: 2 6 12 18

def fact(num):
    for i in range(1,num-1):
        if num % i == 0:
            if i % 2 == 0:
                print(i)

num = int(input("enter a number for factorial"))
fact(num)

4.Accept one character from user and convert case of that character.  Input : a Output : A
Input : D Output : d

def upper(u):
    #res1 = u-32  //alternate
    res1=ord('A')+(u-ord('a'))
    #print()
    print("Uppercase char is : ",chr(res1))

def lower(l):
    #res1 = l+32    //alternate
    res1=ord('a')+(l-ord('A'))
    print("Lowercase char is : ", chr(res1))

ch = input("Enter a character")
if (ord(ch)>97) and (ord(ch)<122):
    print("enter Character is Lowercase : ",ord(ch))
    res=ord(ch)
    upper(res)
elif (ord(ch)>65 and (ord(ch)<90)):
    print("enter Character is Uppercase : ", ord(ch))
    res=ord(ch)
    lower(res)

5. Accept on character from user and check whether that character is vowel  (a,e,i,o,u) or not.
Input : E Output : TRUE
Input : d Output : FALSE

def check(ch):
    if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U'):
        return True
    else:
        return False


ch = input("enter any char")
res = check(ch)

if res== True:
    print("Char is vowel")
else:
    print("char is consonant")
"""



