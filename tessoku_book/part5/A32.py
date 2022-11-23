"""
先手が勝つか負けるかを考える
dpみたいにどう遷移するかを見ていくと計算量O(N)で実行できる
"""
N, A, B = map(int, input().split())
#動的計画法みたいにできる
#先手必勝または先手負け確の状況を考える

dp = [0] * (N+1)
for i in range(N+1):
    if i >= A and dp[i-A] == False:
        dp[i] = True
    elif i >= B and dp[i-B] == False:
        dp[i] = True
    else:
        dp[i] = False

if dp[-1] == False:
    print("Second")
else:
    print("First")