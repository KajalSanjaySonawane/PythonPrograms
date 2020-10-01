"""1.Write a program which accept range from user and display all numbers in between  that range.
Input : 23 35
Output : 23 24 25 26 27 28 29 30 31 32 33 34 35

def checkrange(start,end):
    if start>end:
        print("Invalid range")
    for i in range(start,end+1):
        print(i," ",end="")
start = int(input("enter a start no"))
end = int(input("enter a end no"))
checkrange(start,end)

2. Write a program which accept range from user and display all even numbers in  between that range.

def checkrange(start,end):
    if start>end:
        print("Invalid range")
    for i in range(start,end+1):
        if i%2 == 0:
            print(i," ",end="")
start = int(input("enter a start no"))
end = int(input("enter a end no"))
checkrange(start,end)

3. Write a program which accept range from user and return addition of all numbers  in between that range. (Range should contains positive numbers only)
Input : 23 30
Output : 212
Input : -10 2
Output : Invalid range

def checkrange(start,end):
    res = 0
    if start > end or start<0:
        print("Invalid range")
        return
    for i in range(start,end+1):
        res = res +i
    print(res)
start = int(input("enter a start no"))
end = int(input("enter a end no"))
checkrange(start,end)

4.Write a program which accept range from user and return addition of all even  numbers in between that range. (Range should contains positive numbers only)
Input : 23 30
Output : 108
Input : 10 18
Output : 70
Input : -10 2
Output : Invalid range
Input : 90 18
Output : Invalid range

def checkrange(start,end):
    res = 0
    if start > end or start<0:
        print("Invalid range")
        return
    for i in range(start,end+1):
        if i %2 ==0:
            res = res +i
    print(res)
start = int(input("enter a start no"))
end = int(input("enter a end no"))
checkrange(start,end)

5.Write a program which accept accept range from user and display all numbers in  between that range in reverse order.
Input : 23 35
Output : 35 34 33 32 31 30 29 28 27 26 25 24 23
Input : 10 18
Output : 18 17 16 15 14 13 12 11 10
Input : 10 10
Output : 10
Input : -10 2
Output : 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
Input : 90 18
Output : Invalid range
"""
def checkrange(start,end):
    res = 0
    if start > end or start<0:
        print("Invalid range")
        return
    i=end
    while (i>=start):
        print(i," ",end="")
        i-=1
start = int(input("enter a start no"))
end = int(input("enter a end no"))
checkrange(start,end)


