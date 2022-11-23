"""
しゃくとり法の実装
数列に左手と右手で仕切りを2本入れて、どんどん右に動かしていくアルゴリズム
よく使うパターン
1. 合計がK以下であるような範囲の個数を求める
2. 合計がKより大きいような範囲の個数を求める
"""

N, K = map(int, input().split())
A = list(map(int, input().split()))
R = [0] * N 

#しゃくとり法
for i in range(0, N-1):
    if i == 0:
        R[i] = 0
    else:
        R[i] = R[i-1]

    while R[i] < N-1 and A[R[i]+1] - A[i] <= K:
        R[i] += 1

#出力
Answer = 0
for i in range(0, N-1):
    Answer += (R[i] - i)
print(Answer)