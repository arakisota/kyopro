"""
（コツ）
「袋に入っているボール個数の総積は10^5を超えない」ということは取り出し方が10^5を超えないということ
→全探索でも十分間に合う
袋内のボールは2個以上であるため、2^16 < 10^5 < 2^17より、袋の数は最大16個となる
"""

import copy

N, X = map(int, input().split())
L = [0] * N
num = [1]
for i in range(N):
    L, *A = list(map(int, input().split()))
    ans = []
    for i in range(len(num)):
        for j in range(len(A)):
            tmp = num[i] * A[j]
            ans.append(tmp)
    num = copy.copy(ans)

print(ans.count(X))