A, B, C = map(int, input().split())
if A > C and B < A + C:
    print(-1)
elif B < C:
    print(-1)
elif A <= C <= B:
    print(C)
elif A % C == 0:
    print(A)
elif B % C == 0:
    print(B)
else:
    print(C * ((A // C)+1))