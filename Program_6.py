"""1.Write a program which accept number from user and display its digits in reverse  order.
Input : 2395
Output : 5
 9
 3
 2

def reverse(no):
    r = 0
    while no > 0:
        r = r * 10
        r = r + (int(no % 10))
        no = no // 10 #floor opeartor //
    return r
num = int(input("enter a number"))
ans=reverse(num)
print(ans)

2.Write a program which accept number from user and check whether it contains 0  in it or not.
Input : 2395
Output : There is no Zero
Input : 1018
Output : It Contains Zero
Input : 9000
Output : It Contains Zero
Input : 10687
Output : It Contains Zero

#alternate logic convert it into string and then check every digit
def check(no):
    for i in no:
        if no[int(i)] == '0':
            return True
            break
        else:
            return False

num=input("Enter any number")
ans=check(num)
if ans == True:
    print("It Contain zero")
else:
    print("There is no Zero")


#One more logic first take one by one digit from number and then check codition
"""

def check(no):
    r = 0
    result = 0
    if no == 0:
        print("Enter non-zero value")
        return

    while no != 0:
        r = int(no % 10)
        no = no // 10
        if r == 0:
            result = 1  #if condiiton true return true
            break

    return result

num = int(input("enter a number"))
res=check(num)
if res:
    print("zero")
else:
    print('non-zero')

"""
3.Write a program which accept number from user and count frequency of 2 in it.
Input : 2395
Output : 1
Input : 1018
Output : 0
Input : 9000
Output : 0
Input : 922432
Output : 3

def freq(no):
    r = 0
    cnt = 0
    while no > 0:
        r = int(no % 10)
        no = int(no / 10)
        if r == 2:
            cnt+=1
    return cnt
num = int(input("enter a number"))
ans=freq(num)
print(ans)

4.Write a program which accept number from user and count frequency of 4 in it.
Input : 2395
Output : 0
Input : 1018
Output : 0
Input : 9440
Output : 2
Input : 922432
Output : 1

def freq(no):
    r = 0
    cnt = 0
    while no > 0:
        r = int(no % 10)
        no = int(no / 10)
        if r == 4:
            cnt+=1
    return cnt
num = int(input("enter a number"))
ans=freq(num)
print(ans)

5.Write a program which accept number from user and count frequency of such a  digits which are less than 6.
Input : 2395
Output : 3
Input : 1018
Output : 3
Input : 9440
Output : 3
Input : 96672
Output : 1


def freq(no):
    r = 0
    cnt = 0
    while no > 0:
        r = int(no % 10)
        no = int(no / 10)
        if r < 6:
            cnt+=1
    return cnt
num = int(input("enter a number"))
ans=freq(num)
print(ans)
"""
