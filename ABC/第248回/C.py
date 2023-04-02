"""
・全ての値がM以下で、合計がK以下になるN個の数列が何通りあるか
1 <= M <= M - (N-1)
N <= M <= K / N
N <= K <= NM
（解法）
・動的計画法で解く
→dp[i][j] : 数列i番目まで決めて、総和がjであるものの数
→答えはdp[N][1] + dp[N][2] + ... + dp[N][K]

（コツ）
AiからAi+1に拡張すると、総和がjからj+k(1<=k<=K)となる
"""
N, M, K = map(int, input().split())
MOD = 998244353

dp = [[0] * (K+1) for _ in range(N+1)]
dp[0][0] = 1

for i in range(N):
    for j in range(K):
        for k in range(1, M+1):
            if j + k > K:
                break
            dp[i+1][j+k] += dp[i][j]
            dp[i+1][j+k] %= MOD

print(sum(dp[-1]) % MOD)