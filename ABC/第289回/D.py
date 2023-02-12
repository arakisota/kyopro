"""
非常にやりやすい一次元DPの問題
（解き方）
いま、ロボットがk段目にいるとする。
「ここからl段目に到達できるかどうか」は、「これまでどのような動き方をしてきたか」と関係ない。
→「今いる段数」を状態として持つDPを考えることができる。
dp[i] : i段目に登ることができるなら1、できないなら0とする。
"""

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
X = int(input())

dp = [0] * (X+1)
for i in B:
    dp[i] = -1
dp[0] = 1
for i in range(X):
    if dp[i] == 1:
        for a in A:
            if i + a <= X and dp[i+a] != -1:
                dp[i+a] = 1
if dp[X] == 1:
    print("Yes")
else:
    print("No")