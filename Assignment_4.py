"""1. Write a program which accept number from user and display its multiplication of factors.
Input: 12
Output: 144(1 * 2 * 3 * 4 * 6)
Input: 13
Output: 1(1)
Input: 10
Output: 10(1 * 2 * 5)

def fact_multi(no):
    if no <= 0:
        print("enter another no greater than 0")
        return
    for i in range(1,no+1):
            if no % i == 0:
                print("Factors of given number is : ", i)
    print()
    print('Multiplication of all factors is : ', i * i)

num = int(input("enter a number"))
fact_multi(num)

2)Write a program which accept number from user and display its factors in  decreasing order.
Input : 12
Output : 6 4 3 2 1
Input : 13
Output : 1
Input : 10
Output : 5 2 1

def fact_multi(no):
    if no <= 0:
        print("enter another no greater than 0")
        return
    i=int(no/2)
    while i>=1:
        if no % i == 0:
            print("Factors of given number is : ", i)
        i-=1

num = int(input("enter a number"))
fact_multi(num)

3.Write a program which accept number from user and display all its non factors.
Input : 12
Output : 5 7 8 9 10 11
Input : 13
Output : 2 3 4 5 6 7 8 9 10 11 12
Input : 10
Output : 3 4 6 7 8 9

def fact_multi(no):
    if no <= 0:
        print("enter another no greater than 0")
        return
    for i in range(1, no+1):
        if no % i != 0:
            print("Non-Factors of given no are :", i)

num = int(input("enter a number"))
fact_multi(num)

4.Write a program which accept number from user and return summation of all its  non factors.
Input : 12
Output : 50
Input : 10
Output : 37

def fact_multi(no):
    if no <= 0:
        print("enter another no greater than 0")
        return
    sum1 = 0
    for i in range(1, no+1):
        if no % i != 0:
            print("Non-Factors of given no are :",i)
            sum1 = sum1 + i
    return sum1

num = int(input("enter a number"))
res= fact_multi(num)
print("Sum of all no-factors is:",res)

5.Write a program which accept number from user and return difference between  summation of all its factors and non factors.
Input : 12
Output : -34 (16 - 50)
Input : 10
Output : -29 (8 - 37)
"""

def fact_multi(no):
    if no <= 0:
        print("enter another no greater than 0")
        return
    sum1, sum2 = 0, 0
    for i in range(1, no+1):
        if no % i != 0:
            print("Non-Factors of given no are :",i)
            sum1 = sum1 + i
            print("Summation of Non-factors are :",sum1)
    else:
        print("factors of given no are :",i)
        sum2 = sum2 + i
        print("summation of factors are : ",sum2)
    return sum1-sum2

num = int(input("enter a number"))
res = fact_multi(num)
print("Difference between summation of all it's non-factors and factors is:", res)

"""
def factors(no):
    sum1=0
    for i in range(1,int((no/2)+1)):
        if no % i == 0:
            print(i)
            sum1 = sum1 +i
    print("Summation is :",sum1)
    return sum1

def nonFactors(no):
    sum2 = 0
    for i in range(1,int(no+1)):
        if no % i != 0:
            print(i)
            sum2 = sum2 +i
    print("Summation is :", sum2)
    return sum2

num=int(input("enter a number"))
res1 = factors(num)
res2 = nonFactors(num)
print("Difference between summation of all it's non-factors and factors is:",res1-res2)
"""