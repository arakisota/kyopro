import math

K = int(input())

#素因数分解
#24 = 2^3 * 3^1 -> [[2, 3][3,1]]
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

def sisu(n):
    return math.floor(pow((2*n), 0.5))

factor = factorization(K)
answer = 0
temp = 0
for num in factor:
    if num[1] == 1:
        temp = max(temp, num[0])
    else:
        sisuu = sisu(num[1])
        answer = max(answer, num[0]**sisuu)

if temp > answer:
    print(temp)
else:
    print(answer)