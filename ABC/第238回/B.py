N = int(input())
A = list(map(int, input().split()))

angle = 0
tmp = []
ans = []
for a in A:
    angle += a
    angle %= 360
    tmp.append(angle)

max_a = 0
tmp.sort(reverse=True)
for i in range(len(tmp)):
    if i == 0:
        max_a = max(max_a, 360 - tmp[i])
    elif i == len(tmp) - 1:
        max_a = max(max_a, tmp[i])
    else:
        max_a = max(max_a, tmp[i-1] - tmp[i])

print(max_a)