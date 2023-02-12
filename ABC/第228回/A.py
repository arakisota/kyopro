S, T, X = map(int, input().split())

if S > T:
    T += 24
    if S <= X < T or S <= X+24 < T:
        print("Yes")
    else:
        print("No")
else:
    if S <= X < T:
        print("Yes")
    else:
        print("No")