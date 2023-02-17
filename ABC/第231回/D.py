"""
ループがなく、かつ隣接リストが3つ以上だと条件に合わない
→Union Findでチェック
"""

class UnionFind():
    # 初期化
    def __init__(self, n):
        self.par = [-1] * n
        self.rank = [0] * n
        self.siz = [1] * n

    # 根を求める
    def root(self, x):
        if self.par[x] == -1:
            return x # x が根の場合は x を返す
        else:
            self.par[x] = self.root(self.par[x]) # 経路圧縮
            return self.par[x]

    # x と y が同じグループに属するか (根が一致するか)
    def is_same(self, x, y):
        return self.root(x) == self.root(y)

    # x を含むグループと y を含むグループを併合する
    def unite(self, x, y):
        # x 側と y 側の根を取得する
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry:
            return False # すでに同じグループのときは何もしない
        # union by rank
        if self.rank[rx] < self.rank[ry]: # ry 側の rank が小さくなるようにする
            rx, ry = ry, rx
        self.par[ry] = rx # ry を rx の子とする
        if self.rank[rx] == self.rank[ry]: # rx 側の rank を調整する
            self.rank[rx] += 1
        self.siz[rx] += self.siz[ry] # rx 側の siz を調整する
        return True

    # x を含む根付き木のサイズを求める
    def size(self, x):
        return self.siz[self.root(x)]




N, M = map(int, input().split())
G = [[] for i in range(N)]
uf = UnionFind(N)
ans = 1
for i in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    #閉路検出
    if uf.is_same(A, B):
        ans = 0
        continue
    uf.unite(A, B)
    # 頂点 A から頂点 B への辺を張る
    G[A].append(B)
    # 無向グラフの場合は次も実施
    G[B].append(A)

for i in range(N):
    if len(G[i]) > 2:
        ans = 0
        break

if ans == 1:
    print("Yes")
else:
    print("No")