"""
最長共通部分文字列問題(Long Common Subsequence)
→東工大2022-3-2でも出たからなんとしてでも制覇したい
"""
#入力
S = list(input())
T = list(input())

dp = [[0] * (len(T)+1) for i in range(len(S)+1)]
for i in range(len(T)+1):
    dp[0][i] = 0

for j in range(len(S)+1):
    dp[j][0] = 0

#DP
for i in range(1, len(S)+1):
    for j in range(1, len(T)+1):
        if S[i-1] == T[j-1]:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]+1)
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp[len(S)][len(T)])