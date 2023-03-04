"""
セグメント木の問題 : RMQ(Range Maximum Queries)
→セグメント木はXX番目からYY番目までの要素の最大値を求める問題に強いデータ構造
→区間ごとの最大値が木構造になっている
→下から順に区間が大きくなっていく
"""

N, Q = map(int, input().split())
A = [0] * N
for i in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        A[query[1]-1] = query[2]
    else:
        print(max(A[query[1]-1 : query[2]-2]))