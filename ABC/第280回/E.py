N, P = map(int, input().split())

#動的計画法
#dp[i][0] : i+1からくるパターン
#dp[i][1] : i+2からくるパターン
dp = [0] * (N+1)
dp[-1] = 1
dp[-2] = 1
for i in reversed(2, range(N)):
    dp[i] = dp[i+1] + dp[i+2] + 2