"""
dp[i][0or1] : X[i]A[i]orB[i]を選んだ時に組み合わせがあるかどうか
（注意）
これを最初に組み合わせの数でやると、条件分岐に対して計算量が多くなりすぎてしまいTLEやMLEしてしまった。
→今回の場合は、できるかどうかなのでTrue or Falseで十分足りる
→実際にこれでACできた
"""

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [[False]*2 for _ in range(N)]
dp[0][0] = True
dp[0][1] = True
for i in range(N-1):
    if dp[i][0]:
        if abs(A[i+1] - A[i]) <= K:
            dp[i+1][0] = dp[i][0]
        if abs(B[i+1]- A[i]) <= K:
            dp[i+1][1] = dp[i][0]
    if dp[i][1]:
        if abs(A[i+1]- B[i]) <= K:
            dp[i+1][0] = dp[i][1]
        if abs(B[i+1]- B[i]) <= K:
            dp[i+1][1] = dp[i][1]

ans = dp[N-1][0] | dp[N-1][1]

if ans:
    print("Yes")
else:
    print("No")