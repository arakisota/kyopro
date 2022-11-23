"""
modを工夫して使う
modは使うタイミングを自由に動かすことができる→ただ割り算は特殊ではある
そのため、計算する前に10000で割ることでオーバーフローを防ぐことができる
そして、引き算の途中で0を下回るときには10000を足す必要がある
操作が行われる度に、10000で割る
"""
N = int(input())
T = [0] * N
A = [0] * N

answer = 0
for i in range(N):
    T[i], A[i] = input().split()
    A[i] = int(A[i])

    if T[i] == "+":
        answer += int(A[i])
    elif T[i] == "-":
        answer -= int(A[i])
    else:
        answer *= int(A[i])

    if answer < 0:
        answer += 10000
    answer %= 10000
    print(answer)   