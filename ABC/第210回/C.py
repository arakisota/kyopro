"""
愚直に調べるとTLEしてしまうため、どうにか工夫して、高速化を図る
（考え方）
・[i, i+K-1]の数をカウントして、[i+1, i+K]の数をカウントするとTLEする
→そのため、前の結果を活かすことを考えてみる
→[i, i+K-1]と[i+1, i+K]はiとi+K以外は同じなので、差分に注目する

(方法)
・尺取り法
→差分計算を用いて高速化する方法
→区間の右端を1つ動かしたら、条件を満たすように左端を右に動かして、調整するアルゴリズム
"""
from collections import Counter

N, K = map(int, input().split())
c = list(map(int, input().split()))
cnt = Counter(c[:K]) #そのままぶち込んでもいける
ans = len(cnt) #最初のキャンディーの種類

for i in range(K, N):
    left = c[i-K] #配列の左端
    right = c[i] #次の配列の右端
    cnt[left] -= 1
    cnt[right] += 1
    if cnt[left] == 0:
        del cnt[left] #listから0個になったキャンディーを削除する
    ans = max(ans, len(cnt))

print(ans)