N, D = map(int, input().split())
T = list(map(int, input().split()))

judge = False
ans = 0
for i in range(1, N):
    if T[i] - T[i-1] <= D:
        judge = True
        ans = T[i]
        break

if judge:
    print(ans)
else:
    print(-1)