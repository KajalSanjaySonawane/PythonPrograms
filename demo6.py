"""Pattern printing
outut:
1234
5678
1234
5678
"""
i=1
while i<=4:
    if i%2==0:
        j=5
        while j<=8:
            print(j,end="")
            j+=1
    else:
        j=1
        while j<=4:
            print(j,end="")
            j += 1
    print()
    i += 1