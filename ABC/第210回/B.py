N = int(input())
S = input()
ans = int()
for i in range(N):
    if S[i] == "1":
        ans = i+1
        break

if ans % 2 == 1:
    print("Takahashi")
else:
    print("Aoki")