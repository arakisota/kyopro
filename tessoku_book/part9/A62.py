"""
DFS用いて、連結の判定を行う
（手順）
①最初は全ての頂点が白色に塗られた状態にしておく
②頂点を訪問したら、青色に塗る
→隣接する白色頂点があれば、一つ選び先に進む
→隣接する白色頂点がない場合は、一つ戻る。ただし頂点1の場合は終了する
③行動が終了したときに、全てが青色であれば連結。そうでなければ、連結ではない。

（実装方法）
・再帰関数を用いる
→計算量はO(N+M)
"""

def dfs(pos, G, visited):
    visited[pos] = True
    for i in G[pos]:
        if visited[i] == False:
            dfs(i, G, visited)

N, M = map(int, input().split())
G = [[] for _ in range(N+1)]
for i in range(M):
    A, B = map(int, input().split())
    G[A].append(B)
    G[B].append(A)

#dfs
visited = [False] * (N+1)
dfs(1, G, visited)

#連結の判定
answer = True
for i in range(1, N+1):
    if visited[i] == False:
        answer = False

if answer == True:
    print("The graph is connected.")
else:
    print("The graph is not connected.")