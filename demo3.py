#----------------------Even_Odd Number print Simple logic---------------

x = int(input("Take any number and check it is even or odd"))
if x % 2 == 0:
    print(x, "is Even NO")
else:
    print(x, "is Odd NO")

#----------------------print even odd numbers from 10 to 50----------------------

for i in range(10,50):
    if i % 2 == 0:
        print(i, "is Even NO")
    else:
        print(i, "is Odd NO")