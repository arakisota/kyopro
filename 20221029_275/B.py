A, B, C, D, E, F = map(int, input().split())
answer = (A*B*C) - (D*E*F)

print(answer%998244353)