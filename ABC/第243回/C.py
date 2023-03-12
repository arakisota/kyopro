"""
R L -> マル
L R -> ダメ
LとRのdictで管理する。その際に値をINFで初期化する
"""

from collections import defaultdict

N = int(input())
INF = (1 << 62) - 1
XY = []

for i in range(N):
    X, Y = map(int, input().split())
    XY.append((X, Y))

S = input()

L_max = defaultdict(lambda: -INF)
R_min = defaultdict(lambda: INF)
for s, (x, y) in zip(S, XY):
    if s == "L":
        L_max[y] = max(L_max[y], x)
    else:
        R_min[y] = min(R_min[y], x)

ans = 0
for y in L_max.keys():
    if L_max[y] > R_min[y]:
        ans = 1
        break

if ans == 1:
    print("Yes")
else:
    print("No")