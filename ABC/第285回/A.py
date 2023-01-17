a, b = map(int, input().split())

x1 = [2, 3]
x2 = [1, 4, 5]
x3 = [1, 6, 7]
x4 = [2, 8, 9]
x5 = [2, 10, 11]
x6 = [3, 12, 13]
x7 = [3, 14, 15]
x8 = [4]
x9 = [4]
x10 = [5]
x11 = [5]
x12 = [6]
x13 = [6]
x14 = [7]
x15 = [7]

def comp(a):
    if a == 1:
        return x1
    elif a == 2:
        return x2
    elif a == 3:
        return x3
    elif a == 4:
        return x4
    elif a == 5:
        return x5
    elif a == 6:
        return x6
    elif a == 7:
        return x7
    elif a == 8:
        return x8
    elif a == 9:
        return x9
    elif a == 10:
        return x10
    elif a == 11:
        return x11
    elif a == 12:
        return x12
    elif a == 13:
        return x13
    elif a == 14:
        return x14
    else:
        return x15

ans = comp(a)
if b in ans:
    print("Yes")
else:
    print("No")