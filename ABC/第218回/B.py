P = list(map(int, input().split()))
al = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"
, "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
ans = str()
for i in P:
    ans += al[i-1]
print(ans)