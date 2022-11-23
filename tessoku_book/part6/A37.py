"""
各値が何回足されたかの回数に注目する
→主客転倒テクニックと呼ばれる
より一般に、問題を複数のパーツに分解し、各パーツの答えへの寄与分を求める手法
"""
N, M, B = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))

ans = B * len(C) * len(A) + sum(A) * len(C) + sum(C) * len(A)
print(ans)