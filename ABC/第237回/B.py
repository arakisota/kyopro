H, W = map(int, input().split())
A = []
for i in range(H):
    A.append(list(map(int, input().split())))

B = [list(x) for x in list(zip(*A))]
for i in range(W):
    print(*B[i])