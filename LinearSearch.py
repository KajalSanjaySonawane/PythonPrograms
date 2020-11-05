pos = -1
def LinearSearch(vals,valToSearch):
    for i in range(len(vals)):
        if vals[i] == valToSearch:
            globals() ['pos'] = i
            return True;
    else:
        return False;

vals = [10,5,2,6,8,1]
valToSearch = int(input("enter the no to be searched within list"))
if LinearSearch(vals,valToSearch):
    print("found",pos+1)
else:
    print("not found")