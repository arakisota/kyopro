from collections import defaultdict

N, K = map(int, input().split())

cnt = defaultdict(int)
medicine = 0
for _ in range(N):
    a, b = map(int, input().split())
    cnt[a] += b
    medicine += b

day = 1
for key in list(sorted(cnt.keys())):
    if medicine <= K:
        break
    medicine -= cnt[key]
    day = key + 1

print(day)