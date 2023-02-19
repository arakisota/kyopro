T = int(input())
for i in range(T):
    N, D, K = map(int, input().split())
    mass = [False] * N
    mass[0] = True
    x = 0
    for j in range(K):
        x = (x + D) % N
        if mass[x] == True:
            while mass[x] == False:
                x += 1
                x %= N
            mass[x] = True
    print(x)