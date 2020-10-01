"""1.Write a program which accept number from user and return the count of even digits.
Input: 2395
Output: 1
Input: 1018
Output: 2
Input: -1018
Output: 2
Input: 8462
Output: 4
"""
def checkEVEN(no):
    cnt = 0
    while no != 0:
        r = int(no % 10)
        if int(r % 2) == 0:
            cnt += 1
        no = int(no / 10)
    return cnt

"""
num=int(input("enter a num"))
res=checkEVEN(num)
print(res)

2.Write a program which accept number from user and return the count of odd digits.
Input : 2395
Output : 3
"""
def checkOdd(no):
    cnt = 0
    while no != 0:
        r = int(no % 10)
        if int(r % 2) != 0:
            cnt += 1
        no = int(no / 10)
    return cnt

"""
num=int(input("enter a num"))
res=checkOdd(num)
print(res)

3.Write a program which accept number from user and return the count of digits in  between 3 and 7.
Input : 2395
Output : 1
Input : 1018
Output : 0
Input : 4521
Output : 2
Input : 9922
Output : 0

def check(no):
    cnt = 0
    while no != 0:
        r = int(no % 10)
        if (r > 3) and (r < 7):
            cnt += 1
        no = int(no / 10)
    return cnt

num=int(input("enter a num"))
res=check(num)
print(res)

4.Write a program which accept number from user and return multiplication of all  digits.
Input : 2395
Output : 270
Input : 1018
Output : 8
Input : 9440
Output : 144
Input : 922432
Output : 864

def check(no):
    multi = 1

    while no != 0:
        multi = multi * (int(no % 10))
        no = int(no / 10)
    return multi
num=int(input("enter a number"))
result = check(num)
print(result)

5.Write a program which accept number from user and return difference between
summation of even digits and summation of odd digits.
Input : 2395
Output : -15 (2 - 17)
Input : 1018
Output : 6 (8 - 2)
Input : 8440
Output : 16 (16 - 0)
Input : 5733
Output : -18 (0 - 18)
"""
def check(no):
    sum = 0
    sum1 = 0
    while no != 0:
        r = int(no % 10)
        if r % 2 == 0:
            sum = sum + r
        else:
            sum1 = sum1 + r
        no = int(no / 10)
    return sum - sum1

num = int(input("enter a number"))
result = check(num)
print(result)
