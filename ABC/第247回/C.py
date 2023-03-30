N = int(input())
s = "1"
ans = ["1"] * N
for i in range(1,N):
    ans[i] = ans[i-1] + " " + str(i+1) + " " + ans[i-1]
print(ans[-1])