N = int(input())
p = list(map(int, input().split()))

num = [i for i in range(1, N+1)]
dict_a = dict(zip(p, num))

sort_p = sorted(p)
ans = []
for i in sort_p:
    ans.append(dict_a[i])
print(*ans)