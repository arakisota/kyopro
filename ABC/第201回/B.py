"""
二次元配列にして、ソートする。そして2番目を出力すればいける
"""

N = int(input())
S = [0] * N
T = [0] * N

for i in range(N):
    S[i], T[i] = map(str, input().split())
    T[i] = int(T[i])

temp = sorted(T)

print(S[T.index(temp[-2])])