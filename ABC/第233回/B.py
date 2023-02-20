L, R = map(int, input().split())
S = input()

tmp = S[L-1:R]
ans = str()
for s in S[:L-1]:
    ans += s
for s in reversed(tmp):
    ans += s
for s in S[R:]:
    ans += s

print(ans)