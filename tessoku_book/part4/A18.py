"""
部分和問題
→二次元DPの典型的な問題
dp[i][j]はindexがiまでの数字の中でjという部分和が組み合わせが存在すれば1にする。
存在しなければ0にする。
・コツ
dp[i][j] = 1となるのは、dp[i-1][j] or d[i-1][j-A[i]]となるとき
"""

N, S = map(int, input().split())
A = list(map(int, input().split()))

dp = [[0] * (S+1) for i in range(N+1)]
dp[0][0] = 1
for i in range(1, S+1):
    dp[0][i] = 0

for i in range(1, N+1):
    for j in range(S+1):
        if j >= A[i-1]:
            if dp[i-1][j] == 1 or dp[i-1][j-A[i-1]] == 1:
                dp[i][j] = 1 
            else:
                dp[i][j] = 0
        else:
            if dp[i-1][j] == 1:
                dp[i][j] = 1
            else:
                dp[i][j] = 0


if dp[N][S] == 1:
    print("Yes")
else:
    print("No")