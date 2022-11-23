"""
偶数と奇数で分けて、それぞれソートすることで二つの数字の最大の和が出しやすくなる
"""

N = int(input())
A = list(map(int, input().split()))
even_list = []
odd_list = []
even = 0
odd = 0

for num in A:
    if num % 2 == 0:
        even += 1
        even_list.append(num)
    else:
        odd += 1
        odd_list.append(num)

if even >= 2 and odd >= 2:
    even_list = sorted(even_list)
    odd_list = sorted(odd_list)
    print(max(even_list[-1] + even_list[-2], odd_list[-1] + odd_list[-2])) 
elif even >= 2:
    even_list = sorted(even_list)
    print(even_list[-1] + even_list[-2])
elif odd >= 2:
    odd_list = sorted(odd_list)
    print(odd_list[-1] + odd_list[-2]) 
else:
    print("-1")