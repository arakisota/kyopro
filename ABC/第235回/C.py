"""
（解き方）
クエリ問題の定石として、先に用意しておくこと
→今回は先にどの数字がどのタイミングで出てくるのかを事前に用意しておく。
→そうすることでO(Q)で済む
→defaultdictで簡単にできる
"""

from collections import defaultdict

N, Q = map(int, input().split())
a = list(map(int, input().split()))
cnt = defaultdict(list)
for i in range(N):
    cnt[a[i]].append(i)
key = set(cnt.keys())

for i in range(Q):
    x, k = map(int, input().split())
    if x not in key:
        print(-1)
    else:
        if k > len(cnt[x]):
            print(-1)
        else:
            print(cnt[x][k-1] + 1)