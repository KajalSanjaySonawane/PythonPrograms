# Basic Array Program
from array import *

"""
1)
val= array('i' ,[10,50,40,60,20])    # 'i' is for signed int
for i in val:
    print(i)

2)
val = array('I',[5,4,8,6,2,3])    #'I' is for unsigned int

newArray = array(val.typecode,(a*3 for a in val))    # Copy first array into second and a*a means do some operation on newarray
for j in newArray:
    print(j)

3)
k = array('u',['K','J','L','A'])   # 'u' is for unicode character
for i in k:
    print(i)

4)
#Odd even no and their count
val = array('i',[1,2,3,4,5,6,7,8,9,10])
count=0
for i in val:
    if i%2 == 0 :
        count+=1
        print(val.index(i),"->",i)
print("Count of even no's are", count)

5)
val = array('i',[100,75,40,25,85,69,26,56,23,12,0,3,5,98])
count1=0
count2=0
for i in val:
    if i>50:
        print(i)
        count1 +=1
    elif i<50 :
        print(i)
        count2 +=1
print("Count of values greater than 50 are",count1)
print("Count of values greater than 50 are",count2)

6) 
#Print the sum of array elements below 50 if sum goes beyond 50 stop the addition.
val = array('i', [5, 4, 8, 6, 2, 3, 86, 0, 2, 5])
# print(sum(val))
ans = 0
for i in val:
    if i<=50:
        ans = ans + i
    else:
        break

print(ans)

7)
val= array('i',[4,2,10,9,7,8,5,20,4])  #Sort the array elements Ascending/ Descending
temp=0
for i in range(0,len(val)):
    for j in range(i+1,len(val)):
        if val[i]>val[j]:
            temp=val[i]
            val[i]=val[j]
            val[j]=temp
for e in range(0,len(val)):
    print(val[e])
"""
l1 = ['abc','bv','ccc']
l1+='de'
print(l1)