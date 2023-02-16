A , B = map(str, input().split())

if len(A) > len(B):
    length = len(B)
else:
    length = len(A)

ans = 1
for i in range(length):
    tmp = int(A[len(A) - i - 1]) + int(B[len(B) - i - 1])
    if tmp >= 10:
        ans = 0
        break
if ans == 1:
    print("Easy")
else:
    print("Hard")