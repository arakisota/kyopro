"""
方針
まず前後左右に振るコードを書く
その上で、新たに追加されたキャンディーから一番近い同じ種類のキャンディーまでの距離を算出する
その時に前後左右した時それぞれで計算して、最大の選択肢を選び続ける

常に4パターンの結果を確認するやり方もある
Ptについても各行の0の数で番号を特定することができる
"""
import bisect

from numpy import insert


#キャンディー味の情報
f = list(map(int, input().split()))

#二次元平面
box = [0 * 10 for i in range(10)]

def forward(candy):

    return candy

def backward(candy):

    return candy

def Right(box):
    for j in range(10):
        candy = box[j] 
        candy = [i for i in candy if i == 0]
        for _ in range(10 - len(candy)):
            candy.insert(0, 0)

    return candy

def Left(box):
    for j in range(10):
        candy = box[j] 
        candy = [i for i in candy if i == 0]
        for _ in range(10 - len(candy)):
            candy.append(0)

    return candy

#累積和を取って、どこに入力するかをわかるようにする
def insert_t(box, t):
    count = [0 * 10]
    count_sum = [0 * 11]
    for i in range(10):
        count[i] = 10 - box[i].count(0) 
        count_sum[i+1] = count_sum[i] + count[i]
    insert_row = bisect.bisect(count_sum, t) - 1
    insert_col = t - count_sum[insert_row]
    box[insert_row][box[insert_row].index(0) + insert_col -1] = t

    return box

#Ptの入力
for i in range(100):
    t = int(input())
    box = insert_t(t)
    box = Right(box)
    print("R")
