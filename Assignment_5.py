"""1.Write a program which accept name from user and print that name.

Input: Piyush Khairnar
Output: Piyush Khairnar

print(input("enter your full name"))

2. Write a program which accept one number from user and check whether that
number is greater than 100 or not.

Input : 101
Output : Greater

    Input : 39
Output : Smaller

def check(no):
    if no>100:
        return True
    else:
        return False

num=int(input("enter a number"))
res=check(num)
if res:
    print("No is greater")
else:
    print("NO is smaller")

3. Write a program which accept two numbers and check whether numbers are
equal or not.

Input : 10 10
Output : Equal
Input : 10 12
Output : Not Equal
Input : 10 -10
Output : Not Equal

def equal(no1,no2):
    if no1 == no2:
        return True
    else:
        return False

num1 = int(input("enter first number"))
num2 = int(input("enter second number"))
res = equal(num1,num2)
if res:
    print("Equal numbers")
else:
    print("Not Equal numbers")

4. Write a program which accept three numbers and print its multiplication.
 Input : 5 4 7
 Output : 140
 Input : 5 0 7
 Output : 35
 Input : 5 0 0
 Output : 5
 Input : 0 0 0
 Output : 0

def multi(no1, no2, no3):
    res = 0:
    res = no1 * no2 * no3
    return res

num1 = int(input("enter first number"))
num2 = int(input("enter second number"))
num3 = int(input("enter third number"))
res1 = multi(num1, num2, num3)
print("Multiplication of 3 no's is :", res1)

5. Write a program which accept total marks & obtained marks from user and  calculate percentage.
Input : 1000 745
 Output : 74.5%
"""
def divide(ttl,obt):
    res=0
    res= (obt/ttl)*100
    return res
total=int(input("enter total marks"))
obtained=int(input("enter obtained marks"))
ans=divide(total,obtained)
print(ans,"%")