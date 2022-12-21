N , M = map(int, input().split())
S = [0] * N
mihon = "1" * M
#print(mihon)
ans_list = []
for i in range(N):
    S[i] = input()
    temp = []
    s = str()
    for j in range(M):
        if S[i][j] == "x":
            s += "0"
        else:
            s += "1"
    ans_list.append(int(s,2))
#print(ans_list)
ans = 0
for i in range(N):
    for j in range(i+1, N):
        #print(ans_list[i] | ans_list[j])
        temp = ans_list[i] | ans_list[j]
        #print(temp)
        if temp == int(mihon, 2):
            ans += 1

print(ans)