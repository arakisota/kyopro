N, K = map(int, input().split())
S = input()

ans = str()
num = 0

for s in S:
    if s == "x":
        ans += "x"
    elif s == "o" and num < K:
        ans += "o"
        num += 1
    else:
        ans += "x"
print(ans)