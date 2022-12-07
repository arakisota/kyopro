H, W = map(int, input().split())
S = [0] * H

count = 0
for i in range(H):
    S[i] = input()
    for num in S[i]:
        if num == "#":
            count += 1

print(count)