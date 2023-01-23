S = [None] * 4
ans = []
for i in range(4):
    S[i] = input()
    ans.append(S[i])

if len(set(ans)) == 4:
    print("Yes")
else:
    print("No")