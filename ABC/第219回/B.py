S = [0] * 3
for i in range(3):
    S[i] = input()
T = input()
ans = str()
for t in T:
    ans += S[int(t)-1]
print(ans)