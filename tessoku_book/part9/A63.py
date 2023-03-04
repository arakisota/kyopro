from queue import Queue

"""BFSをキューを用いて実装する。startを指定することでそこからの値が求まる"""
def BFS(G, start=1):
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
    return dist, cnt

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

dist, _ = BFS(G)
for i in range(N):
    print(dist[i])