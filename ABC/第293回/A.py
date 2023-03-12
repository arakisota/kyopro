S = list(input())

ans = str()
for i in range(len(S)//2):
    ans += S[2*i+1]
    ans += S[2*i]

print(ans)