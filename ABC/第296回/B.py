num = []
alp = "abcdefgh"
for i in reversed(range(1, 9)):
    Q = input()
    if "*" in Q:
        num = Q.index("*")
        print(alp[num]+str(i))