N = int(input())
a = [[] for _ in range(N)]
a[0].append(1)
for i in range(1, N):
    for j in range(i+1):
        if j == 0 or i == j:
            a[i].append(1)
        else:
            tmp = a[i-1][j-1] + a[i-1][j]
            a[i].append(tmp)

for tmp in a:
    ans = str(tmp[0])
    for i in range(1, len(tmp)):
        ans += " "
        ans += str(tmp[i])
    print(ans)