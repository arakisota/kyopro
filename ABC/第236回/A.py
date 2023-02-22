S = input()
a, b = map(int, input().split())
ans = str()
for i in range(len(S)):
    if i == a-1:
        ans += S[b-1]
    elif i == b-1:
        ans += S[a-1]
    else:
        ans += S[i]

print(ans)