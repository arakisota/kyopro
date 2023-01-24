"""
（解き方）
・優先度付きキューを使う
→要素の追加や削除があるときにソートの代わりに使うもの
→https://qiita.com/T_Wakasugi/items/dac6eb77a3cace54f95e

（コツ）
・操作2で全ての数字で書き換える最悪ケースを考えるとこれだけでO(10^9)になってしまい、TLEする
→そのため、全体に足された値を管理する
"""

from heapq import heappop, heappush

Q = int(input())
pq = []
S = 0 #全体に足された値
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0]== 1:
        x = q[1]
        heappush(pq, x-S) #x-Sにすることで、全体に足すSと相殺して、Sになるように調整する
    elif q[0] == 2:
        x = q[1]
        S += x
    else:
        y = heappop(pq) #最小値を取得
        print(y + S) #最後にしっかり足された分を足してから出力する