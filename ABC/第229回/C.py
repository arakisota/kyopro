"""
from operator import itemgetterはindexを指定する関数
itemgetter(0) == lambda x:x[0]と同じ役割を持つ。
→だが、実行速度がitemgetterの方が倍くらい速い
https://www.haya-programming.com/entry/2018/05/22/234809
（解き方）
・一見、ナップザック問題で解けそうだが、今回は重さWが3*10^8とかなり大きいため、TLEしてしまう。
→そのため、美味しさAをソートして、貪欲法で埋めていくのが良い
"""

from operator import itemgetter

N , W = map(int, input().split())
AB = []
#これで二次元配列の入力方法になる
AB = [list(map(int, input().split())) for _ in range(N)]
AB.sort(reverse=True, key=itemgetter(0))
ans = 0
rem = W
#二次元配列をそれぞれa, bに受け渡している
for a, b in AB:
    t = min(rem, b)
    ans += t * a
    rem -= t

print(ans)