N = int(input())

#再帰的に実施
def f(k):
    if k == 0:
        return 1
    else:
        return f(k//2) + f(k//3)

print(f(N))

#工夫する
