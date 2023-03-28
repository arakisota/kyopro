from collections import Counter

N = int(input())
A = list(map(int, input().split()))
cnt = Counter()

for a in A:
    cnt[a] += 1

ans = 0
for i in set(A):
    tmp = cnt[i] // 2
    ans += tmp

print(ans)