S = input()
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
ans = []
for s in S:
    ans.append(int(s))

print(list(set(num) - set(ans))[0])