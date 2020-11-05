def BubbleSort(val):
    for i in range(len(val)-1,0,-1):
        for j in range(i):
            if val[j]>val[j+1]:
                temp = val[j]
                val[j] = val[j+1]
                val[j+1] = temp

val= [10,5,6,3,8,9,2,1,45]
BubbleSort(val)
print(val)