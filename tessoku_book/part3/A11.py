"""
通常の二分探索
再帰的にLとRの値を変えていき、範囲を狭めていく方法
"""

N, X = map(int, input().split())
A = list(map(int, input().split()))

L = 0
R = N-1

while L <= R:
    M = (L + R) // 2
    if X < A[M]:
        R = M - 1
    elif X == A[M]:
        print(M + 1)
        break
    else:
        L = M + 1
 