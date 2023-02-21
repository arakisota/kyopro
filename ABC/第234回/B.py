N = int(input())
x = [0] * N
y = [0] * N
for i in range(N):
    x[i], y[i] = map(int, input().split())

def length(x1, y1, x2, y2):
    return pow(pow(x2- x1, 2) + pow(y2 - y1, 2), 1/2)

ans = 0
for i in range(N):
    for j in range(i+1, N):
        ans = max(ans, length(x[i], y[i], x[j], y[j]))

print(ans)