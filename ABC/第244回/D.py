"""
rgb 0 : 0回
brg -> bgr -> rgb 3 : 2回
rbg -> rgb 2 : 1回
rgb -> rgg
"""

S = list(input())
T = list(input())

x = sum(s != t for s, t in zip(S, T))

if x == 2:
    print("No")
else:
    print("Yes")