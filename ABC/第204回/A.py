"""
(別解)
あいこになる必要十分条件はx + y + z = 0 (mod3)になることである
"""
x, y = map(int, input().split())
if x != y:
    print(3 - x - y)
else:
    print(x)