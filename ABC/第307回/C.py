def reproduce_sheet(A, B, X):
    HA, WA = len(A), len(A[0])
    HB, WB = len(B), len(B[0])
    HX, WX = len(X), len(X[0])

    # シートAとシートBを組み合わせてシートCを作成
    C = []
    for i in range(HX-HA):
        for j in range(WX-WA)


    # シートCからHX×WXの領域を切り出す
    extracted_sheet = []
    for i in range(HX):
        row = combined_C[i][0:WX]
        extracted_sheet.append(row)

    # 切り出したシートとシートXが一致するかどうかを判定
    if extracted_sheet == X:
        return "Yes"
    else:
        return "No"


HA, WA = map(int, input().split())
A = []
B = []
X = []
for _ in range(HA):
    A.append(input())

HB, WB = map(int, input().split())
for _ in range(HB):
    B.append(input())


HX, WX = map(int, input().split())
for _ in range(HX):
    X.append(input())