A, B = map(int, input().split())
mass = set()
mass.add((1,2))
mass.add((2,3))
mass.add((4,5))
mass.add((5,6))
mass.add((7,8))
mass.add((8,9))

if (A, B) in mass:
    print("Yes")
else:
    print("No")