N, M = map(int, input().split())
a = list(map(int, input().split()))

tmp = []
ans = []
for i in range(1, N+1):
    if i in set(a):
        tmp.append(i)
    else:
        ans.append(i)
        for j in reversed(tmp):
            ans.append(j)
        tmp = []
print(*ans)