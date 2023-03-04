"""
キューの問題
→キューはただの筒と同じ
→先入先出し→FIFO(First In First Out)

・キューのライブラリ
dequeモジュールを使う
"""

from collections import deque

Q = int(input())

que = deque()
for i in range(Q):
    query = input().split()
    if query[0] == "1":
        que.append(query[1])
    elif query[0] == "2":
        print(que[0])
    else:
        que.popleft()


"""
自力で実装するver
"""
Q = int(input())

que = []
for i in range(Q):
    query = input()
    if query[0] == "1":
        que.append(query[1:])
    elif query[0] == "2":
        print(que[0])
    else:
        que.pop(0)