"""
（ボールに書かれた整数、ボールの連続する個数）の形でリストに入れる
スタックで管理する
番兵を入れておくと楽
"""

N = int(input())
a = list(map(int, input().split()))
L = [[-1, 0]]
ans = 0
for cx in a:
    tx, cnt = L[-1]
    ans += 1
    if cx == tx:
        L[-1][1] += 1
    else:
        L.append([cx, 1])
    if L[-1][0] == L[-1][1]:
        L.pop()
        ans -= cx
    print(ans)