"""
入力されるそれぞれの数字を2または3で割り切れるところまで割り切ってみる
・数字が揃う場合
この時点で数字が揃うはず
・数字が揃わない場合
この時点で-1を出力する

次に最小回数であるため、それぞれ2または3を何回割ったかを計算して、それぞれの最小値分かければ良い

"""

N = int(input())
a = list(map(int, input().split()))

min_list = []
count_list2 = []
count_list3 = []
for num in a:
    count_2 = 0
    count_3 = 0
    while True:
        if num % 2 == 0:
            num /= 2
            count_2 += 1
        elif num % 3 == 0:
            num /= 3
            count_3 += 1
        else:
            break
    min_list.append(num)
    count_list2.append(count_2)
    count_list3.append(count_3)

if len(set(min_list)) > 1:
    print(-1)
else:
    print(min(count_list2) + min(count_list3))