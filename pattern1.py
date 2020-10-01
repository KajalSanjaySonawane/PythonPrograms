""""
-----------------using FOR--------------
Pattern printing
****
****
****
****

for i in range(1, 5):
    for j in range(1, 5):
        print("*", end="")
    print()
"""
#-----------------using WHILE--------------
i = 1
while i<=4:
    j = 1
    while j <= 4:
        print("*",end="")
        j+=1
    i+=1
    print()
