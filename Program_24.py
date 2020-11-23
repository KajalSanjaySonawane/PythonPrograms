"""
1. Accept N numbers from user and return the largest number.  Input : N : 6
 Elements : 85 66 3 66 93 88
 Output : 93

2. Accept N numbers from user and return the smallest number.  Input : N : 6
 Elements : 85 66 3 66 93 88
 Output : 3

3. Accept N numbers from user and return the difference between largest  and smallest number.
Input : N : 6
Elements : 85 66 3 66 93 88
Output : 90 (93 -3)

4. Accept N numbers from user and display all such numbers which contains  3 digits in it.
Input : N : 6
Elements : 8225 665 3 76 953 858
Output : 665 953 858

5. Accept N numbers from user and display summation of digits of each  number.
Input : N : 6
 Elements : 8225 665 3 76 953 858
Output : 17 17 3 13 17 21
"""
max = 0
min = 0
class prog24:
    def prog1(self, ls):
        tempMax = ls[0]
        for i in range(0,len(ls)-1):
                if tempMax < ls[i+1]:
                    tempMax = ls[i+1]
        return tempMax

    def prog2(self,ls):
        tempMin = ls[0]
        for i in range(0,len(ls)-1):
            if tempMin > ls[i+1]:
                tempMin = ls[i+1]
        return tempMin

    def prog3(self,ls):
        tempMax = ls[0]
        tempMin = ls[0]
        for i in range(0,len(ls)-1):
            if tempMax < ls[i+1]:
                tempMax = ls[i+1]
            elif tempMin > ls[i+1]:
                tempMin = ls[i+1]
        return tempMax - tempMin

    def prog4(self,ls):
        for i in range(len(ls)):
            cnt = 0
            sep = ls[i]
            while sep>0:
                separator = sep % 10
                cnt += 1
                sep = sep // 10
                if cnt >= 3:
                    print("The element in list which contains more than 3 digits are :",ls[i])
                    break

    def prog5(self,ls):
        for i in range(len(ls)):
            res = 0
            sep = ls[i]
            while sep>0:
                separator = sep % 10
                res = separator + res
                sep = sep // 10
            print("Summation of each digits from each element is :",res)

obj = prog24()
N = int(input("How many elements you want to insert"))
ls = []
for i in range(N):
    ele = int(input())
    ls.append(ele)
print("entered elements are : ", ls)
max = obj.prog1(ls)
print("max element within lists is :", max)
min = obj.prog2(ls)
print("min elements are :",min)
diff = obj.prog3(ls)
print("difference between max and min element is :",diff)
obj.prog4(ls)
obj.prog5(ls)
