avb = 10

x= int(input("How many books u can take from store"))

i=1
while i<=x:
    if i>avb:
        print("Not Available in the store")
        print("You can Exit")
        break
    print("Available in store")
    i+=1


