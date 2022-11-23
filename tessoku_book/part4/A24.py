"""
最長増加部分列問題
"""

N = int(input())
A = list(map(int, input().split()))

#単純な動的計画法
dp = [0 * N]
"""
dp[i]を最後の要素がAiである部分列のうち、最長のものの長さ
方法は2通り
1. 要素Aiだけからなる列
2. i > jのとき、dp[j]の後ろに繋げる → dp[j]+1
"""
for i in range(N):
    dp[i] = 1
    for j in range(i):
        dp[i] = max(dp[i], dp[j]+1)

#工夫した動的計画法
