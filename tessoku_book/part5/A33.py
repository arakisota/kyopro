"""
暗記問題
山が3個以上の必勝問題は以下の規則がある（証明は難しいらしい）
A1 XOR A2 XOR ... XOR = 0 -> 後手必勝
A1 XOR A2 XOR ... XOR = 1 -> 先手必勝
ちなみにこのXORの和をニム和という。
"""
#入力
N = int(input())
A = list(map(int, input().split()))

judge = A[0]
#XORは^で表す
for i in range(1, len(A)):
    judge = judge ^ A[i]

if judge == 0:
    print("Second")
else:
    print("First")