def BinarySearch(vals,valToSearch):
    lb = 0
    ub = len(vals)-1
    pos = -1

    while lb <= ub:
        mid = (lb+ub)//2

        if vals[mid] == valToSearch:
            globals()['pos'] = mid
            return True
        else:
            if vals[mid] < valToSearch:
                lb = mid+1
            else:
                ub = mid-1
    return False

vals = [15,45,56,89,5236,1256]
valToSearch = int(input("enter the no which you want to search in list"))
if BinarySearch(vals,valToSearch):
    print("no is found at pos ",pos+1)
else:
    print("no not found")