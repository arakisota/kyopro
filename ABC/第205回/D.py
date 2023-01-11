"""
・クエリ問題
→クエリ問題は先読みが重要
・先に準備したら、どこにKが入るかを二分探索する
→bisectで二分探索
→計算量については、探索はO(log(N))だが、挿入はO(N)
・計算量
→1クエリに対して、二分探索でO(log(N))
"""

import bisect

N , Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
#ソートして、事前に準備する
S  = [0] * N
for i in range(N):
    S[i] = A[i] - i - 1

for i in range(Q):
    K = int(input())
    idx = bisect.bisect_left(S, K) #同じ値の時に左側のindexを返す.O(log(N))
    if idx == 0:
        print(K)
    else:
        print(A[idx-1] + (K - S[idx-1]))