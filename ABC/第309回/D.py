from queue import Queue

def BFS(G, N, start=1):
    ans = 0
    start -= 1
    dist = [-1] * N #startからの距離
    cnt = [0] * N #Nまでの最短で行くパターン数
    cnt[0] = 1 #初期値

    que = Queue()

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
            ans = max(dist[next_v], ans)
    return ans

#グラフの入力の受け方
N1, N2, M = map(int, input().split())

G = [[] for i in range(N1+N2)]
for i in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    # 頂点 A から頂点 B への辺を張る
    G[A].append(B)

    # 無向グラフの場合は次も実施
    G[B].append(A)
N = N1 + N2
ans1 = BFS(G, N, start=1)
ans2 = BFS(G, N, start=N)

print(ans1+ans2+1)