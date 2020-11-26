"""Each variable  and  will have values of 0 or 1 . All permutations of lists in the form .
Remove all arrays that sum to  to leave only the valid permutations.

Print the list in lexicographic increasing order.
Sample Input 
1
1
1
2

SAmple output: [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
"""

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    ls = []
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if i+j+k != n:
                    ls.append([i,j,k])
    print(ls)
