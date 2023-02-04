"""
dpを使う問題
dp[i][j] : i番目までを使って、一番左の要素をjにできるか
（解き方）
・dp[i-1][j]の遷移
→(i+A[i])%10 or (i*A[i])%10
"""
N = int(input())
A = list(map(int, input().split()))

MOD = 998244353
dp = [[0] * 10 for _ in range(N)]
dp[0][A[0]] = 1

for i in range(1, N):
    for j in range(10):
        f = (j + A[i]) % 10
        g = (j * A[i]) % 10
        dp[i][f] += dp[i-1][j]
        dp[i][g] += dp[i-1][j]
        dp[i][f] %= MOD
        dp[i][g] %= MOD

for i in range(10):
    print(dp[N-1][i])