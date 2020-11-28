a,M=(int(input()),input().split())
c,N=(int(input()),input().split())
x=set(M)
y=set(N)
one = x.difference(y)
two = y.difference(x)
res = one.union(two)
print ('\n'.join(sorted(res, key=int)))

"""
input:
4
2 4 5 9
4
2 4 11 12

output:
5
9
11
12

TASK: 
The term symmetric difference indicates those values that exist in either M or N but do not exist in both.
"""
