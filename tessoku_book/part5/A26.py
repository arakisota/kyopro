#入力
from operator import is_


Q = int(input())
X = [0] * Q

for i in range(Q):
    X[i] = int(input())

def is_prime(num):
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

"""
素数はその数のルートを取った数で見ていけば十分
"""
for num in X:
    if is_prime(num) == True:
        print("Yes")
    else:
        print("No")
    