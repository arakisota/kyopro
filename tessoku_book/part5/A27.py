def gcd(a, b):
    while a != 0 and b != 0:
        if a >= b:
            a = a % b
        else:
            b = b % a
    if a != 0:
        return a
    else:
        return b

#入力
A, B = map(int, input().split())

print(gcd(A, B))