import copy
S = input()
T = input()

ans = 0
if S == T:
    ans = 1
else:
    for i in range(len(S)-1):
        tmp = copy.copy(S)
        if i == 0:
            tmp = S[i+1] + S[i] + S[i+2:]
        elif i == len(S)-1:
            tmp = S[:i] + S[i+1] + S[i]
        else:
            tmp = S[:i] + S[i+1] + S[i] + S[i+2:]
        if tmp == T:
            ans = 1
            break
if ans == 1:
    print("Yes")
else:
    print("No")