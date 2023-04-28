"""
-o
o-
"""
N = int(input())
S = input()

ind = [0]
num = 0
for i in range(N):
    if S[i] == "-":
        ind.append(i+1)
    if S[i] == "o":
        num += 1

level = -1
for i in range(1, len(ind)):
    if num == 0:
        break
    if i == len(ind) - 1:
        level = max(len(S) - ind[-1], level)
    else:
        if level < ind[i] - ind[i-1]:
            level = ind[i] - ind[i-1] - 1
print(level)