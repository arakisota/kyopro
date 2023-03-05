a, b = map(int, input().split())
ans = 0
if a == 10 or b == 10:
    if abs(a-b) == 9:
        ans = 1
if abs(a-b) == 1:
    ans = 1

if ans == 1:
    print("Yes")
else:
    print("No")