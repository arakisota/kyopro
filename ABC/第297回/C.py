H, W = map(int, input().split())
for i in range(H):
    S = input()
    tmp1 = 0
    tmp2 = str()
    ans = str()
    for i in range(len(S)):
        tmp2 += S[i]
        if S[i] == "T":
            tmp1 += 1
        else:
            ans += tmp2
            tmp1 = 0
        if tmp1 == 2:
            ans += "PC"
            tmp1 = 0
            tmp2 = str()
    print(ans)