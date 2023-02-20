"""
（コツ）
部分和は累積和の引き算で求まる
（解き方）
引いてKになる数がいくつあるかが答えになる
→累積和を前から見ていって、見終わった値をCounterで管理する
→そうすれば、前から見るだけなので、O(N)で済む
"""

from itertools import accumulate
from collections import Counter

N, K = map(int, input().split())
A = list(map(int, input().split()))
ac = list(accumulate(A))
cnt = Counter()
cnt[0] += 1
ans = 0

for x in ac:
    y = x - K
    ans += cnt[y]
    cnt[x] += 1

print(ans)