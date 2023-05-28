N = int(input())
S = input()
T = input()

ans = 0
tmp = ["0o", "o0", "1l", "l1"]
for i in range(N):
    tmp3 = S[i] + T[i]
    if S[i] == T[i]:
        ans += 1
    elif tmp3 in set(tmp):
        ans += 1
    else:
        pass

if ans == N:
    print("Yes")
else:
    print("No")