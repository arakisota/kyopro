from collections import defaultdict

#グラフの入力の受け方
N, M = map(int, input().split())
a = []
for i in range(M):
    a.append(list(map(int, input().split())))

G = defaultdict(set)
for i in range(M):
    for j in range(N-1):
        A = a[i][j] - 1
        B = a[i][j+1] - 1
        # 頂点 A から頂点 B への辺を張る
        G[A].add(B)

        # 無向グラフの場合は次も実施
        G[B].add(A)

ans = 0
for i in range(N):
    tmp = N - len(G[i]) - 1
    ans += tmp

print(ans // 2)