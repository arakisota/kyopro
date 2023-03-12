H, W = map(int, input().split())
A = []
for i in range(H):
    A.append(list(map(int, input().split())))

p = set()
def dfs(x, y, H, W, path):
    if x == H and y == W:
        p.add(path)
        return
    if x + 1 <= H:
        dfs(x + 1, y, H, W, path + 'D')
    if y + 1 <= W:
        dfs(x, y + 1, H, W, path + 'R')

path = str()
dfs(1, 1, H, W, path)

cnt = 0
for i in p:
    ans = set()
    ans.add(A[0][0])
    x = 1
    y = 1
    for j in range(len(i)):
        if i[j] == "D":
            y += 1
        if i[j] == "R":
            x += 1
        if A[x-1][y-1] not in ans:
            ans.add(A[x-1][y-1])
    if len(ans) == H+W-1:
        cnt += 1
print(cnt)