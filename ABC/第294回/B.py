from string import ascii_lowercase

H, W = map(int, input().split())
ans = []
s = ascii_lowercase.upper()
for i in range(H):
    tmp1 = str()
    tmp = list(map(int, input().split()))
    for j in tmp:
        if j == 0:
            tmp1 += "."
        else:
            tmp1 += s[j-1]
    ans.append(tmp1)

for i in ans:
    print(i)