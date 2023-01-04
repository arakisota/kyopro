N = int(input())

c = N  // 100
amari = N % 100
if amari == 0:
    print(c)
else:    
    print(c+1)