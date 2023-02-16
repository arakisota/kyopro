N = int(input())
if N >= 42:
    ans = "AGC0"
    ans += str(N+1)
elif N <= 10:
    ans = "AGC00"
    ans += str(N)
else:
    ans = "AGC0"
    ans += str(N)
print(ans)