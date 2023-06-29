N = int(input())

S = []
for i in range(N):
    S.append(input())

flag = False
for i in range(N):
    for j in range(i+1, N):
        tmp1 = S[i] + S[j]
        tmp2 = S[j] + S[i]
        if tmp1 == tmp1[::-1] or tmp2 == tmp2[::-1]:
            flag = True
            break

if flag:
    print("Yes")
else:
    print("No")