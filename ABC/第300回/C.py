h, w = map(int, input().split())
S = [input() for _ in range(h)]
n = min(h, w)
ans = [0] * n
for i in range(1, h - 1):
    for j in range(1, w - 1):
        if S[i][j] == S[i - 1][j - 1] == S[i - 1][j + 1] == S[i + 1][j - 1] == S[i + 1][j + 1] == '#':
            c = -1
            for k in range(1, min(i, j) + 1):
                if S[i - k][j - k] == '.':
                    break
                c += 1
            ans[c] += 1
print(*ans)