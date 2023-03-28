N = int(input())
W = list(map(str, input().split()))

ans = ["and", "not", "that", "the", "you"]
ans1 = 0

for i in W:
    if i in set(ans):
        ans1 = 1
        break

if ans1 == 1:
    print("Yes")
else:
    print("No")