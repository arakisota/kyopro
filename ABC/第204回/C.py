"""
有向グラフのDFSorBFS問題
・グラフ問題の入力の受け方を覚える
"""

from queue import Queue

def BFS(G, start):
    #探索済かを判断する配列
    dist = [-1] * N
    que = Queue()

    #スタート地点をマーク
    dist[start] = 0
    que.put(start)

    while not que.empty():
        #キューから取り出す
        v = que.get()

        #vから一手でいける場所を探す
        for next_v in G[v]:
            #探索済であれば何もしない
            if dist[next_v] != -1:
                continue
            
            #頂点next_vを探索する
            dist[next_v] = dist[v] + 1
            que.put(next_v)
    return dist

#グラフ問題の入力の受け方
N, M = map(int, input().split())
G = [[] for i in range(N)]
for i in range(M):
    A, B = map(int, input().split())

    # 頂点 A から頂点 B への辺を張る
    G[A-1].append(B-1)
ans = 0
for start in range(N):
    dist = BFS(G, start)
    ans += N - dist.count(-1)
print(ans)