"""
1. Accept N numbers from user and accept one another number as NO ,  check whether NO is present or not.
 Input : N : 6
 NO: 66
 Elements : 85 66 3 66 93 88
 Output : TRUE
 Input : N : 6
 NO: 12
 Elements : 85 11 3 15 11 111
Output : FALSE

2. Accept N numbers from user and accept one another number as NO ,  return index of first occurrence of that NO.  
 Input : N : 6
 NO: 66  
 Elements : 85 66 3 66 93 88  
 Output : 1

 Input : N : 6
 NO: 12
 Elements : 85 11 3 15 11 111
 Output : -1

3. Accept N numbers from user and accept one another number as NO ,  return index of last occurrence of that NO.
 Input : N : 6
 NO: 66
 Elements : 85 66 3 66 93 88
 Output : 3
 Input : N : 6
 NO: 93
 Elements : 85 66 3 66 93 88
 Output : 4
 Input : N : 6
 NO: 12
 Elements : 85 11 3 15 11 111
 Output : -1

4. Accept N numbers from user and accept Range, Display all elements from  that range
Input : N : 6
 Start: 60

 End : 90

 Elements : 85 66 3 76 93 88
Output : 66 76 88
Input : N : 6
 Start: 30

 End : 50

 Elements : 85 66 3 76 93 88

5. Accept N numbers from user and return product of all odd elements.
 Input : N : 6
 Elements : 15 66 3 70 10 88
 Output : 45
 Input : N : 6
 Elements : 44 66 72 70 10 88
 Output : 0
"""

pos = 0
first = -1
last = -1
countOdd = 1

class prog23:
    def prog1(self, ls, NO):
        for i in range(len(ls)):
            if ls[i] == NO:
                globals()['pos'] = i
                return True
        else:
            return False

    def prog3(self, ls, NO):
        for i in range(len(ls)):
            if ls[i] != NO:
                continue
            elif first == -1:
                globals()['first'] = i
            globals()['last'] = i

        if first != -1:
            return True
        else:
            return False

    def prog4(self, ls, start,end):
        for i in range(len(ls)):
            if start <= ls[i] or ls[i] >= end:
                print(ls[i])

    def prog5(self,ls):
        for i in range(len(ls)):
            if ls[i] % 2 != 0:
                globals()['countOdd'] = countOdd * ls[i]
        return countOdd

obj = prog23()
N = int(input("how many ele you want to insert"))
ls = []
for i in range(N):
    ele = int(input())
    ls.append(ele)

print("entered elements are :", ls)
NO = int(input("enter the no you want to search in array"))
check = obj.prog1(ls,NO)
check = obj.prog3(ls, NO)

if check:
    print("NO is present at location", last+1)
    print("first occurence",first+1)
    print("last occurence",last+1)
else:
    print("NO is absent")

start = int(input("enter the starting range"))
end = int(input("enter the end range"))
obj.prog4(ls,start,end)

obj.prog5(ls)
print("product of all odd elements are : ",countOdd)