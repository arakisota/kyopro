from collections import defaultdict

# 無向グラフを表すクラス
class Graph:
  def __init__(self, num_vertices):
    # 頂点数
    self.num_vertices = num_vertices
    # 隣接リスト表現で、各頂点に隣接する頂点を格納する
    self.adj_list = defaultdict(list)

  def add_edge(self, u, v):
    # 無向グラフであるため、両方向に辺を追加する
    self.adj_list[u].append(v)
    self.adj_list[v].append(u)

def dfs(graph, vertex, visited):
  # 頂点を訪問済みにする
  visited[vertex] = True

  # 頂点から出る辺をたどる
  for neighbor in graph.adj_list[vertex]:
    if not visited[neighbor]:
      # 未訪問の頂点について、再帰的にDFSを実行する
      dfs(graph, neighbor, visited)

def count_connected_components(graph):
  # 各頂点を未訪問の状態とする
  visited = [False for _ in range(graph.num_vertices)]

  # 連結成分をカウントする変数
  count = 0
  for vertex in range(graph.num_vertices):
    # 未訪問の頂点を見つけたら、そこからDFSを開始する
    if not visited[vertex]:
      dfs(graph, vertex, visited)
      # DFSが終わったら、連結成分をカウントする
      count += 1
  return count

# 使用例
N, M = map(int, input().split())
# 頂点数と辺数
num_vertices = N
num_edges = M
# 無向グラフを作成する
graph = Graph(num_vertices)

u = [0] * M
v = [0] * M
for i in range(M):
    u[i], v[i] = map(int, input().split())
    graph.add_edge(u[i]-1, v[i]-1)

# 連結成分の個数を求める
result = count_connected_components(graph)
print(result)