"""#FUnction Syntax
1.
def Small():
    print("hello")
Small()

2.
res=int(input("enter number"))
print(res+1)

3.
def info(data, **data1):    #** means takes multiple data in key-Value format
    print(data)
    for i,j in data1.items():
        print(i,j)              #one by one print

info(10, name='kajal', city='pune', mobno=25631025)

4.
def info(data, **data1):    #** means takes multiple data in key-Value forma
        print(data)
        print(data1)            #in one line print

info(10, name='kajal', city='pune', mobno=25631025)

5.Take 10 names from user and print those names who has more than 5 letters in their name.

def count(name):
    for i in name:
        if len(i) > 5:
            print("the name contents more than 5 letter is :",i)
name = []
for i in range(1,6):
    name.append(input("Enter a name"))
print(name)

count(name)

6.Fibonnacci Series

ele1 = 0
ele2 = 1
for i in range(2,10):
    ans = ele1 + ele2
    ele1 = ele2
    ele2 = ans
    print(ans)

7.Factorial number e.g.5!=1*2*3*4*5 =>120

def fact(no):
    count = 1
    for i in range(1,no+1):
        count = i * count
    print(count)

num = int(input("enter a number for factorial"))
fact(num)

#Using recursion
def fact(no):
    if no == 0:
        return 1
    return no * fact(no-1)

num = int(input("enter a number for factorial"))
res = fact(num)
print("factorial of given no is : ",res)
"""


def gfg(x, l=[]):
    for i in range(x):
        l.append(i * i)
        print(i)
    print(l)


gfg(2)
gfg(3, [3, 2, 1])
gfg(3)
gfg(4)
gfg(3, [10,15,16])
