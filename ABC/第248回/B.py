A, B, K = map(int, input().split())

ans = 0
while B - A > 0:
    A *= K
    ans += 1

print(ans)