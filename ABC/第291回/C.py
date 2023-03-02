N = int(input())
S = input()

count = 0

x = 0
y = 0

ans = set()
ans.add((0, 0))
for i in range(N):
    if S[i] == "R":
        x += 1
    elif S[i] == "L":
        x -= 1
    elif S[i] == "U":
        y += 1
    else:
        y -= 1
    ans.add((x, y))
    #print(ans)
    if len(ans) != i+2:
        count = 1
        break

if count == 1:
    print("Yes")
else:
    print("No")