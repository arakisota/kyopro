A, B, C, D = map(int, input().split())

blue = A
red = 0
now = 0
if B >= C * D:
    print(-1)
else:
    while  blue > red * D:
        blue += B
        red += C
        now += 1
    print(now)