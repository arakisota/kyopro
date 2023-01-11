A, B, C = map(int, input().split())

def comp(A, B, C):
    if C % 2 == 0:
        A = abs(A)
        B = abs(B)

    if A > B:
        print(">")
    elif A == B:
        print("=")
    else:
        print("<")

comp(A, B, C)