"""
区間DP
考えられるパターン
①dp[l-1][r]の状態から、左端のブロックを取り除く -> l≦Pl-1≦rの時Al-1点
②dp[l][r+1]の状態から、右端のブロックを取り除く -> l≦Pr+1≦rの時Ar+1点
"""
#入力
N = int(input())
P = [0] * (N+1)
A = [0] * (N+1)

for i in range(1, N+1):
    P[i], A[i] = map(int, input().split())

#区間DP
#左端と右端しか取らないため、l番目からr番目までのブロックが残っている
dp = [[0] * (N+1) for i in range(N+1)]

#初期条件
dp[1][N] = 0
for LEN in reversed(range(0, N-1)):
    for l in range(1, N-LEN+1):
        r = l + LEN

        #score1(l-1番目のブロックを取り除くときの得点)
        score1 = 0
        if l >= 2 and l <= P[l-1] and P[l-1] <= r:
            score1 = A[l-1]
        #score2(r+1番目のブロックを取り除くときの得点)
        score2 = 0
        if r <= N-1 and l <= P[r+1] and P[r+1] <= r:
            score2 = A[r+1]

        if l == 1:
            dp[l][r] = dp[l][r+1] + score2
        elif r == N: 
            dp[l][r] = dp[l-1][r] + score1
        else:
            dp[l][r] = max(dp[l-1][r] + score1, dp[l][r+1] + score2)

#出力
Answer = 0
for i in range(1, N+1):
    Answer = max(Answer, dp[i][i])
print(Answer)