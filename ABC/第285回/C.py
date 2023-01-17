S = input()

def f(N):
    return int(26 * ((26**N)-1) / 25)

length = len(S)
s = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
ans = f(length-1)

for i in range(len(S)):
    idx = s.index(S[i]) + 1 #何番目か
    j = length - i #何桁目か
    if i == len(S)-1:
        temp = idx * pow(26, j-1)
    elif idx == 1:
        temp = 0
    else:
        temp = (idx-1) * pow(26, j-1)
    ans += temp

print(ans)