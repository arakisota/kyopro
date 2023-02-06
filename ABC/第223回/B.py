S = input()
ans = []
for i in range(len(S)):
        tmp = S[i:] + S[:i]
        ans.append(tmp)

ans_sort = sorted(ans)
print(ans_sort[0])
print(ans_sort[-1])