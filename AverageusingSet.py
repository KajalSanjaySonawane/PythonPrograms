ef average(array):
    # your code goes here
    avg = float(sum(set(array)))/len(set(array))
    return avg

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
