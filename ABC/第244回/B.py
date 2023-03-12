N = int(input())
S = input()

d = 0
n = 0
e = 0
w = 0
s = 0

for i in range(N):
    if S[i] == "R":
        d += 1
    else:
        if d % 4 == 0:
            e += 1
        elif d % 4 == 1:
            s += 1
        elif d % 4 == 2:
            w += 1
        elif d % 4 == 3:
            n += 1

x = e - w
y = n - s

print(x, y)