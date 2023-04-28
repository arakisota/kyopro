N = int(input())
A = []
B = []
for i in range(N):
    A.append(list(map(int, input().split())))

for i in range(N):
    B.append(list(map(int, input().split())))

def rotate(A):
    A_2 = []
    for i in range(N):
        tmp = []
        for j in range(N):
            i_2, j_2 = N-1-j, i
            tmp.append(A[i_2][j_2])
        A_2.append(tmp)
    return A_2

def check(A, B, N):
    a_1 = 0
    b_1 = 0
    for i in range(N):
        for j in range(N):
            if A[i][j] == 1:
                a_1 += 1
                if B[i][j] == 1:
                    b_1 += 1

    if a_1 == b_1:
        return True
    return False

A_2 = rotate(A)
A_3 = rotate(A_2)
A_4 = rotate(A_3)

ans = False
for a in [A, A_2, A_3, A_4]:
    if check(a, B, N):
        ans = True
        break

if ans:
    print("Yes")
else:
    print("No")