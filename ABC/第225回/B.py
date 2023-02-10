N = int(input())

G = [[] for i in range(N)]
for i in range(N-1):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    # 頂点 A から頂点 B への辺を張る
    G[A].append(B)
    # 無向グラフの場合は次も実施
    G[B].append(A)

ans = 0
for i in range(N):
    if len(G[i]) == N-1:
        ans = 1
        break
if ans == 1:
    print("Yes")
else:
    print("No")