def max(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    print(arr)
    max = arr[-1]
    print(max)
    for i in range(len(arr),0,-1):
        if max <= arr[i-1]:
            secmax = arr[i-1]
            print(secmax)

arr = [2,3,6,6,5]
max(arr)