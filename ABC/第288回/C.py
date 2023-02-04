class UnionFind:
    def __init__(self, n):
        self.p = [-1 for i in range(n)]

    def find(self, x):
        if self.p[x] < 0:
            return x
        else:
            self.p[x] = self.find(self.p[x])
            return self.p[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        if self.p[x] > self.p[y]:
            x, y = y, x
        self.p[x] += self.p[y]
        self.p[y] = x
        return True

    def same(self, x, y):
        return self.find(x) == self.find(y)

N, M = map(int, input().split())
G = UnionFind(N)
ans = 0
for i in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    if G.same(A, B):
        ans += 1
    else:
        G.unite(A, B)
print(ans)
