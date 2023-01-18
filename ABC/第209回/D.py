"""
木構造になっているグラフの問題。木の二部グラフ性を活用する。
（考え方）
・2人の最短距離が偶数であれば、Townで奇数であればRoadで出会うことになる
・そのため、ある位置xに対しての最短距離を偶数または奇数で全ての街を色分けする
→そうすることで、最初の2人の位置によって、どこで出会うかが計算できる
→各クエリの計算量はO(1)に抑えられる
→色の計算はBFS or DFSで求められる
"""

from queue import Queue

"""BFSをキューを用いて実装する"""
def BFS(G, start):
    # 各頂点が何手目に探索されたか
    # -1 は「まだ探索されていない」ことを表す
    dist = [-1] * N

    # todo リストを表すキュー
    que = Queue()

    # 頂点 0 を始点とする
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
                continue

            # 頂点 next_v を探索する
            dist[next_v] = dist[v] + 1 #startから何手かかったか
            que.put(next_v)
    return dist

#グラフの入力の受け方
N, Q = map(int, input().split())
G = [[] for i in range(N)]
for i in range(N-1):
    A, B = map(int, input().split())
    # 頂点 A から頂点 B への辺を張る
    G[A-1].append(B-1)
    # 無向グラフの場合は次も実施
    G[B-1].append(A-1)

#街を色付けしていく
dist = BFS(G, 0)
ans = [0] * len(dist)
for i in range(len(dist)):
    if dist[i] % 2 == 0:
        ans[i] = 1

for i in range(Q):
    c, d = map(int, input().split())
    if ans[c-1] == ans[d-1]:
        print("Town")
    else:
        print("Road")