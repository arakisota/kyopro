"""
繰り返し二乗法

割り算を*b^m-2で表す
"""
def power(a, b, m):
    p = a
    answer = 1
    for i in range(30):
        wari = 2 ** i
        #二進法表記における2^iが1であるときに繰り返し二乗法が使える
        if (b // wari) % 2 == 1:
            answer = (answer * p) % m
        p = (p * p) % m
    return answer

def Division(a, b, m):
    return (a * power(b, m-2, m)) % m

#入力
n, r = map(int, input().split())
m = 1000000007

#分子
a = 1
for i in range(1, n + 1):
    a = (a * i) % m
#分母
b = 1
for i in range(1, r+1):
    b = (b * i) % m
for i in range(1, n-r+1):
    b = (b * i) % m

print(Division(a, b, m))