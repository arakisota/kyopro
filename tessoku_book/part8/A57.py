"""
ダブリングの問題
→1日後、2日後、4日後、8日後、16日後、、、の入る場所を事前に計算する
→制約的に、10^9 < 2^30よりdp[30][i]まで調べれば良い
"""

N, Q = map(int, input().split())
A = list(map(int, input().split()))
queries = []
for i in range(Q):
    queries.append(list(map(int, input().split())))

#dp[i][j] : 穴jにいて、s^i日後における場所
LEVELS = 30
dp = [[0] * N for _ in range(30)]

for i in range(N):
    dp[0][i] = A[i] - 1

for i in range(1, LEVELS):
    for j in range(N):
        dp[i][j] = dp[i-1][dp[i-1][j]]

#クエリ処理
for X, Y in queries:
    current = X - 1
    for d in range(29, -1, -1):
        if ((Y >> d) & 1) == 1: #これは右シフトしていって、1になるところを条件で示している。ビット演算。
            current = dp[d][current]
    print(current + 1)