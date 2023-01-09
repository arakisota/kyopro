N, K = map(int, input().split())

temp = int((1+K) * K / 2)
ans = 0
for i in range(1, N+1):
    ans += 100 * i * K
    ans += temp

print(ans)