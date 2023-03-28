import copy
R, C = map(int, input().split())
B = []
for i in range(R):
    B.append(list(input()))
ans = copy.deepcopy(B)
num = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

for i in range(R):
    for j in range(C):
        if B[i][j] in set(num):
            ans[i][j] = "."
            for k in range(R):
                for l in range(C):
                    d = abs(i-k) + abs(j-l)
                    if d <= int(B[i][j]):
                        ans[k][l] = "."
        else:
            pass

for i in range(R):
    ans1 = str()
    for j in range(C):
        ans1 += ans[i][j]
    print(ans1)