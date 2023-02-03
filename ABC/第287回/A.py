N = int(input())
cnt = 0
for i in range(N):
    S = input()
    if S == "For":
        cnt += 1
if cnt >= (N//2+1):
    print("Yes")
else:
    print("No")