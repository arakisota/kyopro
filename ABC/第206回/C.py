"""
第200回C問題に類似した問題。
（考え方）
・整数組(i, j) 1 <= i < j <= Nの組み合わせはN * (N -1) / 2通りある。
→そのため、Ai = Ajとなる組み合わせを見つけてその分減らすだけ

・そしてこれdefaultdictじゃなくてCounterでいける。
"""

from collections import defaultdict

def f(N):
    return int(N * (N - 1) / 2)

N = int(input())
A = list(map(int, input().split()))

d = defaultdict(int)
for key in A:
    d[key] += 1

ans = f(N)
for key in set(A):
    ans -= f(d.get(key))
print(ans)