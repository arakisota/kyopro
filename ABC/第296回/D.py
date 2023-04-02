"""
1 <= a, b <= N
X = ab
b = X / a
M <= X <= N^2

a, bの最小公倍数を求めて、その中でM以上の最小の値が答え
"""
from math import gcd

N, M = map(int, input().split())

if N**2 < M:
    print(-1)
elif N >= M:
    print(M)
else:

