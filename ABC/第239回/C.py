def dis5(x, y):
    p = [0] * 8
    p[0] = (x+2, y+1)
    p[1] = (x+2, y-1)
    p[2] = (x-2, y+1)
    p[3] = (x-2, y-1)
    p[4] = (x+1, y+2)
    p[5] = (x+1, y-2)
    p[6] = (x-1, y+2)
    p[7] = (x-1, y-2)

    return p

x1, y1, x2, y2 = map(int, input().split())
p1 = dis5(x1, y1)
p2 = dis5(x2, y2)

if len(set(p1) & set(p2)) == 0:
    print("No")
else:
    print("Yes")