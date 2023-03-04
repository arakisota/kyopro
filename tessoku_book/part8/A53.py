"""
優先度付きキューの問題
・優先度付きキューに入っている最小の要素を取得したり削除できる
→箱の中で、常に最小値だけは管理されてる
→最大の要素の場合は少し工夫すれば実装できる

優先度付きキューはheapqを使う
→dequeと違って、listを操作する形式になっている
→そのため、T[0]で最小値をとってこれるが、T[1]で2番目に小さい値が取れるわけではないことを注意する。
"""

import heapq

Q = int(input())

T = []

for i in range(Q):
    query = input().split()
    if query[0] == "1":
        heapq.heappush(T, query[1])
    elif query[0] == "2":
        print(T[0])
    else:
        heapq.heappop(T)