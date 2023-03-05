"""
dp[i][j]:i回目のジャンプで座標jにジャンプできるかどうか
i回目にjにいるためには、i-1回目にj-ai or j-biにいる必要がある
"""
N, X = map(int, input().split())
dp = [[False] * (X+1) for _ in range(N+1)]
dp[0][0] = True
a = [0] * N
b = [0] * N
for i in range(N):
    a[i], b[i] = map(int, input().split())
for i in range(N):
    for j in range(X+1):
        if j >= a[i] and j >= b[i]:
            if dp[i][j-a[i]] == True or dp[i][j-b[i]] == True:
                dp[i+1][j] = True
        elif j >= a[i]:
            if dp[i][j-a[i]] == True:
                dp[i+1][j] = True
        elif j >= b[i]:
            if dp[i][j-b[i]] == True:
                dp[i+1][j] = True
        else:
            pass

if dp[N][X] == True:
    print("Yes")
else:
    print("No")