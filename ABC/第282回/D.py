#グラフオブジェクトを表すクラス
class Graph:
    #コンストラクター
    def __init__(self, edges=None, n=0):
 
        #グラフ内のノードの総数
        self.n = n
 
        #隣接リストを表すリストのリスト
        self.adjList = [[] for _ in range(n)]
 
        #は無向グラフにエッジを追加します
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)
 
 
#頂点`v`から始まるグラフでDFSを実行します
def DFS(graph, v, discovered, color):
 
    #はすべてのエッジに対して実行します(v、u)
    for u in graph.adjList[v]:
 
        # 頂点`u`が初めて探索される場合は
        if not discovered[u]:
 
            #は、現在のノードを検出済みとしてマークします
            discovered[u] = True
 
            #の現在のノードは、その親とは反対の色になります
            color[u] = not color[v]
 
            # `v`をルートとするサブツリーのDFSがfalseを返す場合は
            if not DFS(graph, u, discovered, color):
                return False
 
        #頂点がすでに検出されている場合、および
        #頂点`u`と`v`が同じである場合、グラフは2部グラフではありません
        elif color[v] == color[u]:
            return False
 
    return True
 
 
# DFSを使用してグラフが2部グラフであるかどうかを確認する#関数
def isBipartite(graph):
 
    # 頂点が検出されたかどうかを追跡する
    discovered = [False] * graph.n
 
    #は、DFSの各頂点に割り当てられた色(0または1)を追跡します
    color = [False] * graph.n
 
    #は、グラフが接続され、無向であるため、任意のノードから開始します
    src = 0
 
    #は、ソース頂点を検出済みとしてマークし、その色を0(偽)に設定します
    discovered[src] = True
    color[src] = False
 
    #呼び出しDFSプロシージャ
    return DFS(graph, src, discovered, color)
 
 
if __name__ == '__main__':
    N, M = map(int, input().split())
    u = [0] * M
    v = [0] * M

    edges = []
    for i in range(M):
        u[i], v[i] = map(int, input().spplit())
        edges.append((u[i], v[i]))
 
    #グラフ内のノードの総数(0から8)
    n = len(edges)
 
    #は、指定されたエッジからグラフを作成します
    graph = Graph(edges, n)
 
    if isBipartite(graph):
        print('Graph is bipartite')
    else:
        print('Graph is not bipartite')