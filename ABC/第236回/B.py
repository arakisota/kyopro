from collections import Counter

N = int(input())
A = list(map(int, input().split()))
cnt = Counter()

for key in A:
    cnt[key] += 1

num = list(cnt.values()).index(3)
print(list(cnt.keys())[num])