from collections import Counter

N = int(input())
cnt = Counter()
for i in range(N):
    key = input()
    cnt[key] += 1
ans = sorted(cnt.items(), key=lambda i: i[1], reverse=True)
print(ans[0][0])