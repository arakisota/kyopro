import bisect

N = int(input())
A = list(map(int, input().split()))

T = list(set(A)) #setで重複を消す
T.sort()

B = [None] * N
for i in range(N):
    #これでA[i]が何番目に小さいかがわかる
    B[i] = bisect.bisect_left(T, A[i])
    B[i] += 1 #1からスタート

#答え空白区切りで出力
Answer = [str(i) for i in B]
print(" ".join(Answer)) #これで横並びに空白区切りで出力される