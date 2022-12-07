N = int(input())
S = list(map(int, input().split()))

ans_list = [S[0]]
for i in range(1, len(S)):
    temp = S[i] - S[i-1]
    ans_list.append(temp)

print(* ans_list)