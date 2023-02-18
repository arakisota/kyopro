"""
DPで解く問題
(i, j)は(i-1, j)か(i, j-1)のどちらかからくる以外に選択肢がない
→そのため、これらの最大値+1が(i, j)の最大値になる
dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + 1
dp[0][0] = 1とし、それ以外を-INFとして初期化する。
"""

H, W = map(int, input().split())
C = []
for i in range(H):
    tmp = list(input())
    C.append(tmp)

INF = 1 << 60
dp = [[-INF]*(W) for _ in range(H)]
dp[0][0] = 1
for i in range(H):
    for j in range(W):
        if i == 0 and j == 0:
            continue
        if C[i][j] == ".":
            if i == 0:
                dp[i-1][j] = -INF
            if j == 0:
                dp[i][j-1] = -INF
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + 1

ans = 0
for v in dp:
    tmp = max(v)
    ans = max(ans, tmp)
print(ans)