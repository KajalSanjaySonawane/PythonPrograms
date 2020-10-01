"""Pattern Print Reverse
****
***
**
*
"""
"""---------------Using While------------------------
i=1
while i<=4 :
    j=4
    while j>=i:
        print("*",end="")
        j-=1
    print()
    i+=1

"""
#--------------------Using For------------------------
for i in range(5):
    for j in range(5-i):
        print("*",end="")
    print()