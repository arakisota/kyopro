"""
dp[l][r] : l文字目からr文字列目までの部分文字列が嬉しいかどうか
嬉しい列→ S[l : (l+r)//2] == S[(l+r)//2 : r]
(l, r)にr - l が奇数であり、かつその部分文字列が要素がそれぞれ偶数個ないとだめ
(l, r)の要素のそれぞれの個数があれば、足し引きでいける？

20230322
0 : 2
2 : 4
3 : 2

(000), 010, 110, 120, 121, 221, 222, 232, 242

(2, 7)のとき
232 - 010 = 222
(7, 8)のとき
242 - 222 = 020
(1, 6)のとき
222 - 000 = 222
(1, 5)のとき
221 - 000 = 221
"""

from collections import Counter
import copy

S = input()
N = len(S)
ans = [[False] * N for _ in range(N)]
num = [""] * N

cnt = Counter()
p = set()
r = []
for i in range(N):
    p.add(int(S[i]))
    cnt[int(S[i])] += 1

for i in reversed(range(N)):
    tmp = copy.deepcopy(cnt)
    r.append(tmp)
    cnt[int(S[i])] -= 1

