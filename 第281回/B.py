S = input()
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

jedge = False
try:
    s_1 = S[0]
    s_6 = S[-1]
    s_25 = int(S[1:-1])

    if s_1 not in num == True and s_6 not in num == True:
        jedge = True
    if s_1.isupper() == True:
        jedge = True
    if s_6.isupper() == True:
        jedge = True
    if s_25 >= 100000 and s_25 <= 999999:
        jedge = True
    if s_25 < 100000 or s_25 > 999999:
        jedge = False
    if s_1.isupper() == False or s_6.isupper() == False:
        jedge = False
    if s_1 in num == True and s_6 in num == True:
        jedge = False
    if len(S) != 8:
        jedge = False
except:
    jedge = False

if jedge == True:
    print("Yes")
else:
    print("No")