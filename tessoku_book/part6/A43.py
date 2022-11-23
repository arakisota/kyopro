N, L = map(int, input().split())
A = [0] * N
B = [0] * N

time_list = []
for i in range(N):
    A[i], B[i] = map(str, input().split())
    A[i] = int(A[i])
    if B[i] == "E":
        time_list.append(L-A[i])
    else:
        time_list.append(A[i])
print(max(time_list))