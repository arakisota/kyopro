N = int(input())
num = [i for i in range(1, 2*N+2)]

for i in range(2*N+1):
    if len(num) == 0:
            print(0)
            break
    if i % 2 != 0:
        aoki = int(input())
        num.pop(num.index(aoki))
    else:
        print(num.pop())