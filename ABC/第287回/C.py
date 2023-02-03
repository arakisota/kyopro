"""
パスグラフを判定する問題
（用語）
・パスグラフ
→一本鎖になっているグラフ
（解法）
・必要条件
→次数が1が2つで、それ以外は次数が2つになっている
→だがしかし、それぞれが分離した状態がこれの反例になっているため、十分条件を加える必要がある
・十分条件
→連結性がある
"""

from queue import Queue

def BFS(G, start=0):
    # 各頂点が何手目に探索されたか
    # -1 は「まだ探索されていない」ことを表す
    start -= 1
    dist = [-1] * N #startからの距離
    cnt = [0] * N #Nまでの最短で行くパターン数
    cnt[0] = 1 #初期値

    # todo リストを表すキュー
    que = Queue()

    # startを始点とする
    dist[start] = 0
    que.put(start)

    # キューが空になるまで探索する
    while not que.empty():
        # キューから頂点を取り出す
        v = que.get()

        # 頂点 v から 1 手で行ける頂点 next_v を探索
        for next_v in G[v]:
            # 頂点 next_v が探索済みであれば何もしない
            if dist[next_v] != -1:
                if dist[next_v] == dist[v] + 1:
                    cnt[next_v] += cnt[v]
                continue

            # 頂点 next_v を探索する
            dist[next_v] = dist[v] + 1 #startから何手かかったか
            que.put(next_v)
            cnt[next_v] = cnt[v]
    return dist

#グラフの入力の受け方
N, M = map(int, input().split())
G = [[] for i in range(N)]
for i in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    # 頂点 A から頂点 B への辺を張る
    G[A].append(B)

    # 無向グラフの場合は次も実施
    G[B].append(A)

length = []
ans = 0
cnt = 0
dist = BFS(G)
#print(dist)
for g in G:
    if len(g) == 1:
        cnt += 1
    if len(g) > 2:
        ans = 1
        break
    if cnt > 2:
        ans = 1
        break

if min(dist[:-1]) == 0 or M == 0 or M!=N-1:
    ans = 1
#print(dist)
#print(dist[:-1])
#print(ans)
if ans == 1 or min(dist[:-1]) == 0:
    print("No")
else:
    print("Yes")