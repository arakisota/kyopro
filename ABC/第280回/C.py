S = input()
T = input()

answer_list = []
for i in range(len(S)):
    if S[i] != T[i]:
        answer_list.append(i+1)

if len(answer_list) == 0:
    print(len(S)+1)
else:
    print(answer_list[0])