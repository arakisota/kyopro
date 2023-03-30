"""
右から入れて、左から出すので、キューを使えば良い
→deque
（コツ）
まとめて塊ごとに処理していく
→ランレングス圧縮(Run Length)という
"""
from collections import deque

Q = int(input())
deq = deque()
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x, c = query[1], query[2]
        deq.append([x, c])
    else:
        c = query[1] #取り出す個数
        sm = 0 #ボールの合計
        while c > 0:
            num, cnt = deq[0]
            if c >= cnt:
                sm += num * cnt
                deq.popleft()
                c -= cnt
            else:
                sm += num * c
                deq[0][1] -= c
                c = 0
        print(sm)