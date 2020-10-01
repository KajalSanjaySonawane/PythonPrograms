"""
Pattern Printing
___*
__*
_*
*
"""
#-----------------------Using WHILE----------------------
i=1
while i<=4:
    j=i
    while j<=i:
        k=1
        while k<=4-i:
            print("_ ",end="")
            k=k+1
        j = j + 1
        print("* ",end="")
        print()
    i=i+1


#-------------------Using for-----------------
for i in range(4):
    for j in range(i):
        if j<=i:
            for k in range(4-i):
                print("- ", end="")
        print("* ",end="")
        print()
