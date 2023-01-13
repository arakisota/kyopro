"""
今回はN<=2000なのでO(N^2)のような全探索をやってもTLEにならずに実行できる。
そして、開区間を±0.1させて閉区間とすれば、全て同じやり方で解くことができる。

（コツ）
・大小の判定では、排反事象を考えて、それ以外でcountするやり方でやれば簡単に求まる。
・開区間を簡単に置き換えて、閉区間として扱う。
"""

N = int(input())
t = [0] * N
l = [0] * N
r = [0] * N

ans = [0] * N
for i in range(N):
    t[i], l[i], r[i] = map(int, input().split())
    if t[i] == 1:
        ans[i] = [l[i], r[i]]
    elif t[i] == 2:
        ans[i] = [l[i], r[i]-0.1]
    elif t[i] == 3:
        ans[i] = [l[i]+0.1, r[i]]
    else:
        ans[i] = [l[i]+0.1, r[i]-0.1]

count = 0
for i in range(N):
    for j in range(i+1, N):
        if ans[i][-1] < ans[j][0] or ans[i][0] > ans[j][-1]:
            pass
        else:
            count += 1

print(count)