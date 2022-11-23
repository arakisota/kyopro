"""
・後ろから考える
→ 今回の場合は、最後に塗るタイルは3つ連続であるため、3つ連続の文字がない場合は
その時点でNoになる。
"""
N = int(input())
S = input()

Answer = False
for i in range(N-2):
    if S[i] == "R" and S[i+1] == "R" and S[i+2] == "R" :
        Answer = True
    if S[i] == "B" and S[i+1] == "B" and S[i+2] == "B":
        Answer = True
    
if Answer == True:
    print("Yes")
else:
    print("No")