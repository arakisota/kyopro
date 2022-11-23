"""
遷移形式の工夫
→配る遷移形式（今までは貰う遷移形式）
"""

#入力
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

#配る形式にする
#dp[i]をマスiまで進んだ時の最大スコアとする
dp = [ -(10 ** 9) ] * (N + 1)
dp[1] = 0

#iから順にみていく
for i in range(1, N):
    dp[A[i-1]] = max(dp[A[i-1]], dp[i]+100)
    dp[B[i-1]] = max(dp[B[i-1]], dp[i]+150)

print(dp[-1])