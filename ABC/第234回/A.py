def f(t):
    return t**2 + 2*t + 3

t = int(input())
ans = f(f(f(t)+t)+f(f(t)))
print(ans)