N = int(input())
H = list(map(int, input().split()))

now = 0
for i in range(len(H)):
    if now < H[i]:
        now = H[i]
    else:
        print(now)
        break
    if i == len(H) - 1:
        print(now)