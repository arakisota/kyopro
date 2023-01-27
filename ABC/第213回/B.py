import copy
N = int(input())
A = list(map(int, input().split()))

cp = copy.copy(A)
A.sort()
print(cp.index(A[-2])+1)