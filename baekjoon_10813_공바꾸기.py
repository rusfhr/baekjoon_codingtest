# 바구니 n 개
# 각 바구니 1번부터 n번 번호
# 바구니에 공 1개씩
# 처음에는 바구니에 적힌 번호와 같은 번호 공 들어있음
# m번 공 바꿈
# 바구니에 들어있는 공 서로 바꿈

n, m = map(int, input().split())

baguni = [i for i in range(1, n + 1)]

i = 0

while i < m:
    a, b = map(int, input().split())
    a = a - 1
    b = b - 1
    
    if a != b:
        temp = ''

        temp = baguni[a]
        baguni[a] = baguni[b]
        baguni[b] = temp


    else:
        pass

    i += 1

for i in baguni:
    print(i, end = ' ')