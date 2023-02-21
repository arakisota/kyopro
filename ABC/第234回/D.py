"""
大きい方からK個だけを袋に入れるイメージで、その中より大きい数がでたら、最小の数字を捨てる。
→優先度付きキュー(Priority queue)
・最小値（最大値）をO(logN)で取り出す
・要素をO(logN)で挿入する
・heapqは先頭の要素のみ最小になっている
"""

from heapq import heapify, heappop, heappush

N, K = map(int, input().split())
P = list(map(int, input().split()))

ans = P[:K]
heapify(ans)
print(ans[0])

for i in P[K:]:
    heappush(ans, i)
    heappop(ans)
    print(ans[0])