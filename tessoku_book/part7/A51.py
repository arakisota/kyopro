"""
・スタックの問題
→スタックは箱に上から詰めていって、上から出すデータ構造
→後入先出し→LIFO(Last In First Out)

・スタックのライブラリ
dequeモジュールを使う
"""
from collections import deque

Q = int(input())
S = deque()
for i in range(Q):
    tmp = input()
    if tmp[0] ==  "1":
        num = tmp[0]
        S.append(tmp[1:])
    elif tmp[0] == "2":
        print(S[-1])
    else:
        S.pop()

"""
モジュールなしver
"""
Q = int(input())
stack = []
for i in range(Q):
    tmp = input()
    if tmp[0] ==  "1":
        num = tmp[0]
        name = tmp[1:]
        stack.append(name)
    elif tmp[0] == "2":
        print(stack[-1])
    else:
        stack.pop(-1)
