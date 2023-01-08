"""
・前もって数をカウントしておくことで、計算量を省く
→同じような処理を何度も行うような問題に対しては、こういう方法が有効
・今回の場合は先にB[C[j]]を別の配列で用意しておくことで考えやすくなる
"""

import collections

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

temp = [0] * N
for i in range(N):
    temp[i] = B[C[i]-1]

#辞書型になる
count_a = collections.Counter(A)
count_temp = collections.Counter(temp)

set_a = set(A)
answer = 0
for i in set_a:
    ans = count_a[i] * count_temp[i]
    answer += ans

print(answer)