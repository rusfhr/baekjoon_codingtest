a, b = map(int, input().split())

def transfer_matrix(num):
    i = 0
    matrix = []

    while i < num:
        values = input().split()
        matrix.append(values)
        i += 1

    for a in range(0, len(matrix)):
        for b in range(0, len(matrix)):
            matrix[a][b] = int(matrix[a][b])

    return matrix
    
matrix_a = transfer_matrix(a)
matrix_b = transfer_matrix(b)

matrix_total = []

for a, b in zip(matrix_a, matrix_b):
    matrix_total.append([x + y for x, y in zip(a, b)])

for i in range(0, len(matrix_total)):
    print(*matrix_total[i])