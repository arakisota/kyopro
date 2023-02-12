N = int(input())
S = list(map(int, input().split()))

tmp = set()
for a in range(1, 1001):
    for b in range(1, 1001):
        tmp.add(4*a*b + 3*a + 3*b)
cnt = 0
for i in S:
    if i  not in tmp:
        cnt += 1
print(cnt)