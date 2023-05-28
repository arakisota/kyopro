"""
最後が0になってもいい
→N-Kでアイテムを消費すればいい
→N-2Kでアイテムを消費する

よって、H+KM >= Nであればいい
"""

from collections import defaultdict

N, M, H, K = map(int, input().split())
S = input()
xy = defaultdict(int)
for i in range(M):
    x, y = map(int, input().split())
    xy[(x,y)] = 1

def act(x, y, action):
    if action == "R":
        x += 1
    if action == "L":
        x -= 1
    if action == "U":
        y += 1
    if action == "D":
        y -= 1
    return x, y

now_x = 0
now_y = 0
judge = True
for action in S:
    now_x, now_y = act(now_x, now_y, action)
    #print(now_x, now_y)
    H -= 1
    if H < 0:
        judge = False
        break
    if xy[(now_x, now_y)] == 1 and H < K:
        H = K
        xy[(now_x, now_y)] = 0
    #print("H", H)

if judge:
    print("Yes")
else:
    print("No")