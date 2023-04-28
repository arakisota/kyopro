from collections import defaultdict

cnt = defaultdict(list)
S = input()
for i in range(len(S)):
    cnt[S[i]].append(i+1)

judge = 0
if sum(cnt["B"]) % 2 == 1:
    judge += 1
a = cnt["R"]
a.sort()
if a[0] < int(cnt["K"][0]) < a[1]:
    judge += 1

if judge == 2:
    print("Yes")
else:
    print("No")