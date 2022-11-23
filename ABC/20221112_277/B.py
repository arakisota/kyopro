N = int(input())
S = [0] * N
judge_list = [0] * N
label_1 = ["H", "D", "C", "S"]
label_2 = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]
for i in range(N):
    S[i] = input()
    if S[i][0] in label_1:   
        judge_list[i] += 1
    if S[i][1] in label_2:
        judge_list[i] += 1
    if S[i] not in S[:i]:
        judge_list[i] += 1
    
if sum(judge_list) == 3 * N:
    print("Yes")
else:
    print("No")