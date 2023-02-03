"""
まずN <= 2000だから、ペアを全探索する。その後に一つずつ個数をカウントしていけば良い
（コツ）
・座標系の問題はtupleで受け取って、listやsetにすると扱いやすいかもしれない
・先に左下と右上を決めて、残りは(x1, y2), (x2, y1)があるかどうかを調べればいい
→ただ最後に2で割る必要がある
→右上と左下の決定の仕方が二重でカウントしているため
"""

N = int(input())
z = []
s = set()

for i in range(N):
    x, y = map(int, input().split())
    s.add((x, y))
    z.append((x, y))
ans = 0
for i in range(N):
    for j in range(i+1, N):
        x1, y1 = z[i]
        x2, y2 = z[j]
        if x1 == x2 or y1 == y2:
            continue
        if (x1, y2) in s and (x2, y1) in s:
            ans += 1
print(ans//2)