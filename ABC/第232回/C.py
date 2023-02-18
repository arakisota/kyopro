from itertools import permutations


def judge():
    def is_same_shape(P):
        for i in range(N):
            for j in range(N):
                if AB[P[i]][P[j]] != CD[i][j]: return False
        return True

    N, M = map(int, input().split())
    AB = [[False] * N for _ in range(N)]
    CD = [[False] * N for _ in range(N)]

    for _ in range(M):
        a, b = map(int, input().split())
        a, b = a - 1, b - 1
        AB[a][b] = True
        AB[b][a] = True

    for _ in range(M):
        c, d = map(int, input().split())
        c, d = c - 1, d - 1
        CD[c][d] = True
        CD[d][c] = True

    for perm in permutations(range(N)):
        if is_same_shape(perm):
            return True
    return False

print("Yes" if judge() else "No")