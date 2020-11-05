"""
1. Accept N numbers from user and return frequency of even numbers.  Input : N : 6
Elements : 85 66 3 80 93 88
Output : 3

2. Accept N numbers from user and return difference between frequency of  even number and odd numbers.
Input : N : 7
 Elements : 85 66 3 80 93 88 90
Output : 1 (4 -3)

3. Accept N numbers from user check whether that numbers contains 11 in  it or not.
Input : N : 6
 Elements : 85 66 11 80 93 88
Output : 11 is present
Input : N : 6
 Elements : 85 66 3 80 93 88
Output : 11 is absent

4. Accept N numbers from user and return frequency of 11 form it.  Input : N : 6
 Elements : 85 66 3 15 93 88
Output : 0
Input : N : 6
 Elements : 85 11 3 15 11 111
Output : 2

5. Accept N numbers from user and accept one another number as NO ,  return frequency of NO form it.
Marvellous Logic Building Assignment : 22
Input : N : 6
 NO: 66
 Elements : 85 66 3 66 93 88
Output : 2
Input : N : 6
 NO: 12
 Elements : 85 11 3 15 11 111
Output : 0

"""
class Ass22:
    def prog1(self,ls):
        count = 0
        for i in range(len(ls)):
            if ls[i] % 2 == 0:
                count+=1
        return count

    def prog2(self, ls):
        count1 = 0
        count2 = 0
        for i in range(len(ls)):
            if ls[i] % 2 == 0:
                count1 += 1
            else:
                count2 += 1
        return count1-count2

    def prog3(self, ls):
        for i in range(len(ls)):
            if ls[i] == 11:
                return True

    def prog4(self, ls):
        count = 0
        for i in range(len(ls)):
            if ls[i] == 11:
                count+=1
        return count

    def prog5(self, ls, No):
        count = 0
        for i in range(len(ls)):
            if ls[i] == No:
                count+=1
        return count

obj = Ass22()
ls = []
N = int(input("How many elements you want to add"))
for i in range(N):
    ele= int(input())
    ls.append(ele)
No = int(input("enter the element you wwant to search"))
#freq = obj.prog1(ls)
#print("frequency of even numbers is :",freq)

#difffreq = obj.prog2(ls)
#print("difference in between of frequency of even numbers  and odd numbers is :",difffreq)

"""checkno = obj.prog3(ls)
if checkno:
    print("11 is present")
else:
    print("11 is absent")

"""
#checkno = obj.prog4(ls)
#print("freq of 11 is :",checkno)

freq = obj.prog5(ls,No)
print("frequency of",No, "is :",freq)
