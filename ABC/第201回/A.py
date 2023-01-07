"""
今回は愚直に6通りやったが、以下のような別解もある
（別解）
等差数列は単調増加・現象である必要があるため、最初に数列をソートして、その階差を取れば一致するはず。
→これだと以下のような愚直にやるより綺麗にコードが書ける
"""

A = list(map(int, input().split()))

if A[1] - A[0] == A[2] - A[1]:
    print("Yes")
elif A[2] - A[0] == A[1] - A[2]:
    print("Yes")
elif A[0] - A[1] == A[2] - A[0]:
    print("Yes")
elif A[2] - A[1] == A[0] - A[2]:
    print("Yes")
elif A[0] - A[2] == A[1] - A[0]:
    print("Yes")
else:
    print("No")
