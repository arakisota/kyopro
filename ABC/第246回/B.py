A, B = map(int, input().split())

if A != 0:
    m = B / A
    x = pow(1 / (1+m**2), 1/2)
    y = pow(1-x**2, 1/2)
else:
    x = 0
    y = 1

print(x, end=" ")
print(y)